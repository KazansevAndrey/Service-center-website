<template>
    <div class="application-item menu">
        <div class="application-parameter">
            <i class="fas fa-user"></i>
            <span class="application-text">Пользователь:</span>
            <span class="application-value">User123</span>
        </div>
        <div class="application-parameter">
            <i class="fas fa-calendar-alt "></i>
            <span class="application-text">Дата создания:</span>
            <span class="application-value">10:10:2024</span>
        </div>
        <div class="application-parameter">
            <i class="fas fa-desktop"></i>
            <span class="application-text">Устройство:</span>
            <span class="application-value">Ноутбук</span>
        </div>
        <div class="application-parameter">
            <i class="fas fa-tasks"></i>
            <span class="application-text">Статус:</span>
            <span class="application-value">В процессе</span>
        </div>

    </div>
</template>
<script>
import get_all_applications_from_clients from '@/api/applications'
export default {
    name: 'repairApplications',
    props: {
        apiEndpoint:{
            type:String,
            required: true
        }
    },
    data() {
        return {
            Applications: []
        }
    },
    methods: {
        async getApplications() {
            this.Applications = await get_all_applications_from_clients(this.apiEndpoint)
        }
    },
    created(){
        this.getApplications()
    }
}
</script>

<style scoped>
.applications-list {
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
</style>