<template>
    <div class="container">
        <p class="breadcrumbs"><a href="/" class="interpreter">Главная</a> > Вызов мастера</p>

        <!-- Форма регистрации -->
        <h1 class="heading">Вызов мастера</h1>
        <form action="">

            <div>

                <div class="phoneDiv">
                    <p>Сломанная техника:</p>
                    <select name="technic" id="technic" class="form-select">
                        <option value="0" disabled selected hidden>Выберите технику</option>
                        <option v-for="device in deviceTypes" :key="device.id" :value="device.id">{{ device.device_type
                            }}
                        </option>
                    </select>
                    <p id="errTechnic">Выберите технику</p>
                </div>

                <div class="problemDiv">
                    <p>Опишите проблему</p>
                    <textarea name="problem" class="form-control" id="problem" rows="4"
                        placeholder="Введите проблему"></textarea>
                    <p id="errProblem">Введите описание проблемы</p>
                </div>


                <div class="buttonDiv">
                    <input type="button" class="btn btn-primary" @click="Request()" value="Оставить заявку">
                </div>

            </div>
        </form>

        <!-- Modal -->
        <div class="modal fade window" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel"
            aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Заказать звонок</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <p>Ваша заявка успешно принята. Мы свяжемся с вами в ближайшее время.</p>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                            @click="Сleansing()">Закрыть</button>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import { Modal } from 'bootstrap';
import { get_device_types, send_application } from '@/api/applications'
export default {
    name: "AppointmentView",
    data() {
        return {
            deviceTypes: []
        }

    },
    methods: {
        async loadDevices() {
            this.deviceTypes = await get_device_types()

        },
        // Функция для заявкии пользователя
        async Request() {

            // Ссылки на метки для отображения ошибок
            const labelErrTechnic = document.getElementById("errTechnic");
            const labelErrProblem = document.getElementById("errProblem");
            // Очистка меток ошибок перед каждой новой проверкой
            labelErrProblem.style.opacity = "0";
            labelErrTechnic.style.opacity = "0";

            // Получение значений из полей формы и удаление лишних пробелов
            let technic = document.getElementById("technic").value;
            let problem = document.getElementById("problem").value.trim();

            let errors = 0;

            // Валидация выбора техники
            if (technic == 0) {
                labelErrTechnic.style.opacity = "1";
                errors++;
            }

            // Валидация описания проблемы
            if (!problem) {
                labelErrProblem.style.opacity = "1";
                errors++;
            }

            // Если нет ошибок, сохраняем данные пользователя и очищаем поля формы
            if (errors == 0) {
                const data = { device: technic, description: problem }
                await send_application(data)
                labelErrProblem.style.opacity = "0";
                labelErrTechnic.style.opacity = "0";
                var modalElement = document.getElementById('exampleModal');
                var modal = new Modal(modalElement);
                modal.show();
            }},
            Сleansing() {
                document.getElementById("problem").value = "";
                document.getElementById("technic").selectedIndex = 0;
                this.$router.push('/repair-status')
            },
        },
        created() {
            this.loadDevices()
            console.log(this.deviceTypes)
        }


    }

</script>

<style scoped>
form{
    height: 50vh;
}
.interpreter,
.breadcrumbs {
    color: rgb(127, 127, 127);
    text-decoration: none;
    padding-top: 30px;
}

.interpreter:hover {
    text-decoration: underline;
}

.heading {
    margin: 16px 0;
}

form {
    align-items: center;
    display: flex;
    justify-content: center;
}

.buttonDiv {
    align-items: center;
    display: flex;
    justify-content: center;
}

form p {
    margin: 0;
}

form>div {
    border: 1px solid #0d6efd;
    border-radius: .25rem;
    padding: 16px;
    align-items: center;
}

select {
    margin: 0 !important;
}

select,
textarea {
    width: 100%;
}

.checkboxDiv {
    display: flex;
    align-items: baseline;
}

.checkboxDiv input {
    margin-right: 4px;
    accent-color: #0d6efd;
}

.checkboxDiv a {
    color: rgb(127, 127, 127);
}

#errName,
#errPhone,
#errTechnic,
#errProblem,
#errAgreement {
    color: red;
    margin-bottom: 0;
    margin-bottom: 4px;
    opacity: 0;
}
</style>