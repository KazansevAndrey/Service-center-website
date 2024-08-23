
import axiosInstance from '@/axios';
export async function getServices() {
    const url = `/services/services-category-list/`;    
    return axiosInstance.get(url)
        .then(response => {
            return response.data; // response.data содержит тело ответа в формате JSON
        })
        .catch(error => {
            console.error('Error fetching services:', error);
            throw error; // выбрасывание ошибки для обработки в месте вызова
        });
}
