from sqlalchemy import (
    Column,
    String,
    Text,
    Enum,
    ForeignKey,
    Integer,
    Boolean,
    create_engine,
    TIMESTAMP,
)
import enum
from datetime import datetime, timedelta
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from nanoid import generate
import os
from bcrypt import hashpw, gensalt
from sqlalchemy.inspection import inspect


current_dir = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{current_dir}/household.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    __abstract__ = True
    id = Column(String, primary_key=True, default=generate, unique=True)
    date_created = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    date_updated = Column(TIMESTAMP, nullable=False,
                          default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self, r=False):
        """Convert SQLAlchemy model instance to dictionary, with optional relationships."""
        data = {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}

        # Convert bytes fields to a string (or another suitable format)
        for key, value in data.items():
            if isinstance(value, bytes):
                # You can adjust the decoding format as needed.
                data[key] = value.decode('utf-8', 'ignore')
            if isinstance(value, enum.Enum):
                data[key] = value.value
        if r:
            for relationship in inspect(self).mapper.relationships:
                related_value = getattr(self, relationship.key)
                if related_value is not None:
                    if relationship.uselist:
                        # For lists (one-to-many, many-to-many)
                        data[relationship.key] = [item.to_dict()
                                                  for item in related_value]
                    else:
                        # For single items (many-to-one, one-to-one)
                        data[relationship.key] = related_value.to_dict()

        return data


class UserTypes(enum.Enum):
    ADMIN = "admin"
    USER = "user"


class RequestStatus(enum.Enum):
    REQUESTED = "requested"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    COMPLETED = "complete"


class User(Base):
    __tablename__ = "users"
    user_type = Column(Enum(UserTypes), nullable=False, default=UserTypes.USER)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    address = Column(Text, nullable=True)
    phone = Column(String(10), nullable=False)
    pincode = Column(String(6), nullable=False)
    is_blocked = Column(Boolean, nullable=False, default=False)

    # Relationships
    reviews = relationship("Review", back_populates="user")
    service_requests = relationship("ServiceRequest", back_populates="user")


class ServiceType(Base):
    __tablename__ = "service_types"
    name = Column(String, nullable=False)

    services = relationship("Service", back_populates="service_type")


class ServiceProfessional(Base):
    __tablename__ = "service_professionals"
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    address = Column(Text, nullable=False)
    pincode = Column(String(6), nullable=False)
    proof_document = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    experience = Column(Integer, nullable=False)
    phone = Column(String(10), nullable=False)
    is_approved = Column(Boolean, nullable=False, default=False)
    is_blocked = Column(Boolean, nullable=False, default=False)
    service_type_id = Column(String, ForeignKey(
        "service_types.id"), nullable=False)

    # Relationships
    service_type = relationship("ServiceType", backref="service_professionals")
    reviews = relationship("Review", back_populates="service_professional")
    service_requests = relationship(
        "ServiceRequest", back_populates="service_professional")


class Service(Base):
    __tablename__ = "services"
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    time_required = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)
    service_type_id = Column(String, ForeignKey(
        "service_types.id"), nullable=False)
    is_active = Column(Boolean, default=True)

    # Relationships
    service_type = relationship("ServiceType", back_populates="services")
    service_requests = relationship("ServiceRequest", back_populates="service")


class Review(Base):
    __tablename__ = "reviews"
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    service_professional_id = Column(String, ForeignKey(
        "service_professionals.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    review = Column(Text, nullable=True)
    request_id = Column(String, ForeignKey(
        "service_requests.id"), nullable=False)

    # Relationships
    user = relationship("User", back_populates="reviews")
    service_professional = relationship(
        "ServiceProfessional", back_populates="reviews")
    request = relationship("ServiceRequest", back_populates="review")


class ServiceRequest(Base):
    __tablename__ = "service_requests"
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    service_professional_id = Column(String, ForeignKey(
        "service_professionals.id"), nullable=False)
    request_status = Column(Enum(RequestStatus),
                            nullable=False, default=RequestStatus.REQUESTED)
    date_completed = Column(TIMESTAMP, nullable=True)

    service_id = Column(String, ForeignKey("services.id"), nullable=False)
    # Relationships
    user = relationship("User", back_populates="service_requests")
    service_professional = relationship(
        "ServiceProfessional", back_populates="service_requests")
    service = relationship("Service", back_populates="service_requests")
    review = relationship("Review", back_populates="request")


class Tokens(Base):
    __tablename__ = "tokens"
    owner_id = Column(String),
    date_expiry = Column(TIMESTAMP, nullable=False,
                         default=datetime.utcnow + timedelta(minutes=10))


Base.metadata.create_all(bind=engine)


def create_default_user():
    db_session = SessionLocal()
    existing_user = db_session.query(User).filter_by(
        email='admin@household.com').first()

    if not existing_user:
        try:
            new_user = User(
                name="admin",
                password=hashpw("admin".encode("utf-8"), gensalt()),
                email="admin@household.com",
                phone="11111111",
                user_type=UserTypes.ADMIN,
            )

            db_session.add(new_user)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            print(f"An error occurred: {e}")

    db_session.close()


def create_service_types():
    db_session = SessionLocal()

    s_types = ["Cleaning", "Salon", "Electrician",
               "Plumbing", "Painting", "Gardening", "Cooking"]

    for s in s_types:
        # Check if the service type already exists
        existing_service_type = db_session.query(
            ServiceType).filter_by(name=s).first()

        if not existing_service_type:
            # If it doesn't exist, add it
            service_type = ServiceType(name=s)
            db_session.add(service_type)

    # Commit the changes and close the session
    db_session.commit()
    db_session.close()


create_default_user()
create_service_types()
