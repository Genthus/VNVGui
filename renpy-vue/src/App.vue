<template>
<div class="h-screen bg-gray-100">
  <nav class="basis-1/10 bg-white border-gray-200 px-2 sm:px-4 py-2.5 rounded">
    <div class="container flex flex-wrap justify-between items-center mx-auto">
      <div class="flex items-center">
        <span class="self-center text-xl font-semibold whitespace-nowrap">Renpy Vue</span>
      </div>
      <div class="block w-auto">
        <ul class="flex flex-row p-4 bg-gray-50 rounded-lg border-gray-100 space-x-8 mt-0  text-sm font-medium border-0 ">
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
  <router-view @projectLoaded="hasProject = true" class="h-screen"/>
</div>
</template>

<script setup>
//const project = {}
import {ref} from 'vue'
import {useRoute} from 'vue-router'
const route = useRoute()
const hasProject = ref(false)
</script>
