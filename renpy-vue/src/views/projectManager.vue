<template>
<div class="w-full h-80 bg-slate-100">
    <div class="max-w-sm shadow-md mt-3 rounded-lg p-6 m-auto bg-slate-400">
        <span class="mb-2 text-lg font-bold tracking-tight text-white">Projects</span>
        <div class="flex flex-wrap flex-col justify-center p-2 items-center">
            <ul class="projects" :key="project.id" v-for="project in projects">
              <button class="bg-white rounded-lg w-64 p-3 mt-4 text-lg font-medium" @click="setProject(project.id)">{{project.name}}</button>
            </ul>
        </div>
    </div>
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