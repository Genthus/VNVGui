<template>
<div class="min-h-screen max-h-screen flex flex-col bg-blue-300 py-2">
  <nav class="w-11/12 mx-auto px-12 rounded-full bg-white border-gray-200 shadow-md p-2">
    <div class="flex flex-wrap justify-between items-center mx-auto">
      <div class="flex items-center">
        <svg class="mr-3 h-6 sm:h-9" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"></path></svg>
        <span class="self-center text-xl font-semibold whitespace-nowrap">Renpy Vue</span>
      </div>
      <div class="block w-auto">
        <ul class="flex flex-row p-4 bg-gray-50 rounded-lg border-gray-100 space-x-8 mt-0  text-sm font-medium border-0 ">
          <div
          class="block py-2 pr-4 pl-3 text-white bg-teal-700 rounded p-0"
          @click="parseProject"
          v-if="hasProject">Parse</div>
          <router-link
          class="block py-2 pr-4 pl-3 text-white bg-purple-700 rounded p-0"
          :to="{name: 'projectView', params: {projectId: route.params.projectId}}"  
          v-if="hasProject">Project View</router-link>
          <router-link 
          class="block py-2 pr-4 pl-3 text-white bg-blue-700 rounded p-0" 
          to="/projects" 
          @click="hasProject = false">Project Manager</router-link>
        </ul>
      </div>
    </div>
  </nav>
  <router-view @projectLoaded="hasProject = true" class="grow overflow-hidden"/>
</div>
</template>

<script setup>
//const project = {}
import {ref} from 'vue'
import {useRoute} from 'vue-router'
const route = useRoute()
const hasProject = ref(false)

async function parseProject() {
    const response =  await fetch("http://localhost:5000/parse?projectId=" + route.params.projectId)
    if (!response.ok) {
        console.log('failed to parse project')
      alert("Project failed to parse")
    }
    else {
      alert("Project parsed and sent to folder")
    }
}
</script>
