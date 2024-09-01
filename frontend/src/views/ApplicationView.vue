<template>
    <div class="container">
        <p class="breadcrumbs"><a href="/employee-page-applications" class="interpreter">Все заявки</a> > Заявка №{{ application.id }}</p>
        <h2 class="application-number">Заявка №{{ application.id }}</h2>
        <div class="application-details">
            <p class='application-parameter'><strong>Имя:</strong> {{ application.user_first_name }}</p>
            <p class='application-parameter'><strong>Фамилия:</strong> {{ application.user_last_name }}</p>
            <p class='application-parameter'><strong>Email:</strong> {{ application.user_email }}</p>
            <p class='application-parameter'><strong>Номер телефона:</strong> {{ application.user_phone_number }}</p>
            <p class='application-parameter'><strong>Статус:</strong> {{ application.status }}</p>

            <p class='application-parameter'><strong>Устройство:</strong> {{ application.device_title }}</p>
            <p class='application-parameter'><strong>Описание:</strong> {{ application.description }}</p>
            <p class='application-parameter'><strong>Дата создания:</strong> {{ application.time_create }}</p>

        </div>
        <div class="application-actions">
            <div class="status-change">
                <label for="status-select">Изменить статус:</label>
                <select id="status-select" v-model="selectedStatus" @change="changeStatus($event, application_id)">
                    <option value="" disabled>Выберите статус</option>
                    <option v-for="status in statuses" :key="status" :value="status.value">
                        {{ status.label }}
                    </option>
                </select>
            </div>
            <button @click="deleteApplication(application.id)" class="delete-button">Удалить заявку</button>

        </div>
    </div>
</template>

<script>
import {get_application} from '@/api/applications'
export default {
    name: "ApplicationCard",
    props: {
        application_id: String,
    },
    data() {
        return {
        application: [],
        selectedStatus: "",
            statuses: [
                { value: "C", label: "На рассмотрении" },
                { value: "P", label: "В процессе работы" },
                { value: "D", label: "Завершена" },
            ],
        };
    },
    methods: {
        async getApplication(application_id){
            this.application = await get_application(application_id)
            console.log(this.application)
        }
        changeStatus(application_id)
    },
    created(){
        this.getApplication(this.application_id)
    }
}

</script>

<style scoped>

.interpreter,
.breadcrumbs {
    color: rgb(127, 127, 127);
    text-decoration: none;
    padding-top: 30px;

}

.container {
    width: 100%;
    padding-right: var(--bs-gutter-x,.75rem);
    padding-left: var(--bs-gutter-x,.75rem);
    margin-right: auto;
    margin-left: auto;   
    padding-bottom: 40px;
}

.application-number {
    margin-bottom: 10px;
    font-size: 25px;
    color: #333;
}

.application-details p {
    margin: 15px 0;
    font-size: 18px;
}

.application-actions {
    margin-top: 15px;
    display: flex;
    align-items:end;
    gap: 20px;
}

.delete-button {
    background-color: #e74c3c;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 5px;
    text-wrap: nowrap;
}

.status-change {
    display: flex;
    flex-direction: column;
}

#status-select {
    padding: 5px;
}

@media(max-width:333px){
    .application-actions{
        flex-direction: column;
        align-items:start;
        gap:10px;
    }
}
</style>