
import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "../views/LoginView.vue"
import RegisterView from "../views/RegisterView.vue"
import ServiceView from '../views/ServiceView.vue'
import AppointmentView from '@/views/AppointmentView.vue'
import AboutView from '@/views/AboutView.vue'
import VacanciesView from '@/views/VacanciesView.vue'
import RepairStatusView from '@/views/RepairStatusView.vue'
import EmployeeLoginView from '@/views/EmployeeLoginView.vue'
import EmployeePageApplicationsView from '@/views/EmployeePageApplicationsView.vue'
import ApplicationView from '@/views/ApplicationView.vue'

import store from "@/stores";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/registration",
    name: "registration",
    component: RegisterView,
  },
  {
    path: "/services/:category_id",
    name: "service",
    component: ServiceView,
    props: true,
  },
  {
    path: "/make-an-appointment",
    name: "appoinment",
    component: AppointmentView,
    meta: {
      requiresAuth: true // 
    },
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,
  },
  {
    path: "/vacancies",
    name: "vacancies",
    component: VacanciesView,
  },

  {
    path: "/repair-status",
    name: "repair-status",
    component: RepairStatusView,
    meta: {
      requiresAuth: true // Add meta field to indicate protected route
    },
  },
  {
    path: "/employee-login",
    name: "employee-login",
    component: EmployeeLoginView,
  },
  {
    path: "/employee-page-applications",
    name: "employee-page-applications",
    component: EmployeePageApplicationsView,
    meta: {
      requiresEmployees: true // 
    },
  },
  {
    path: "/employee-page-applications/:category_name/:application_id",
    name: "application",
    component: ApplicationView,
    meta: {
      requiresEmployees: true // 
    },
    props: true,
  },
];

const router = createRouter({
  routes,
  history: createWebHistory()
});

router.beforeEach(async (to, from, next) => {
  if (to.meta.requiresAuth) {
    let isAuthenticated = await store.getters['auth/isUserAuthenticated']
    if (isAuthenticated) {
      // User is authenticated, proceed to the route
      next();
    } else {
      // User is not authenticated, redirect to login
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      });
    }
  } 
  //Если доступ только сотрудникам
  if (to.meta.requiresEmployees) {
    const isEmployee = await store.getters['auth/isEmployee']
    if (isEmployee == true) {
      next();
    } else {
      next({
        path: '/employee-login',
        query: { redirect: to.fullPath }
      });
    }
  } else {
    next();
  }
}
);

export default router;
