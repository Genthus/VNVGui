<template>
<div class="w-full h-80 bg-slate-100">
    <div class="max-w-sm shadow-md mt-3 rounded-lg p-6 m-auto bg-slate-400 ">
        <span class="mb-2 text-lg font-bold tracking-tight text-white">Scenes</span>
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
import {useRouter} from 'vue-router'

const router = useRouter()

const scenes = ref(0)

function changeScene(sceneId) {
    router.push('/sceneEditor/'+sceneId)
}

function loadProject() {
    fetch("http://localhost:5000/testProject").then(response => {
        if (!response.ok) {
            throw new Error("Request failed")
        }
        return response.json()
    })
    .then(data => {
        scenes.value = data.scenes
    })
    .catch(error => console.log(error))
}

onMounted(() => {
    loadProject()
})
</script>