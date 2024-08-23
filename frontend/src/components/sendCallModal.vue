<template>
    <div class="modal fade window" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Заказать звонок</h5>
                </div>
                <div class="modal-body">
                    <form action="">
                        <label for="">Ваше имя</label>
                        <input type="text" id="name" placeholder="Введите ваше имя" class="form-control">
                        <p id="errName">Поле 'Имя' не должно содержать цифры и длиной больше 2 символов!</p>
                        <label for="">Ваш номер телефона</label>
                        <input type="text" id="phone" placeholder="+77777777777" maxlength="12" class="form-control">
                        <p id="errPhone">Поле 'Телефон' должно соответствовать шаблону: +7XXXXXXXXXX</p>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary btnClose" data-bs-dismiss="modal">Закрыть</button>
                    <button type="button" class="btn btn-primary" data-bs-target="#exampleModal" id="order"
                        @click="Call()">Заказать звонок</button>
                    <slot>
                        <h1>{{ сertificates }}</h1>
                    </slot>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { sendCall } from '@/api/sendCall';
export default {
    name: 'callModal',
    methods: {
        // Функция для валидации имени
        validateName(name) {
            let namePattern = /[0-9]/;
            if (namePattern.test(name) || name.length < 3) {
                return true;
            }
            return null; // Если имя прошло проверку
        },
        // Функция для валидации номера телефона
        validatePhone(phone) {
            let phonePattern = /\+7[0-9]{10}/;
            if (!phonePattern.test(phone) || phone.length < 12 || phone.includes(' ')) {
                return true;
            }
            return null; // Если телефон прошел проверку
        },
        // Функция для регистрации пользователя
        Call() {
            // Очистка меток ошибок перед каждой новой проверкой
            document.getElementById('errName').style.opacity = "0";
            document.getElementById('errPhone').style.opacity = "0";

            // Получение значений из полей формы и удаление лишних пробелов
            let name = document.getElementById("name").value.trim();
            let phone = document.getElementById("phone").value.trim();

            // Преобразование имени, если есть пробелы
            var newName = '';
            for (var i = 0; i < name.length; i++) {
                if (name.charAt(i) === " " && i + 1 < name.length) {
                    newName += name.charAt(i) + name.charAt(i + 1).toUpperCase();
                    i++;
                } else {
                    newName += name.charAt(i);
                }
            }
            name = newName;

            let errors = 0;

            // Валидация имени
            if (this.validateName(name)) {
                document.getElementById('errName').style.opacity = "1";
                errors++;
            }

            // Валидация телефона
            if (this.validatePhone(phone)) {
                document.getElementById('errPhone').style.opacity = "1";
                errors++;
            }

            // Если нет ошибок, сохраняем данные пользователя и очищаем поля формы
            if (errors == 0) {
                const userData = {
                    name: name.charAt(0).toUpperCase() + name.slice(1),
                    phone_number: phone
                };
                try {
                    sendCall(userData)
                }
                catch (error) {
                    console.error(error)
                }
                const modalBody = document.querySelector('.modal-body');
                modalBody.innerHTML = '<p>Мы перезвоним вам в течение часа.</p>';
                // Скрываем кнопку "Заказать звонок"
                const callButton = document.getElementById('order');
                callButton.style.display = 'none';
            }
        }
    }
}
</script>
<style scoped>
.modal-content {
    background-color: rgba(255, 255, 255, 0) !important;
    border: none !important;
}

.orderCall {
    display: flex;
    justify-content: center;
}

.orderCall button {
    margin: 16px 0;
    padding: 1rem 5rem;
}

.window .modal-content {
    background-color: rgba(255, 255, 255) !important;
}

#errName,
#errPhone {
    color: red;
    opacity: 0;
    font-size: 12px;
    margin: 0;
}
</style>