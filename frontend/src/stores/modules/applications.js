const state = {
    currentApplicationsCount: 0,
    incomingApplicationsCount: 0,
    callApplicationsCount: 0
}
const mutations = {
    async setApplicationsCount(state, { category, count }) {
        if (category === 'currentRepairApplications') {
            console.log(category, count, 'Запись count в состояние')

            state.currentApplicationsCount = count
        }
        if (category === 'incomingRepairApplications'){
            console.log()
            state.incomingApplicationsCount = count
        }
        if (category === 'callApplications'){
            state.callApplicationsCount = count
        }
    }
}
const getters = {
    currentRepairApplicationsCount: state => state.currentApplicationsCount,
    incomingRepairApplicationsCount: state => state.incomingApplicationsCount,
    callApplicationsCount: state => state.callApplicationsCount
}

const actions = {
    async setCategoryCount(context, { category_name, count }) {
        await context.commit("setApplicationsCount", { category: category_name, count: count })

    }
}
export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions,
}