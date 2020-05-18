import {
    set
} from "@/utils/actions"

export const state = () => {
    return {
        api: {
            text: '/api'
        },
        dataRes: {},
        listWord: []
    }
}

export const mutations = {
    SET_TEXT_INPUT: set('dataRes'),
}

export const actions = {
    async PostText({ state, commit }, docs) {
        const { text } = state.api
        const res = { isSuccess: false }
        try {

            const data = await this.$axios.$post(`${text}/home`, docs)
            console.log("data", data)
            res.isSuccess = true
            commit('SET_TEXT_INPUT', data)
        }
        catch (err) {
            console.log("PostText", err)
        }
        return res

    }
}