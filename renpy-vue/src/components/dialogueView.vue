<template>
    <div class="dialogueView">
        <div class="dialogueBoxes" :key="dialogue.id" v-for="dialogue in dialogues">
            <dialogueBox @updateDialogue="updateDialogue" :dialogue="dialogue"/>
        </div>
        <toolBox @save="$emit('save')" class="dialogueBoxes"/>
    </div>
</template>

<script>
import dialogueBox from './dialogueBox.vue'
import toolBox from './toolBox.vue'
export default {
    name: 'dialogueView',
    components: {
        dialogueBox,
        toolBox
    },
    props: {
        dialogues: Array
    },
    methods: {
        updateDialogue(dialg) {
            this.$emit('updateDialogue',dialg)
        },
    }
}
</script>

<style scoped>
.dialogueView {
    position:absolute;
    width: 1200px;
    height: 900px;
    margin: 40px;
    margin-top: 150px;
    overflow-y: scroll;
    background: #D0D0D0;
    border-radius: 11px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 0px;
    gap: 5px;
}
.dialogueBoxes {
    margin: 0px 20px;
}
</style>