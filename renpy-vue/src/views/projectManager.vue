<template>
<div class="projectManager">
    <ul class="projects" :key="project.id" v-for="project in projects">
      <button @click="setProject(project.id)">{{project.name}}</button>
    </ul>
</div>
</template>

<script setup>
import {ref,onMounted} from 'vue'
import {useRouter} from 'vue-router'

const router = useRouter()

const projects = ref([])

function setProject(id) {
    router.push({name: 'projectView', params: {projectId: id}})
}

function getProjects() {
    fetch("http://localhost:5000/projects").then(response => {
        if (!response.ok) {
            throw new Error("Request failed")
        }
        return response.json()
    })
    .then(data => {
        projects.value = data.projects
    })
    .catch(error => console.log(error))
}

onMounted(() => {
    getProjects()
})
</script>

<style scoped>
.projectManager {
    position: absolute;
    width: 100%;
    height: 95%;
    top:60px;
    left:0%;
    background: #121212;
}

.projects {
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