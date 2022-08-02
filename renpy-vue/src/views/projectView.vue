<template>
<div class="w-full">
    <div class="container shadow-md mt-3 rounded-lg p-6 m-auto bg-slate-400 ">
        <span class="mb-2 text-lg font-bold tracking-tight text-white">{{name}}</span>
        <div class="flex flex-wrap flex-col justify-center p-2 items-center">
            <ul :key="scene.id" v-for="scene in scenes">
              <button class="bg-white rounded-lg w-64 p-3 mt-4 text-lg font-medium" @click="changeScene(scene.id)">{{scene.name}}</button>
            </ul>
        </div>
    </div>
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
