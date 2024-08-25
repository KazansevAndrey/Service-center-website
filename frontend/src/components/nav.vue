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
                <a v-for="service in services" :key="service.id" class="dropdown-item"
                  :href="`/services/${service.id}`">
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
                style=" font-size: 18px; font-weight: 500; background-color: inherit !important; border: none;"
                @click="ChangeTheme()">
                Поменять тему
              </button>
            </li>
            <li v-if="!isAuthenticate" class="nav-item">
              <a href="/login" class="nav-link">Вход</a>
            </li>
            <li style="display: flex; text-align: center" v-if="isAuthenticate" class="nav-item">
              <a @click="UserLogout" href="/" class="nav-link" style="margin-right: 20px">Выход</a>
            </li>
            <span v-if="isAuthenticate" class="nav-link"
              style="color:white; vertical-align: center; text-decoration: none">Здравствуйте {{ user.first_name }}
              !</span>

          </ul>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
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
    user() {
      console.log("UUUUSERRRRRRRRR", store.state.auth.authUser)
      return store.state.auth.authUser
    },
    isAuthenticate() {
      return store.state.auth.isAuthenticated
    }
  },
  created() {
    this.loadServices()
  },
  methods: {
    async loadServices() {
      this.services = await getServices();
    },
    UserLogout() {
      store.commit('auth/logout')
    }
  }
  }
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
