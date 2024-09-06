
const state = {
  authUser: {},
  isAuthenticated: false,
  jwt: localStorage.getItem('access'),
  endpoints: {
    obtainJWT: "http://127.0.0.1:8000/api/v1/users/auth/token/",
    refreshJWT: "http://127.0.0.1:8000/api/v1/users/auth/refresh_token/",
    baseUrl: "http://127.0.0.1:8000/api/v1/",
  },
}

const mutations = {
  setAuthUser(state, { authUser, isAuthenticated }) {
    state.authUser = authUser;
    state.isAuthenticated = isAuthenticated;
  },
  updateToken(state, access_token) {
    localStorage.setItem("access", access_token);
    state.jwt = access_token;
  },
  logout(state) {
    localStorage.removeItem("access");
    state.jwt = null;
    state.isAuthenticated = false;
    state.authUser = {}
  }
}
const getters = {
    isUserAuthenticated: state => state.isAuthenticated,
    isEmployee: state => state.authUser.is_employee,
}
export default {
  namespaced: true,
  state,
  mutations,
  getters,
}