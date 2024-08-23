import axiosInstance from '@/axios';
export async function getCategoryInfo(category_id) {
    const url = `/services/services-category-list/${category_id}`;    
    return await axiosInstance.get(url)
        .then(response => {
            return response.data; 
        })
        .catch(error => {
            console.error('Error fetching service:', error);
            throw error; 
        });
}
export async function getPopularServicesByCategory(category_id) {
    const url = `/services/popular-services-by-category-list/${category_id}`;    
    return await axiosInstance.get(url)
        .then(response => {
            return response.data; 
        })
        .catch(error => {
            console.error('Error fetching popular service:', error);
            throw error; 
        });
}

export async function getAnotherServicesByCategory(category_id) {
    const url = `/services/another-services-by-category-list/${category_id}`;    
    return await axiosInstance.get(url)
        .then(response => {
            return response.data; 
        })
        .catch(error => {
            console.error('Error fetching popular service:', error);
            throw error; 
        });
}