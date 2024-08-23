import axiosInstance from '@/axios';
export async function getEmployees() {
    const url = `/employees/`;
        try{
          const employees = await axiosInstance.get(url)
          
          return employees.data
        }
        catch (error) {
          console.error('Error loading employees:', error);
          return 
        }
}