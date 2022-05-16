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

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
    position: static;
    width: 1920px;
    height: 90px;
    left: 0px;
    top: 0px;
    background: #D0D0D0;
}

.links {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
