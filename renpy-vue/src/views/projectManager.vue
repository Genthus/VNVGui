<template>
<div class="w-full">
    <div class="container shadow-md mt-3 rounded-lg p-6 m-auto bg-purple-400">
        <span class="mb-2 text-lg font-bold tracking-tight text-white">Projects</span>
        <div class="flex flex-wrap flex-col justify-center p-2 items-center">
            <ul class="" :key="project.id" v-for="project in projects">
                <div class="relative bg-white rounded-lg w-64 p-3 mt-4 text-lg font-medium">
                    <div class="bg-white cursor-pointer mr-5" @click="setProject(project.id)">
                        <span class="text-lg text-right font-bold">{{project.name}}</span>
                    </div>
                    <div class="bg-slate-200/50 rounded-l-lg absolute top-0 right-0 p-2 flex flex-wrap flex-row gap-3">
                        <svg @click="deleteProject(project.name)" v-if="project.name != 'test'" class="w-6 h-6 cursor-pointer" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                    </div>
                </div>
            </ul>
            <div class="relative">
                <button class="bg-blue-700 text-white rounded-lg w-64 p-3 mt-4 text-lg font-medium" @click="newProjectOpen = true">New Project</button>
                <teleport to="body">
                    <div class="absolute bg-purple-500 bg-opacity-20 top-0 left-0 w-screen h-screen flex justify-center items-center" v-if="newProjectOpen">
                        <div class="w-1/2 h-2/6 bg-white rounded-xl shadow-xl border border-purple-600 flex flex-col justify-center items-center p-2">
                            <input class="rounded-lg text-lg mb-2 p-2 w-64 border border-blue-700 font-semibold" v-model="newProjData.name"/>
                            <div class="input-errors" v-for="error of v$.name.$errors" :key="error.$uid">
                                <div class="error-msg">{{ error.$message }}</div>
                            </div>
                            <button class="bg-blue-700 text-white rounded-lg w-64 p-3 mt-4 text-lg font-medium" @click="createProject(newProjData.name)">Create</button>
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
import {useVuelidate} from '@vuelidate/core'
import {required} from '@vuelidate/validators'

const router = useRouter()

const projects = ref([])

const newProjectOpen = ref(false);
const newProjData = ref({
    name : ""
})

const rules = {
    name : {required}
}

const v$ = useVuelidate(rules, newProjData)

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
    const result = await this.v$.$validate()
    if (!result) {
        console.log('invalid')
        return
    }
    const response = await fetch('http://localhost:5000/createProject?name=' + name);
    if (!response.ok) {
        console.log('failed to create project')
    }
    else {
        getProjects();
        newProjectOpen.value = false;
    }
}

async function deleteProject(name) {
    const response = await fetch('http://localhost:5000/deleteProject?name=' + name);
    if (!response.ok) {
        console.log('failed to delete project')
    }
    else {
        getProjects();
    }
}

onMounted(() => {
    getProjects()
})
</script>