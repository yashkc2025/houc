from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///household.db", echo=True)

with engine.connect() as connection:
    result = connection.execute(text('select "1"'))


session = Session(bind=engine)
