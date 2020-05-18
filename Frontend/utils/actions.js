export const set = (key, defaultValue) => (state, value) => {
    (state[key] = value || defaultValue)
}
