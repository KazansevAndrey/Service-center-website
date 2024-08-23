<template>
  <header class="menu">
    <div class="container">
      <div class="navbar navbar-dark bg-primary navbar-expand-lg">
        <a class="navbar-brand" href="/">
          <img :src="logo" />
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarContent">
          <ul class="navbar-nav ms-auto me-2" _msthash="234">
            
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button"
                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Каталог услуг
              </a>
              <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <a v-for="service in services" :key="service.id" class="dropdown-item" :href="`/services/${service.id}`">
                  {{ service.category_name }}
                </a>
                <a class="dropdown-item" href='/make-an-appointment'> Вызов мастера </a>
              </div>
            </li>
            
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-bs-toggle="dropdown"
                aria-haspopup="true" aria-expanded="false">
                О компании
              </a>
              <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <a class="dropdown-item" href="/about">О нас</a>
                <a class="dropdown-item" href="/vacancies">Вакансии</a>
              </div>
            </li>
            <li class="nav-item">
              <a href="/repair-status" class="nav-link">Статус ремонта</a>
            </li>
           
            <li class="nav-item">
              <button type="button" class=" nav-link"
                style=" font-size: 18px; font-weight: 500; background-color: inherit !important; border: none;" @click="ChangeTheme()">
                Поменять тему
              </button>
            </li>
            <li v-if="!isAuthenticate" class="nav-item">
              <a href="/login" class="nav-link">Вход</a>
            </li>
            <li style="display: flex; text-align: center" v-if="isAuthenticate" class="nav-item">
              <a @click="UserLogout" href="/" class="nav-link" style="margin-right: 20px">Выход</a>
            </li>
            <span v-if="isAuthenticate" class="nav-link" style="color:white; vertical-align: center; text-decoration: none">Здравствуйте {{user.first_name}} !</span>

          </ul>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import Cookies from "js-cookie";
import logo from "@/assets/images/Logo.svg";
import { getServices } from '../api/services-list(header)';
import store from "@/stores";
export default {
  name: "NavComponent",
  data() {
    return {
      services: [],
      logo,
    };
  },
  computed: {
    user(){
      console.log("UUUUSERRRRRRRRR", store.state.auth.authUser)
      return store.state.auth.authUser
  },
  isAuthenticate(){
      return store.state.auth.isAuthenticated
  }},
  created() {
    this.loadServices()
  },
  methods: {
    async loadServices() {
      this.services = await getServices();},
    UserLogout() {
      store.commit('auth/logout')
    },
    Theme1() {
      // Проверка наличия элементов
      var head = document.querySelector(".menu");
      if (head) {
        head.classList.remove("bg-dark");
      }

      var navB = document.querySelector(".navbar");
      if (navB) {
        navB.classList.remove("bg-dark");
        navB.classList.add("bg-primary");
      }

      var butt = document.querySelectorAll(".btn-secondary");
      butt.forEach((element) => {
        if (!element.classList.contains("btnClose")) {
          element.classList.remove("btn-secondary");
          element.classList.add("btn-primary");
        }
      });

      var modalHead = document.querySelector(".formHeader");
      if (modalHead) {
        modalHead.classList.remove("bg-dark");
      }

      var modalFooter = document.querySelector(".formFooter");
      if (modalFooter) {
        modalFooter.classList.remove("bg-dark");
      }

      var headerText = document.querySelector(".headerText");
      if (headerText) {
        headerText.style.color = "black";
      }

      var btnClose = document.querySelector(".btn-close");
      if (btnClose) {
        btnClose.style.background = "#6c757d";
      }

      var footerColor = document.querySelector("footer");
      if (footerColor) {
        footerColor.classList.remove("bg-dark");
      }

      var footerText = document.querySelectorAll("footer p");
      footerText.forEach((element) => {
        element.style.color = "black";
      });

      var footerLink = document.querySelectorAll("footer a");
      footerLink.forEach((element) => {
        element.style.color = "black";
      });
    },
    Theme2() {

      var head = document.querySelector(".menu");
      if (head) {
        head.classList.add("bg-dark");
      }

      var navB = document.querySelector(".navbar");
      if (navB) {
        navB.classList.add("bg-dark");
        navB.classList.remove("bg-primary");
      }

      var butt = document.querySelectorAll(".btn-primary");
      butt.forEach((element) => {
        element.classList.add("btn-secondary");
        element.classList.remove("btn-primary");
      });

      var modalHead = document.querySelector(".formHeader");
      if (modalHead) {
        modalHead.style.background = "black";
      }

      var modalFooter = document.querySelector(".formFooter");
      if (modalFooter) {
        modalFooter.classList.add("bg-dark");
      }

      var headerText = document.querySelector(".headerText");
      if (headerText) {
        headerText.style.color = "white";
      }

      var btnClose = document.querySelector(".btn-close");
      if (btnClose) {
        btnClose.style.background = "#6c757d";
      }

      var footerColor = document.querySelector("footer");
      if (footerColor) {
        footerColor.classList.add("bg-dark");
      }

      var footerText = document.querySelectorAll("footer p");
      footerText.forEach((element) => {
        element.style.color = "white";
      });

      var footerLink = document.querySelectorAll("footer a");
      footerLink.forEach((element) => {
        element.style.color = "white";
      });
    },
    ChangeTheme() {
      var theme = Cookies.get("theme");
      
      if (theme == "2" || theme === null) {
        Cookies.set("theme", "1");
        this.Theme1();
      } else {
        Cookies.set("theme", "2");
        this.Theme2();
      }
    },
    SetTheme() {
      var theme = Cookies.get("theme");
      
      if (theme == "2" || theme === null) {
        this.Theme2();
      } else {
        this.Theme1();
      }
    },
  },
  mounted() {
    this.SetTheme();
  }
};
</script>

<style scoped>
/* Меню */
.nav-link {
  color: white !important;
}

.nav-link:hover {
  color: #cadfff !important;
}

.interpreter,
.breadcrumbs {
  color: rgb(127, 127, 127);
  text-decoration: none;
}

.interpreter:hover {
  text-decoration: underline;
}

.nav-link,
.dropdown-menu,
.dropdown-item {
  font-weight: 500;
  font-size: 18px;
}

.menu {
  background-color: #0d6efd;
}

.navbar-brand img {
  height: 80% !important;
  width: 80% !important;
}
</style>
