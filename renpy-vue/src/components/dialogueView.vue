<template>
    <div class="dialogueView">
        <div class="dialogueBoxes" :key="dialogue.uniqueId" v-for="dialogue in dialogues">
            <highlightTools 
            v-if="dialogue.highlight == true" 
            @addDialogueAt="$emit('addDialogueAt',dialogue.id)"/>
            <dialogueBox 
            @updateDialogue="updateDialogue" 
            @deleteDialogue="$emit('deleteDialogue', dialogue.id)"
            @click="selectComponent(dialogue.id)"
            :dialogue="dialogue"/>
            <highlightTools 
            v-if="dialogue.highlight == true" 
            @addDialogueAt="$emit('addDialogueAt',dialogue.id+1)"/>
        </div>
    </div>
</template>

<script>
import dialogueBox from './dialogueBox.vue'
import highlightTools from './highlightTools.vue'

export default {
    name: 'dialogueView',
    components: {
        dialogueBox,
        highlightTools
    },
    props: {
        dialogues: Array
    },
    data () {
        return {
            currentHightlight: 0
        }
    },
    methods: {
        updateDialogue(dialg) {
            this.$emit('updateDialogue',dialg)
        },
        selectComponent(id) {
            this.dialogues.forEach(d => {
                if (d.id == id) {
                    d.highlight = true;
                    this.currentHightlight = d.id;
                }
                else {
                    d.highlight = false;
                }
            });
        }
    }
}
</script>

<style scoped>
.dialogueView {
    position:relative;
    width: 70%;
    height: 92%;
    overflow-y: scroll;
    background: #2a2929;
    border-radius: 11px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 1%;
    padding:1%;
}
.dialogueBoxes {
    width: 100%;
}
</style>