
import { createStore } from 'vuex'
import auth from './modules/auth'
import applications from './modules/applications'

const store =  createStore({
    modules:{
        auth,
        applications,
    },
    state: {
        backendUrl: "http://127.0.0.1:8000/api/v1"
    },
    mutations: {},
    actions: {},
    getters: {
        getServer: state => {
            return state.backendUrl
        }
    }
})
export default store