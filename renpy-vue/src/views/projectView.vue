<template>
<div class="projectView">
    <ul class="scenes" :key="scene.id" v-for="scene in scenes">
      <button @click="changeScene(scene.id)">{{scene.name}}</button>
    </ul>
</div>
</template>

<script>
export default {
    name: 'projectView',
    data() {
        return {
            scenes: []
        }
    },
    methods: {
        changeScene(sceneId) {
            console.log("switching to scene " + sceneId)
            this.$router.push('/sceneEditor/'+sceneId)
        },
        loadProject() {
            fetch("http://localhost:5000/testProject").then(response => {
                if (!response.ok) {
                    throw new Error("Request failed")
                }
                return response.json()
            })
            .then(data => {
                this.scenes = data.scenes
            })
            .catch(error => console.log(error))
        }
    },
    mounted() {
        this.loadProject()
    }
}
</script>

<style scoped>
.projectView {
    position: absolute;
    width: 1920px;
    height: 1080px;
    background: #ffffff;
}
</style>