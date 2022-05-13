<template>
    <div class="sceneEditor">
        <dialogueView :dialogues="sceneDialogues"/>
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
            sceneDialogues: []
        }
    },
    methods: {
        loadDialogues() {
            fetch("http://localhost:5000/testDialogues").then(response => {
                if (!response.ok) {
                    throw new Error("Request failed")
                }
                return response.json()
            })
            .then(data => {
                console.log(data.dialogues)
                this.sceneDialogues = data.dialogues.start
            })
            .catch(error => console.log(error))
        }
    },
    created() {
        this.loadDialogues()
    }
}
</script>

<style scoped>
.sceneEditor {
    position: absolute;
    width: 1920px;
    height: 1080px;
    background: #5c2525;
}
</style>