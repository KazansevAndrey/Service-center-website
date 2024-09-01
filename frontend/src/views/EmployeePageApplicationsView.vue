<template>
    <div class="main-container">
        <h1 class="heading">Личный кабинет сотрудника</h1>
        <div class="container">
            <div class="category-container">
                <p class="menu-title">Меню</p>
                <div @click="selectCategory(category)" class="category-item" v-for="category in categories"
                    :key="category.id"
                    :style="{ backgroundColor: category.categoryName === categoryName ? '#c8c8c8' : '' }">
                    <i :class="category.icon"></i>
                    <span class="category-title">{{ category.name }}</span>
                    <span class="category-count">{{ category.count }}</span>
                </div>
            </div>
            <div class="items-container">
                <div class="applications-list">
                    <component :is="selectedComponent" :api-endpoint="apiEndpoint" :category_name="categoryName"
                        :applications="categoryApplications">
                    </component>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { markRaw } from 'vue';
import { get_all_applications_from_clients } from '@/api/applications'
import callApplications from '@/components/callApplications.vue';
import repairApplications from '@/components/repairApplications.vue';

export default {
    name: 'EmployeePageApplicationsView',
    data() {
        return {
            categories: {
                personalRepairApplications: {
                    id: 1,
                    name: 'Выполняются мной',
                    component: markRaw(repairApplications),
                    icon: 'fa fa-user icon',
                    count: 0,
                    endpoint: 'applications/personal-repair-applications',
                    categoryName: 'personalRepairApplications',
                    applications: ''
                },
                incomingRepairApplications: {
                    id: 2,
                    name: 'Входящие заявки',
                    component: markRaw(repairApplications),
                    icon: 'fa fa-bell icon',
                    count: 0,
                    endpoint: 'applications/incoming-repair-applications',
                    categoryName: 'incomingRepairApplications',
                    applications: ''
                },
                currentRepairApplications: {
                    id: 3,
                    name: 'В процессе работы',
                    component: markRaw(repairApplications),
                    icon: 'fa fa-laptop icon',
                    count: 0,
                    endpoint: 'applications/current-repair-applications',
                    categoryName: 'currentRepairApplications',
                    applications: ''
                },
                archivesApplications: {
                    id: 4,
                    name: 'Архивные заявки',
                    component: markRaw(repairApplications),
                    icon: 'fa fa-trash icon',
                    count: 0,
                    endpoint: 'applications/archive-repair-applications',
                    categoryName: 'archiveRepairApplications',
                    applications: ''
                },
                callApplications: {
                    id: 5,
                    name: 'Заявки на звонки',
                    component: markRaw(callApplications),
                    icon: 'fa fa-phone icon',
                    count: 0,
                    endpoint: 'call_requests/',
                    categoryName: 'callApplications',
                    applications: ''
                }
            },
            selectedComponent: markRaw(repairApplications),
            apiEndpoint: 'applications/personal-repair-applications',
            categoryName: "personalRepairApplications",
            categoryApplications: []
        };
    },
    methods: {
        selectCategory(category) {
            this.selectedComponent = category.component;
            this.categoryApplications = category.applications
            this.categoryName = category.categoryName
        },

        async getApplicationsByCategory(apiEndpoint) {
            const applications = await get_all_applications_from_clients(apiEndpoint);
            return applications
        },

        async getAllApplications() {
            // Проходим по всем категориям и обновляем count
            for (let key in this.categories) {
                let category = this.categories[key];
                let categoryApplications = await this.getApplicationsByCategory(category.endpoint)
                // Устанавливаем заявки для категории 
                this.categories[key].applications = categoryApplications
                this.categories[key].count = categoryApplications.length
            }
            this.categoryApplications = this.categories.personalRepairApplications.applications
        }
    },
    created() {
        this.getAllApplications()
    }
}
</script>


<style scoped>
.container {
    display: flex;
    gap: 15px;
}

.main-container {
    max-width: 1300px;
    margin-right: auto;
    margin-left: auto;
    min-height: 70vh;
}

.heading {
    margin: 16px;
    margin-bottom: 40px;

}

.category-container {
    background-color: #212529;
    color: white;
    padding: 20px;
    padding-left: 10px;
    padding-right: 10px;
    display: flex;
    flex-direction: column;
    gap: 5px;
    max-height: 60vh;
    min-width: 25%;
    border-radius: 10px;
}

.category-item {
    background-color: white;
    color: black;
    padding: 7px;
    border-radius: 10px;
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    transition: background-color 0.3s ease, color 0.3s ease;
    width: auto;
}

.category-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    cursor: pointer;
}

.menu-title {
    color: white;
    font-size: 25px;
    margin-bottom: 10px;

}

.category-count {
    margin-left: 10px;
    padding: 5px;
    min-width: 40px;
    background-color: #cadfff;
    justify-content: center;
    text-align: center;
    border-radius: 10px;
}

.icon {
    margin-right: 10px;
    color: #0d6efd;
}

.category-title {
    flex-grow: 1;
}

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

.items-container {
    width: 100%;
}

@media(max-width:1200px) {
    .container {
        flex-direction: column
    }
}
</style>