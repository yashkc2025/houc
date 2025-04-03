import { createRouter, createWebHistory } from "vue-router";
import LoginView from "@/views/auth/LoginView.vue";
import RegisterView from "@/views/auth/RegisterView.vue";
import ForgotView from "@/views/auth/ForgotView.vue";
import sitemap from "@/assets/sitemap";
import HomeView from "@/views/HomeView.vue";
import ServiceView from "@/views/ServiceView.vue";
import HistoryView from "@/views/HistoryView.vue";
import AccountView from "@/views/AccountView.vue";
import AdminAuthView from "@/views/auth/AdminAuthView.vue";
import AdminDashboardView from "@/views/admin/AdminDashboardView.vue";
import ProfessionalView from "@/views/ProfessionalView.vue";
import ProfessionalLoginView from "@/views/professional/ProfessionalLoginView.vue";
import ProfessionalRegisterView from "@/views/professional/ProfessionalRegisterView.vue";
import ProfessionalForgotView from "@/views/professional/ProfessionalForgotView.vue";
import TestView from "@/views/TestView.vue";
import LogoutView from "@/views/auth/LogoutView.vue";
import SummaryView from "@/views/admin/SummaryView.vue";
import CustomerManageView from "@/views/admin/CustomerManageView.vue";
import ProfessionalManageView from "@/views/admin/ProfessionalManageView.vue";
import ServiceManageView from "@/views/admin/ServiceManageView.vue";
import CreateServiceView from "@/views/admin/CreateServiceView.vue";
import ProfessionalDashView from "@/views/professional/ProfessionalDashView.vue";
import ProfessionalAccountView from "@/views/professional/ProfessionalAccountView.vue";
import ProfessionalSummaryView from "@/views/professional/ProfessionalSummaryView.vue";
import AdminAccountView from "@/views/admin/AdminAccountView.vue";
import SearchView from "@/views/SearchView.vue";
import RequestManageView from "@/views/admin/RequestManageView.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "Home",
      component: HomeView,
    },
    {
      path: sitemap.auth.login,
      name: "login",
      component: LoginView,
    },
    {
      path: sitemap.auth.logout,
      name: "logout",
      component: LogoutView,
    },
    {
      path: sitemap.auth.register,
      name: "register",
      component: RegisterView,
    },
    {
      path: sitemap.auth.admin,
      name: "admin",
      component: AdminAuthView,
    },
    {
      path: sitemap.admin.config,
      name: "account_admin",
      component: AdminAccountView,
    },
    {
      path: sitemap.admin.manage_users,
      name: "manage_users",
      component: CustomerManageView,
    },
    {
      path: sitemap.admin.manage_professionals,
      name: "manage_professionals",
      component: ProfessionalManageView,
    },
    {
      path: sitemap.admin.manage_services,
      name: "manage_services",
      component: ServiceManageView,
    },
    {
      path: sitemap.admin.manage_requests,
      name: "manage_requests",
      component: RequestManageView,
    },
    {
      path: sitemap.auth.professional_login,
      name: "professional_login",
      component: ProfessionalLoginView,
    },
    {
      path: sitemap.auth.professional_register,
      name: "professional_register",
      component: ProfessionalRegisterView,
    },
    {
      path: sitemap.auth.professional_forgot,
      name: "professional_forgot",
      component: ProfessionalForgotView,
    },
    {
      path: sitemap.admin.dash,
      name: "admin-dash",
      component: AdminDashboardView,
    },
    {
      path: sitemap.admin.create_service,
      name: "create-service",
      component: CreateServiceView,
    },
    {
      path: sitemap.admin.summary,
      name: "admin-summary",
      component: SummaryView,
    },
    {
      path: sitemap.auth.forgot,
      name: "forgot password",
      component: ForgotView,
    },
    {
      path: sitemap.professional.dash,
      name: "professional-dash",
      component: ProfessionalDashView,
    },
    {
      path: sitemap.account.professional_config,
      name: "professional-account-config",
      component: ProfessionalAccountView,
    },
    {
      path: sitemap.professional.summary,
      name: "professional-summary",
      component: ProfessionalSummaryView,
    },
    {
      path: sitemap.services.fn(":category"),
      name: "services",
      component: ServiceView,
    },
    {
      path: sitemap.services.history,
      name: "history",
      component: HistoryView,
    },
    {
      path: sitemap.services.search,
      name: "search",
      component: SearchView,
    },
    {
      path: sitemap.services.professional,
      name: "professional",
      component: ProfessionalView,
    },
    {
      path: sitemap.account.config,
      name: "account",
      component: AccountView,
    },
    {
      path: "/test",
      name: "test",
      component: TestView,
    },
  ],
});

export default router;
