<template>
    <div class="sceneEditor">
        <dialogueView :dialogues="lines"/>
    </div>
</template>

<script>
import dialogueView from '../components/dialogueView.vue'
export default {
    name : 'sceneEditor',
    components: {
        dialogueView
    },
    data() {
        return {
            id: 0,
            name: "",
            lines: []
        }
    },
    methods: {
        loadDialogues(sceneId) {
            fetch("http://localhost:5000/testProject").then(response => {
                if (!response.ok) {
                    throw new Error("Request failed")
                }
                return response.json()
            })
            .then(data => {
                const scene = data.scenes[sceneId]
                console.log(scene)
                this.id = scene.id
                this.name = scene.name
                this.lines = scene.lines
            })
            .catch(error => console.log(error))
        }
    },
    created() {
        this.loadDialogues(this.$route.params.id)
    }
}
</script>

<style scoped>
.sceneEditor {
    position: absolute;
    width: 1920px;
    height: 1080px;
    background: #ffffff;
}
</style>