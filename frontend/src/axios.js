import axios from 'axios';
import store from './stores';

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/v1/',  
  headers: {
    'Content-Type': 'application/json',          
  },
  withCredentials: true,  // Если сервер требует отправки cookies
});

// Интерсептор запросов для добавления токена
axiosInstance.interceptors.request.use(
  (config) => {
    const access_token = localStorage.getItem('access');  
    if (access_token) {
      config.headers.Authorization = `Bearer ${access_token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Функция для получения текущего пользователя
const getCurrentUser = async () => {
  try {
    const userResponse = await axiosInstance.get("/users/current_user");
    store.commit("auth/setAuthUser", {
      authUser: userResponse.data,
      isAuthenticated: true,
    });
    
  } catch (error) {
    console.error("Failed to fetch current user", error);
    throw error;
  }
};

axiosInstance.interceptors.response.use(
  (response) => response,
  async (err) => {
    const originalConfig = err.config;

    if (err.response !== undefined && err.response.status === 401 && !originalConfig._retry) {
      originalConfig._retry = true;
      try {
        const response = await axiosInstance.post("/token/refresh/", {
          refresh: localStorage.getItem('refresh'),
        });
        const { access, refresh } = response.data;
        const tokens = { access, refresh };

        store.commit("auth/updateToken", tokens);
        localStorage.setItem('access', access);
        localStorage.setItem('refresh', refresh);

        await getCurrentUser(); // Получение текущего пользователя после обновления токена

        return axiosInstance(originalConfig); // Повторный запрос
      } catch (err) {
        store.commit("auth/logout");
        return true;
      }
    }
    return Promise.reject(err);
  }
);

// Получение текущего пользователя при загрузке страницы, если токен существует
const initializeAuth = async () => {
  const access_token = localStorage.getItem('access');
  if (access_token) {
    await getCurrentUser();
  }
};

await initializeAuth();

export default axiosInstance;