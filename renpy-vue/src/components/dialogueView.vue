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
        <toolBox @save="$emit('save')" 
        @addDialogue="$emit('addDialogue')" 
        class="dialogueBoxes"/>
    </div>
</template>

<script>
import dialogueBox from './dialogueBox.vue'
import toolBox from './toolBox.vue'
import highlightTools from './highlightTools.vue'

export default {
    name: 'dialogueView',
    components: {
        dialogueBox,
        toolBox,
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
    position:absolute;
    width: 1200px;
    height: 900px;
    margin: 2%;
    margin-top: 2%;
    overflow-y: scroll;
    background: #D0D0D0;
    border-radius: 11px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 1% 00px;
    gap: 5px;
}
.dialogueBoxes {
    margin: 0px 20px;
}
</style>