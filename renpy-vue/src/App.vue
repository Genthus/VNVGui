<template>
<div class="container">
  <nav>
    <h1>Renpy Vue</h1>
    <div class="options">
      
      </div>
    <div class="links">
      <router-link to="/">Project View</router-link>
    </div>
  </nav>
  <router-view/>
</div>
</template>

<script setup>
//const project = {}
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
  width: 100%;
  height: 5%;
  top: 0;
  left:0;
  background: #5647ae;
  display: flex;
  justify-content: left;
  align-content: center;
  padding: 0 5%;
}

.links {
  padding: 1%;
  margin: 0 5%;
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
