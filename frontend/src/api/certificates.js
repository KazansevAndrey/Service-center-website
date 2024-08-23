import axiosInstance from '@/axios';
export async function get_certificates() {
    const url = `/certificates/`;
        try{
          const response = axiosInstance.get(url)
          const certificates = (await response).data.map(certificate => certificate.file)
          
          return certificates
        }
        catch (error) {
          console.error('Error loading images:', error);
          return 
        }
}