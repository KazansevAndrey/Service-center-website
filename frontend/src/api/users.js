
import axios from 'axios';
import store from '@/stores';
import axiosInstance from '@/axios';
export default async function Registration(inputs, $store, $router) {
    const url = `${store.state.backendUrl}/users/registration`;
    try {
        await axios.post(url, inputs)
        //Аутентефицируем пользователя
        const email = inputs.email
        const password = inputs.password
        const data =  { email, password }
        await Login(data, $store, $router)
    }
    catch (error) {
        console.log('Registration error', error.response.data);
        throw error; // выбрасывание ошибки для обработки в месте вызова
    }
}

export async function Login(data, $store, $router, employeeLogin=false) {
    //Аутентефицируем пользователя
    try {
        const response = await axios.post($store.state.auth.endpoints.obtainJWT, data)
  
        const access = response.data.access
        const refresh = response.data.refresh
        const tokens = {access, refresh}
        $store.commit("auth/updateToken", tokens);
        const userResponse = await axiosInstance.get(`/users/current_user`)
        //Логиним сотрудника
        if (employeeLogin == true){
            if (userResponse.data.is_employee !== true){
                console.log('Не сотрудник')
                return false
                }
            }
        $store.commit("auth/setAuthUser", {
            authUser: userResponse.data,
            isAuthenticated: true,
        })
        const redirectTo = $router.currentRoute.value.query.redirect || '/'
        
        $router.push(redirectTo);
        return true
    }
    catch (error) {
        console.log('Login error', error.response?.data || error.message || error)
        return false
    }
} 


