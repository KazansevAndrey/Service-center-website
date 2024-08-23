<template>
    <div class="container">
        <p class="breadcrumbs"><a href="/" class="interpreter">Главная</a> > Статус ремонта</p>

        <h1 class="heading"> Мои заявки</h1>

        <div v-if="applications.length!=0" class="applications-list">
            <div class="application-item menu" v-for="application in applications" :key="application.id">
                <div class="application-parameter">
                    <i class="fas fa-calendar-alt"></i>
                    <span class="application-text">Дата создания:</span>
                    <span class="application-value">{{application.time_create}}</span>
                </div>
                <div class="application-parameter">
                    <i class="fas fa-desktop"></i>
                    <span class="application-text">Устройство:</span>
                    <span class="application-value">{{application.device_title}}</span>
                </div>
                <div class="application-parameter">
                    <i class="fas fa-tasks"></i>
                    <span class="application-text">Статус:</span>
                    <span class="application-value">{{application.status}}</span>
                </div>
                <div class="application-parameter">
                    <i class="fas fa-calendar-check"></i>
                    <span class="application-text">Дата обновления:</span>
                    <span class="application-value">{{application.time_update}}</span>
                </div>
            </div>
        </div>
        <div class='no-applications-container' v-else>
            <div class="no-applications-text">Нет текущих заявок. <a href="/make-an-appointment">Вызвать мастера</a></div> 
        </div>
        
        
    </div>
    
    <div class="orderCall">
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            Заказать звонок
        </button>
    </div>
    <call-modal>
    </call-modal>
</template>

<script>
import callModal from '@/components/sendCallModal.vue';
import {get_client_applications} from '@/api/applications'
export default {
    name: 'repairStatusView',
    components: {
        callModal,
    },
    data(){
        return {
            applications: [],
        }
    },
    methods:{
        async getApplications(){
            const applications = await get_client_applications()
            console.log(applications)
            return applications
        }
    },
    async created(){
        this.applications = await this.getApplications()
    }

}
</script>
<style scoped>
.interpreter,
.breadcrumbs {
    color: rgb(127, 127, 127);
    text-decoration: none;
}

.interpreter:hover {
    text-decoration: underline;
}
.heading{
    margin:16px;
}
.applications-list{
    margin-top: 50px;
    min-height: 50vh;
}
.application-item {
    justify-content: space-between;
    display: flex;
    flex-wrap: wrap;
    width: 100%;
    margin-bottom: 5px;
    background-color: #2c3038;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border: 1px solid #3a3f47;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.application-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
}

.application-parameter {
    margin-bottom: 10px;
    display: flex;
    flex: 1; 
    margin-right: 10px;
}

.application-text {
    margin-right: 10px;
    color: #e9ecef;
    font-weight: 600;
}

.application-value {
    color: #adb5bd;
    font-weight: 400;
}

.application-parameter i {
    color: #61dafb;
    margin-right: 5px;
}
.orderCall {
  display: flex;
  justify-content: center;
}

.orderCall button {
  margin: 16px 0;
  padding: 1rem 5rem;
}
.no-applications-container{
    min-height: 50vh;

}
.no-applications-text{
    font-size: large;
}
@media (max-width: 540px) {
    .application-item {
    flex-direction: column;
}
}
@media (max-width: 580px) {
    .application-item {
    flex-direction: column;
}
}
</style>