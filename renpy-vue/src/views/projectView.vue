<template>
<div class="projectView">
    <ul class="scenes" :key="scene.id" v-for="scene in scenes">
      <button @click="changeScene(scene.id)">{{scene.name}}</button>
    </ul>
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

<style scoped>
.projectView {
    position: absolute;
    width: 100%;
    height: 95%;
    top:5%;
    left:0%;
    background: #121212;
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