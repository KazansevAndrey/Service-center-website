<template>
    <div class="application-item menu" v-for="application in applications" :key="application.id">
        <div class="application-parameter">
            <i class="fas fa-user"></i>
            <span class="application-text">Имя:</span>
            <span class="application-value">{{application.name}}</span>
        </div>
        <div class="application-parameter">
            <i class="fas fa-solid fa-phone"></i>
            <span class="application-text">Номер телефона:</span>
            <span class="application-value">{{application.phone_number}}</span>
        </div>
        <div class="application-parameter">
            <i class="fas fa-calendar-alt"></i>
            <span class="application-text">Дата создания:</span>
            <span class="application-value">{{ application.time_create }}</span>
        </div>

    </div>
</template>
<script>

export default {
    name: 'callApplications',
    props: {
        apiEndpoint:{
            type:String,
            required: true
        },
        category_name:{
            type: String,
            required: true
        },
        applications: {
            type: Array,
            required: true
        }
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
    flex: 1 1 1;
    margin-right: 10px;
    min-width: 32%; 
    flex-wrap: wrap;
    justify-content: start;


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