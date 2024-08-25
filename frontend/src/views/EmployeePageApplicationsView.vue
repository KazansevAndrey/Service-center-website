<template>
    <div class="main-container">
        <h1 class="heading">Текущие заявки на ремонт</h1>
        <div class="container">
            <div class="category-container">
                <p class="menu-title">Меню</p>
                <div @click=selectCategory(category) class="category-item" v-for="category in categories" :key=category.id>
                    <i class="{{ category.icon }}"></i>
                    <span class="category-title">{{category.name}}</span>
                    <span class="category-count">{{category.count}}</span>
                </div>
            </div>
            <div class='items-container'>
                <div class="applications-list">
                    <component :is="selectedComplonent" :apiEndpoint='apiEndpoint'></component>  
                </div> 
            </div>
        </div>
    </div>
</template>

<script>
import callApplications from '@/components/callApplications.vue'
import repairApplications from '@/components/repairApplications.vue'
export default {
    name: 'EmployeePageApplicationsView',
    data() {
        return {
            categories: {
                incomingRepairApplications: {
                    id: 1,
                    name: 'Заявки на ремонт',
                    component: repairApplications,
                    icon: 'fa fa-bell icon',
                    count: 123,
                    endpoint: 'incoming-repair-applications'
                },
                currentRepairApplications: {
                    id: 2,
                    name: 'В процессе выполнения',
                    component: repairApplications,
                    icon: 'fa fa-laptop icon',
                    count: 123,
                    endpoint: 'current-repair-applications'
                },
                callApplications: {
                    id: 3,
                    name: 'Заявки на звонки',
                    component: callApplications,
                    icon: 'fa fa-laptop icon',
                    count: 123,
                    endpoint: 'call-applications'

                }
            },
            selectedComplonent : repairApplications,
            apiEndpoint: 'incoming-repair-applications'
        }
    },
    methods: {
        selectCategory(category){
            this.selectedComplonent = category.component
            this.apiEndpoint = category.apiEndpoint
        }
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
    margin-bottom: 20px;

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

@media(max-width:575px) {
    .container {
        flex-direction: column
    }
}
</style>