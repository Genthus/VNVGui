<template>
    <div class="container h-80 shadow-md mt-3 rounded-lg p-6 m-auto bg-white">
        <VueFlow v-model="elements"/>
    </div>
</template>

<script setup>
    import { VueFlow } from '@braks/vue-flow'
    import { ref,onUpdated } from 'vue';

    const props = defineProps({
        jumps: Array,
        scenes: Array
    })

    const elements = ref([])

    onUpdated(() => {
        var i = 0;
        props.scenes.forEach(scene => {
            elements.value.push({id:String(i), label:scene.name, position: {x:250+50*i, y:50+50*i}});
            i++;
        })
        props.jumps.forEach(jump => {
            elements.value.push({id:String(i), source: String(props.scenes.findIndex(item => item.name === jump.source)), target: String(props.scenes.findIndex(item => item.name === jump.destination))})
            i++;
        })
        console.log(elements.value)
    })
</script>