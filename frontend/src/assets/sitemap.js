const sitemap = {
  auth: {
    login: "/auth/login",
    logout: "/auth/logout",
    register: "/auth/register",
    forgot: "/auth/forgot",
    admin: "/auth/admin",
    professional_login: "/auth/professional/login",
    professional_register: "/auth/professional/register",
    professional_forgot: "/auth/professional/forgot",
  },
  services: {
    dash: "/service/dash",
    fn: (a) => sitemap.services.dash + "/" + a,
    history: "/history",
    search: "/search",
    professional: "/service/professional",
  },
  account: {
    config: "/account/config",
    professional_config: "/account/professional",
  },
  admin: {
    dash: "/admin",
    config: "/admin/config",
    search: "/admin/search",
    summary: "/admin/summary",
    manage_users: "/admin/users",
    manage_professionals: "/admin/professionals",
    manage_requests: "/admin/requests",
    manage_services: "/admin/services",
    create_service: "/admin/create_service",
  },
  professional: {
    dash: "/professional",
    search: "/professional/search",
    summary: "/professional/summary",
  },
};

export default sitemap;
