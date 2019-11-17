

const initialState = { sampleList: [] }

export default function toggleSample(state = initialState, action) {
    console.log('reducer', state)
    let nextState
    switch (action.type) {
        case 'ADD_SAMPLE':
            nextState = {
                ...state,
                sampleList: [...state.sampleList, action.value]
            }
            return nextState || state
        default:
            return state
    }
}