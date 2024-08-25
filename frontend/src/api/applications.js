
import axiosInstance from '@/axios';
export async function get_device_types() {
    const url = `/applications/device-types-list`;
        try{
            const devices = await axiosInstance.get(url)
            return await devices.data
        }
        catch (error) {
          console.error('Error loading device types:', error);
          return 
        }
}

export async function send_application(data) {
    const url = `/applications/client-applications/`;
        try{
        await axiosInstance.post(url, data)
        return true
        }
        catch (error) {
          console.error('Error send applications:', error);
          throw error
        }
}

export async function get_client_applications(){
    const url = 'applications/client-applications/';
    try{
      const response = await axiosInstance.get(url)
      return response.data
    }
    catch (error) {
      console.log('Error loading client applications')
      throw error
    }
}

// Текущие , входящие, заявки на звонки. 3 эндпоинта из EmployyePageApplication
export async function get_all_applications_from_clients(apiEndpoint){
  const url = apiEndpoint
  try{
    const response = await axiosInstance.get(url)
    return response.data
  }
  catch (error) {
    console.log('Error loading all applications')
    throw error
  }

}
