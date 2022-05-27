<template>
    <div class="sceneEditor">
        <dialogueView @save="saveScene" 
        @updateDialogue="updateDialogue" 
        @addDialogue="addDialogue" 
        @addDialogueAt="addDialogueAt"
        @deleteDialogue="deleteDialogue"
        :dialogues="lines"/>
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
            lines: [],
            uniqueId: 0
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
                this.lines.forEach(l => {
                    l.uniqueId = this.uniqueId++;
                });
            })
            .catch(error => console.log(error))
        },
        async saveScene() {
            await fetch("http://localhost:5000/saveScene", {
                method: 'POST',
                headers: {
                    'Accept' : 'application/json',
                    'Content-Type' : 'application/json'
                },
                body: JSON.stringify({'id': this.id, 'name': this.name,'lines': this.lines})
            });
        },
        updateDialogue(dialg) {
            this.lines[dialg.id] = dialg;
        },
        addDialogue() {
            const newDialg = {
                id: this.lines.length,
                type: '',
                character: '',
                text: ''
            }
            this.lines.push(newDialg);
        },
        addDialogueAt(pos) {
            console.log(pos)
            const newDialg = {
                id: pos,
                type: '',
                character: '',
                text: '',
                uniqueId: this.uniqueId++
            }
            this.lines.splice(pos,0,newDialg);
            for (let i = 0; i < this.lines.length; i++) {
                this.lines[i].id = i;
            }
            console.log(this.lines)
        },
        deleteDialogue(i) {
            console.log(this.lines.splice(i,1));
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