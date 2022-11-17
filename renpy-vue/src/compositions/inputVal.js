export async function Validate(state, conditionArray) {
    let errors = []
    let errorId = 0
    Object.keys(state).forEach(function(s) {
        if (Object.keys(conditionArray).includes(s)) {
            if ('alphaNum' in conditionArray[s]) {
                let pattern = /^[a-z0-9]+$/i
                if (!pattern.test(state[s])) {
                    errors.push({
                        id: errorId++,
                        message: 'Only alphanumeric characters allowed'
                    })
                }
            }
            if ('min' in conditionArray[s]) {
                if (conditionArray[s].min > state[s].length) {
                    errors.push({
                        id: errorId++,
                        message: "Must have at least " + conditionArray[s].min + " characters"
                    })
                }
            }
            if ('max' in conditionArray[s]) {
                if (conditionArray[s].max <= state[s].length) {
                    errors.push({
                        id: errorId++,
                        message: "Must at most " + conditionArray[s].min + " characters"
                    })
                }
            }
            if ('required' in conditionArray[s]) {
                if (state[s].length == 0) {
                    errors.push({
                        id: errorId++,
                        message: "Input required"
                    })
                }
            }
        }
        else {
            errors.push({
                id: errorId++,
                message: 'object not found in rules'
            })
        }
    })
    console.log(errors)
    return errors;
}