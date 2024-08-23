<template>
    <div>
        <div class=" limiter">
            <div class="container-login100">
                <div class="wrap-login100">
                    <form class="login100-form validate-form">
                        <span class="login100-form-title p-b-43">
                            Регистрация
                        </span>

                        <div class="wrap-input100 validate-input" :data-validate="errors.email">
                            <input class="input100 has-val" type="text" id='email' name="email" readonly
                                onfocus="this.removeAttribute('readonly')" v-model="form.email">
                            <span class="focus-input100"></span>
                            <span class="label-input100">Email</span>
                        </div>

                        <div class="wrap-input100 validate-input" :data-validate="errors.first_name">
                            <input class="input100 has-val" type="text" id='first-name' name="first_name" readonly
                                onfocus="this.removeAttribute('readonly')" v-model="form.first_name">
                            <span class="focus-input100"></span>
                            <span class="label-input100">Имя</span>
                        </div>

                        <div class="wrap-input100 validate-input" :data-validate="errors.last_name">
                            <input class="input100 has-val" type="text" id='last-name' name="last_name" readonly
                                onfocus="this.removeAttribute('readonly')" v-model="form.last_name">
                            <span class="focus-input100"></span>
                            <span class="label-input100">Фамилия</span>
                        </div>

                        <div class="wrap-input100 validate-input" :data-validate="errors.phone_number">
                            <input class="input100 has-val" type="text" id='phone-number' name="phone_number" readonly
                                onfocus="this.removeAttribute('readonly')" v-model="form.phone_number">
                            <span class="focus-input100"></span>
                            <span class="label-input100">Номер телефона</span>
                        </div>

                        <div class="wrap-input100 validate-input" :data-validate="errors.password">
                            <input class="input100 has-val"  name="password" id="password"
                                v-model="form.password">
                            <span class="focus-input100"></span>
                            <span class="label-input100">Пароль</span>
                        </div>

                        <div class="wrap-input100 validate-input" :data-validate="errors.password2">
                            <input class="input100 has-val" type="password" name="password2" id="password2"
                                v-model="form.password2">
                            <span class="focus-input100"></span>
                            <span class="label-input100">Повторите пароль</span>
                        </div>

                        <div class="flex-sb-m w-full p-b-32">

                            <div>
                                <a href="/login" class="txt1">
                                    Уже есть аккаунт? Войти
                                </a>
                            </div>

                        </div>
                        <div class="container-login100-form-btn">
                            <button class="login100-form-btn">
                                Зарегестрироваться
                            </button>
                        </div>

                    </form>

                    <div class="login100-more">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
@import '../assets/css/login/login.css';
@import '../assets/css/login/login_util.css';

footer {
    margin-top: 0px !important;
}
</style>

<script>
import Registration from '../api/users'
export default {
    name: 'RegistrationView',
    data() {
        return {
            form: {
                'first_name': '',
                'last_name': '',
                'email': '',
                'password': '',
                'password2': '',
                'phone_number': '',
            },
            errors: {
                'first_name': '',
                'last_name': '',
                'email': '',
                'password': '',
                'password2': '',
                'phone_number': ''
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
            let check = true
            const { first_name, last_name, email, password, password2, phone_number } = this.form;
            if (first_name.length < 2 || first_name.length > 20 || !/^[а-яА-ЯёЁa-zA-Z]+$/.test(first_name)) {
                this.errors.first_name = 'Имя должно содержать от 2 до 20 символов и только буквы.';
                check = false
            }
            if (last_name.length < 2 || last_name.length > 20 || !/^[а-яА-ЯёЁa-zA-Z]+$/.test(last_name)) {
                this.errors.last_name = 'Фамилия должна содержать от 2 до 20 символов и только буквы.';
                check = false
            }
            if (!/^([a-zA-Z0-9_.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/.test(email)) {
                this.errors.email = 'Неверный формат электронной почты.';
                check = false
            }
            if (password.length < 10 || password.length > 100) {
                this.errors.password = 'Пароль должен содержать от 10 до 100 символов.';
                check = false
            }
            if (password2 != password) {
                this.errors.password2 = 'Пароли должны совпадать';
                check = false
            }
            const phone_pattern = /^((8|\+7)[- ]?)?(\(?\d{3}\)?[- ]?)?[\d\- ]{7,10}$/
            if (!phone_pattern.test(phone_number)) {
                this.errors.phone_number = 'Телефон должен быть в формате "+71234567890"';
                check = false
            }
            if (check == true) {
                return true;
            }
            else {
                return false
            }
        },
        async submit() {
            if (this.validate()) {
                const formData = {
                    first_name: this.form.first_name,
                    last_name: this.form.last_name,
                    phone_number: this.form.phone_number,
                    email: this.form.email,
                    password: this.form.password,
                };
                try {
                    console.log(formData)
                    await Registration(formData, this.$store, this.$router);
                    this.$router.push('/');
                } catch (error) {
                    if (error.response.data.email){
                        this.errors.email = "Пользователь с таким email уже существует"
                        const email_field = document.getElementById('email')
                        email_field.parentElement.classList.add('alert-validate')
                        return false
                    }
                    console.error('Error during registration:', error);
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
             if (!this.validate() || !this.submit()) {
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
