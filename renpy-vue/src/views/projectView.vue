<template>
<div class="projectView">
    <h1>{{name}}</h1>
    <ul class="scenes" :key="scene.id" v-for="scene in scenes">
      <button @click="changeScene(scene.id)">{{scene.name}}</button>
    </ul>
</div>
</template>

<script setup>
import {ref,onMounted} from 'vue'
import {useRouter, useRoute} from 'vue-router'

const router = useRouter()
const route = useRoute()

const emit = defineEmits([
    'projectLoaded'
])

const scenes = ref(0)
const name = ref('')

function changeScene(id) {
    router.push({name: 'sceneEditor', params: {projectId: route.params.projectId, sceneId: id}})
}

function loadProject(projectId) {
    fetch("http://localhost:5000/project?id=" + projectId).then(response => {
        if (!response.ok) {
            throw new Error("Request failed")
        }
        return response.json()
    })
    .then(data => {
        scenes.value = data.scenes
        name.value = data.projectName
        emit('projectLoaded')
    })
    .catch(error => console.log(error))
}

onMounted(() => {
    loadProject(route.params.projectId)
})
</script>

<style scoped>
.projectView {
    position: absolute;
    width: 100%;
    height: 95%;
    top:60px;
    left:0%;
    background: #121212;
}

h1 {
    color: aliceblue;
}
.scenes {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
}

button {
    width: 10%;
    padding: 1% 0%;
}
</style>