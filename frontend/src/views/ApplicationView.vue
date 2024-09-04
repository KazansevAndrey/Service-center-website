<template>
    <div class="container">
        <p class="breadcrumbs"><a href="/employee-page-applications" class="interpreter">Все заявки</a> > Заявка №{{
            application.id }}</p>
        <h2 class="application-number">Заявка №{{ application.id }}</h2>
        <div class="application-details">
            <p class='application-parameter'><strong>Имя:</strong> {{ application.user_first_name }}</p>
            <p class='application-parameter'><strong>Фамилия:</strong> {{ application.user_last_name }}</p>
            <p class='application-parameter'><strong>Email:</strong> {{ application.user_email }}</p>
            <p class='application-parameter'><strong>Номер телефона:</strong> {{ application.user_phone_number }}</p>
            <p class='application-parameter'><strong>Статус:</strong> {{ application.status_title }}</p>

            <p class='application-parameter'><strong>Устройство:</strong> {{ application.device_title }}</p>
            <p class='application-parameter'><strong>Описание:</strong> {{ application.description }}</p>
            <p class='application-parameter'><strong>Дата создания:</strong> {{ application.time_create }}</p>
        </div>

        <div class="application-actions" v-if = "application.employee_id == employee_id && application.is_archived == false">
            <div class="status-change">
                <label for="status-select">Изменить статус:</label>
                <select id="status-select" v-model="selectedStatus" @change="changeStatus($event, application_id)">
                    <option value="" disabled>Выберите статус</option>
                    <option v-for="status in statuses" :key="status" :value="status.value">
                        {{ status.label }}
                    </option>
                </select>
            </div>
            <button @click="showDeleteConfirmation()" class="delete-button">Удалить заявку</button>
        </div>

        <div id="deleteConfirmationModal" class="modal">
            <div class="modal-content">
                <p>Вы уверены, что хотите удалить эту заявку? Она попадет в список архивных заявок</p>
                <div class="modal-buttons">
                    <button @click="deleteApplication()">Удалить</button>
                <button @click="closeDeleteConfirmation()">Отмена</button>
                </div>
               
            </div>
        </div>

        <!-- Если заявка входящая -->
        <div class="application-actions" v-if = "category_name == 'incomingRepairApplications'">
            <button type="button" @click="showAcceptConfirmation()" class="accept-button btn btn-primary">Принять заявку</button>
        </div>

        <div id="acceptConfirmationModal" class="modal">
            <div class="modal-content">
                <p>Принять заявку?</p>
                <div class="modal-buttons">
                    <button class = 'accept-modal-button' @click="acceptApplication()">Принять</button>
                <button @click="closeAcceptConfirmation()">Отмена</button>
                </div>
            </div>
        </div>


    </div>
</template>

<script>
import { delete_application, get_application, set_status, set_employee_to_application } from '@/api/applications'
import store from '@/stores';
export default {
    name: "ApplicationCard",
    props: {
        application_id: String,
        category_name: String,
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
            employee_id: ''
        };
    },
    methods: {
        async getApplication() {
            this.application = await get_application(this.application_id)
            console.log(this.application)
        },
        async changeStatus(event) {
            const status = event.target.value
            await set_status(this.application_id, status)
            window.location.reload()
        },
        async deleteApplication(){
            await delete_application(this.application_id)
            this.closeDeleteConfirmation()
            
        },
        // Принятие заявки 
        async acceptApplication() {
            await set_employee_to_application(this.application_id, this.employee_id)
            window.location.href = '/employee-page-applications';
        },
        closeDeleteConfirmation() {
            document.getElementById('deleteConfirmationModal').style.display = 'none';
        },
        closeAcceptConfirmation() {
            document.getElementById('acceptConfirmationModal').style.display = 'none';
        },
        showDeleteConfirmation() {
            document.getElementById('deleteConfirmationModal').style.display = 'block';
        },
        showAcceptConfirmation() {
            document.getElementById('acceptConfirmationModal').style.display = 'block';
        },

        getEmployee(){
            const employee_id = store.state.auth.authUser.id
            return employee_id
        },

        
    },
    created() {
        this.getApplication(this.application_id)
        this.employee_id = this.getEmployee()
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
    padding-right: var(--bs-gutter-x, .75rem);
    padding-left: var(--bs-gutter-x, .75rem);
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
    align-items: end;
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

.accept-button{
   
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 5px;
    text-wrap: nowrap;
    margin-top:10px;
    
}
.status-change {
    display: flex;
    flex-direction: column;
}

#status-select {
    padding: 5px;
}
.modal {
    display: none; /* Скрыто по умолчанию */
    position: fixed; /* Окно фиксировано относительно экрана */
    z-index: 1000; /* Располагается поверх всех элементов */
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgb(0, 0, 0);
    background-color: rgba(0, 0, 0, 0.4);
    justify-content: center;
    align-items: center;
}

.modal-content {
    background-color: #fefefe;
    margin: 15% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
    max-width: 400px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    text-align: center;
    border-radius: 8px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.modal-content p {
    margin-bottom: 20px;
}

.modal-content button {
    padding: 7px 7px;
    margin: 5px;
    border: none;
    cursor: pointer;
    font-size: 16px;
    width: 50%;
    border-radius: 4px;
}

.modal-content button:first-of-type {
    background-color: #f44336;
    color: white;
}

.modal-content button:last-of-type {
    background-color: #212529 ;
    color: white;
}
.accept-modal-button{
    background-color: #0b5ed7  !important;
    color: white;
}
.modal-buttons{
    display: flex;
    gap:10px;
}
@media(max-width:333px) {
    .application-actions {
        flex-direction: column;
        align-items: start;
        gap: 10px;
    }
}
</style>