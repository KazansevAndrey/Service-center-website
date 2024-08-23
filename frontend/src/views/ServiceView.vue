<template>
    <div class="container">
        <p class="breadcrumbs"><a href="/" class="interpreter">Главная</a> > {{ category_info.category_name }}</p>

        <h1 class="heading">Профессиональный {{ category_info.category_name }} в ServiceCenter</h1>
        <p>{{ category_info.description }}</p>

        <h1 class="headingCenter">Почему выбирают нас</h1>
        <ul>
            <li>Профессиональные специалисты: Наши инженеры обладают богатым опытом и экспертизой в ремонте устройств
                различных марок и моделей.</li>
            <li>Использование качественных комплектующих: Мы используем только оригинальные и высококачественные
                запчасти для замены, что гарантирует долгосрочную работоспособность вашего устройства.</li>
            <li>Индивидуальный подход: Мы понимаем, что каждая проблема уникальна, поэтому мы предлагаем индивидуальный
                подход к каждому клиенту и его устройству.</li>
        </ul>

        <h1 class="headingCenter">Популярные услуги</h1>

        <table class="table table-bordered table-striped table-hover">
            <thead>
                <tr>
                    <th class="text-start align-middle">Наименование услуги</th>
                    <th class="text-start align-middle">Цена (в тенге)</th>
                    <th class="text-start align-middle">Гарантия</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="service in popular_services" :key="service.id">
                    <td>{{ service.name }}</td>
                    <td>От {{ service.price }}</td>
                    <td>{{ service.warranty_period }} дней</td>
                </tr>
            </tbody>
        </table>

        <div v-if="another_services.length > 0">
            <h1 class="headingCenter">Другие услуги</h1>
            <p>В дополнение к основным видам ремонта, наш сервисный центр также предоставляет следующие услуги:</p>
            <ul>
                <li v-for="service in another_services" :key="service.id">{{ service.name }}</li>
                <li>И так далее</li>
            </ul>
        </div>

        <div class="orderCall">
            <!-- Button trigger modal -->
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                Заказать звонок
            </button>
        </div>
       <callModal>
       </callModal>
    </div>
</template>

<script>
import { getCategoryInfo, getPopularServicesByCategory, getAnotherServicesByCategory } from '../api/services';
import callModal from '@/components/sendCallModal.vue';
export default {
    name: 'ServiceView',
    components: {
        callModal,
    },
    props: {
        category_id: String,
    },
    data() {
        return {
            popular_services: [],
            another_services: [],
            category_info: [],
        }
    },
    async created() {
        this.category_info = await getCategoryInfo(this.category_id)
        this.popular_services = await getPopularServicesByCategory(this.category_id)
        this.another_services = await getAnotherServicesByCategory(this.category_id)
    }
}
</script>

<style scoped>
.interpreter,
.breadcrumbs {
    color: rgb(127, 127, 127);
    text-decoration: none;
}




/* Тело сайта */
.interpreter,
.breadcrumbs {
    color: rgb(127, 127, 127);
    text-decoration: none;
}

.interpreter:hover {
    text-decoration: underline;
}

.heading,
.headingCenter {
    margin: 16px 0;
}

.headingCenter {
    display: flex;
    justify-content: center;
}

p {
    text-align: justify;
}

section li {
    list-style-image: url("../assets/images/marker.svg");
}

section ul {
    padding: 0;
    margin: 0;
}

section ol,
ul {
    padding-left: 1.5rem !important;
}

table {
    margin: 0;
}

#errName,
#errPhone {
    color: red;
    opacity: 0;
    font-size: 12px;
    margin: 0;
}

.orderCall {
    display: flex;
    justify-content: center;
}

.orderCall button {
    margin: 16px 0;
    padding: 1rem 5rem;
}


@media (min-width: 993px) {
    section {
        padding-top: 116px;
    }
}

@media (min-width: 992px) {

    .menu {
        width: 100%;
        position: fixed;
        z-index: 10;
    }

    .map {
        height: 500px;
        width: 500px;
    }

}

@media (max-width: 992px) {

    header {
        margin-bottom: 16px;
    }

    .interpreter {
        margin-top: 16px;
    }

    .dropdown-item {
        color: white !important;
    }

    .dropdown-menu {
        background-color: #0d6efd !important;
        border: none !important;
    }

    .menu {
        position: relative;
    }

    .map {
        height: 300px;
        width: 300px;
    }
}

@media (max-width: 768px) {

    .map {
        margin-bottom: 16px;
        width: 100%;
    }

    footer .container {
        flex-direction: column-reverse;
    }

    .btn {
        width: 100%;
    }
}
</style>
