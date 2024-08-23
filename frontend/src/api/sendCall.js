import axiosInstance from '@/axios';
import store from '@/stores';
export async function sendCall(data) {
    const url = `/call_requests/`;
    const user = store.state.auth.authUser
    if (user) {
        data.user = user.id
    }
    console.log(data)
    try {
        await axiosInstance.post(url, data)
    }
    catch (error) {
        console.error('Error sending call request:', error);
        throw error; // выбрасывание ошибки для обработки в месте вызова
    }
}
