<template>
<div class="container">
  <nav>
    <div class="options">

    </div>
    <div class="links">
      <router-link to="/">Project View</router-link> |
    </div>
  </nav>
  <router-view/>
</div>
</template>

<script>
export default {
  data() {
    return {
      project: {}
    }
  }
}
</script>

<style>
body {
  background:#212122;
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
    background: #D0D0D0;
}

.links {
  padding: 1%;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
