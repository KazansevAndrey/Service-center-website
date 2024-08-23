<template>
    <div class="employee-login-container">
        <form class="login100-form validate-form">
            <span class="login100-form-title p-b-43">
                Вход в личный кабинет сотрудника
            </span>
            <div class="wrap-input100 validate-input" :data-validate="errors.email">
                <input class="input100 has-val" type="text" id='email' name="email" readonly
                    onfocus="this.removeAttribute('readonly')" v-model="form.email">
                <span class="focus-input100"></span>
                <span class="label-input100">Email</span>
            </div>
            <div class="wrap-input100 validate-input" :data-validate="errors.password">
                <input class="input100 has-val" name="password" id="password" v-model="form.password">
                <span class="focus-input100"></span>
                <span class="label-input100">Пароль</span>
            </div>

            <div class="flex-sb-m w-full p-b-32">


            </div>
            <div class="container-login100-form-btn">
                <button class="login100-form-btn">
                    Войти
                </button>
            </div>

        </form>
    </div>
</template>
<script>
import { Login } from '../api/users'
export default {
    name: 'EmployeeLoginView',
    data() {
        return {
            form: {
                'email': '',
                'password': '',
            },
            errors: {
                'email': '',
                'password': '',
            },
        }
    },
    methods: {
        clearErrors() {
            for (const key in this.errors) {
                this.errors[key] = ''
            }
        },
        validate() {
            this.clearErrors()
            const email = this.form.email;
            const password = this.form.password
            let check = true
            if (!/^([a-zA-Z0-9_.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/.test(email)) {
                this.errors.email = 'Неверный формат электронной почты.';
                check = false
            }
            if (password === '') {
                this.errors.password = 'Введите пароль'
                check = false
            }
            if (check == false) {
                return false
            }
            return true
        },
        async submit() {
            if (this.validate()) {
                const formData = {
                    email: this.form.email,
                    password: this.form.password,
                };
                try {
                    if (await Login(formData, this.$store, this.$router, this.employeeLogin=true)) {
                        return true
                    }
                    const password_field = document.getElementById('password')
                    this.errors.password = 'Неправильный email или пароль'
                    password_field.parentElement.classList.add('alert-validate')

                } catch (error) {
                    console.log('Error during login:', error);
                }
            }
        },
    },
    mounted() {
        const inputs = document.querySelectorAll('.validate-form .input100');
        inputs.forEach(input => {
            input.addEventListener('focus', () => {
                input.parentElement.classList.remove('alert-validate');
            });
        });

        document.querySelector('.validate-form').addEventListener('submit', (event) => {
            event.preventDefault();
            if (this.validate()) {
                this.submit()
            } else {
                inputs.forEach(input => {
                    const field_name = input.getAttribute('name')
                    if (this.errors[field_name] != '') {
                        input.parentElement.classList.add('alert-validate');

                    }
                })
            }
        })
    }
}
</script>
<style scoped>
@import '../assets/css/login/login.css';
@import '../assets/css/login/login_util.css';

.login100-form{
    min-height: 70vh;

}

.employee-login-container{
    display: flex;
    justify-content: center;
    
}
footer {
    margin-top: 0px !important;
}
</style>