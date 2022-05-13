<template>
    <div> 
        <button @click="getNumber">Get number</button>
        <h3>{{ count }}</h3>
    </div>
</template>

<script>
export default {
    name: 'simpleTest',
    data() {
        return {
            count: 0
        }
    },
    methods: {
        getNumber() {
            fetch("http://localhost:5000/number").then(response => {
                if (!response.ok) {
                    throw new Error("Request failed")
                }
                return response.json()
            })
            .then(data => {
                console.log(data.count)
                console.log(data.number)
                this.count = data.number
            })
            .catch(error => console.log(error))
        }
    }
}
</script>
