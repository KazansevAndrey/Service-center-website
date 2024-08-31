<template>
    <div class="application-card">
        <h2 class="application-number">Заявка №{{ application.id }}</h2>
        <div class="application-details">
            <p><strong>Имя:</strong> {{ application.user_first_name }}</p>
            <p><strong>Фамилия:</strong> {{ application.user_last_name }}</p>
            <p><strong>Email:</strong> {{ application.user_email }}</p>
            <p><strong>Номер телефона:</strong> {{ application.user_phone_number }}</p>
            <p><strong>Статус:</strong> {{ application.status }}</p>

            <p><strong>Устройство:</strong> {{ application.device_title }}</p>
            <p><strong>Описание:</strong> {{ application.description }}</p>
            <p><strong>Дата создания:</strong> {{ application.time_create }}</p>

        </div>
        <div class="application-actions">
            <button @click="deleteApplication(application.id)" class="delete-button">Удалить заявку</button>

            <div class="status-change">
                <label for="status-select">Изменить статус:</label>
                <select id="status-select" v-model="selectedStatus" @change="changeStatus(application.id)">
                    <option value="" disabled>Выберите статус</option>
                    <option v-for="status in statuses" :key="status.value" :value="status.value">
                        {{ status.label }}
                    </option>
                </select>
            </div>
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
                { value: "pending", label: "В ожидании" },
                { value: "in_progress", label: "В процессе" },
                { value: "completed", label: "Завершена" },
                { value: "cancelled", label: "Отменена" },
            ],
        };
    },
    methods: {
        async getApplication(application_id){
            this.application = await get_application(application_id)
            console.log(this.application)
        }
    },
    created(){
        this.getApplication(this.application_id)
    }
}

</script>

<style scoped>
.application-card {
    border: 1px solid #ddd;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 5px;
    background-color: #f9f9f9;
}

.application-number {
    margin-bottom: 10px;
    font-size: 18px;
    color: #333;
}

.application-details p {
    margin: 5px 0;
}

.application-actions {
    margin-top: 15px;
    display: flex;
    align-items: center;
    gap: 20px;
}

.delete-button {
    background-color: #e74c3c;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 5px;
}

.status-change {
    display: flex;
    flex-direction: column;
}

#status-select {
    padding: 5px;
}
</style>