<template>
<div class="w-full">
    <div class="container shadow-md mt-3 rounded-lg p-6 m-auto bg-purple-400">
        <span class="mb-2 text-lg font-bold tracking-tight text-white">Projects</span>
        <div class="flex flex-wrap flex-col justify-center p-2 items-center">
            <ul class="projects" :key="project.id" v-for="project in projects">
              <button class="bg-white rounded-lg w-64 p-3 mt-4 text-lg font-medium" @click="setProject(project.id)">{{project.name}}</button>
            </ul>
            <div class="relative">
                <button class="bg-blue-700 text-white rounded-lg w-64 p-3 mt-4 text-lg font-medium" @click="newProjectOpen = true">New Project</button>
                <teleport to="body">
                    <div class="absolute bg-purple-500 bg-opacity-20 top-0 left-0 w-screen h-screen flex justify-center items-center" v-if="newProjectOpen">
                        <div class="w-1/2 h-2/6 bg-white rounded-xl shadow-xl border border-purple-600 flex flex-col justify-center items-center p-2">
                            <input class="rounded-lg text-lg mb-2 p-2 w-64 border border-blue-700 font-semibold" placeholder="new Project" v-model="newProjName"/>
                            <button class="bg-blue-700 text-white rounded-lg w-64 p-3 mt-4 text-lg font-medium" @click="createProject(newProjName)">Create</button>
                            <button class="bg-purple-700 text-white rounded-lg w-32 p-3 mt-4 text-md font-medium" @click="newProjectOpen = false">Close</button>
                        </div>
                    </div>
                </teleport>
            </div>
        </div>
    </div>
</div>
</template>

<script setup>
import {ref,onMounted} from 'vue'
import {useRouter} from 'vue-router'

const router = useRouter()

const projects = ref([])

const newProjectOpen = ref(false);
const newProjName = ref("");

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

async function createProject(name) {
    const response = await fetch('http://localhost:5000/createProject?name=' + name);
    if (!response.ok) {
        console.log('failed to create project')
    }
    else {
        getProjects();
        newProjectOpen.value = false;
    }
}

onMounted(() => {
    getProjects()
})
</script>