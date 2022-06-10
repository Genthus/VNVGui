<template>
<div class="container">
  <nav>
    <h1>Renpy Vue</h1>
    <div class="options">
      
      </div>
    <div class="links">
      <router-link :to="{name: 'projectView', params: {projectId: route.params.projectId}}" class="projectView" v-if="hasProject">Project View</router-link>
    </div>
    <router-link to="/projects" class="projectManager" @click="hasProject = false">Project Manager</router-link>
  </nav>
  <router-view @projectLoaded="hasProject = true"/>
</div>
</template>

<script setup>
//const project = {}
import {ref} from 'vue'
import {useRoute} from 'vue-router'
const route = useRoute()

const hasProject = ref(false)
</script>

<style>
body {
  background:#121212;
}

.container {
  width: 100%;
  height: 100%;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  position:absolute;
  width: 94%;
  height: 50px;
  top: 0;
  left:0;
  background: #5647ae;
  display: flex;
  justify-content: left;
  align-items: center;
  padding: 0 3%;
  gap: 2%;
}

.links {
  width: 20%;
  display: flex;
  flex-direction: row;
  gap: 4%;
   
}

.projectManager {
  right: 5%;
}

nav a {
  font-weight: bold;
  color: #ffffff;
}

h1 {
  color:#000000;
}

nav a.router-link-exact-active {
  color: #bc9eec;
}
</style>
