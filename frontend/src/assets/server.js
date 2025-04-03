const serverLocation = "http://localhost:5000/";
const l = (a) => serverLocation + a;

const server = {
  auth: {
    user_register: l("user/user_register"),
    user_login: l("user/user_login"),
    professional_register: l("user/professional_register"),
    professional_login: l("user/professional_login"),
    admin_login: l("user/admin_login"),
    logout: l("user/logout"),
  },
  account: {
    user_details: l("user/get_user_details"),
    update_user_details: l("user/update_profile_user"),
  },
  service: {
    get_types: l("general/get_service_types"),
    create_service: l("manage/create_service"),
    get_services: l("general/get_services"),
    book_service: l("general/book_service"),
    history: l("general/get_history"),
    close_request: l("general/close_request"),
  },
  professionals: {
    get_professional: l("manage/list_professionals"),
    get_requests: l("general/get_requests"),
    accept_request: l("general/accept_request"),
    reject_request: l("general/reject_request"),
    professional_summary: l("general/professional_summary"),
  },
  admin: {
    get_users: l("manage/list_customers"),
    summary: l("manage/get_summary"),
    block_user: l("manage/block_user"),
    unblock_user: l("manage/unblock_user"),
    block_professional: l("manage/block_professional"),
    approve_professional: l("manage/approve_professional"),
    unblock_professional: l("manage/unblock_professional"),
    delete_service: l("manage/delete_service"),
    get_requests: l("manage/get_requests"),
    get_doc: l("manage/get_doc"),
  },
};

export default server;
