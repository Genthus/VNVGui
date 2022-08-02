<template>
    <div class="flex flex-nowrap flex-col p-2">
        <div class="bg-blue-100 mt-3 rounded-lg shadow-md" :key="dialogue.uniqueId" v-for="dialogue in dialogues">
            <highlightTools 
            v-if="dialogue.highlight == true" 
            @addDialogueAt="$emit('addDialogueAt',dialogue.id)" @save="$emit('save')"/>
            <dialogueBox 
            @updateDialogue="updateDialogue" 
            @deleteDialogue="$emit('deleteDialogue', dialogue.id)"
            @click="selectComponent(dialogue.id)"
            :dialogue="dialogue"/>
            <highlightTools 
            v-if="dialogue.highlight == true" 
            @addDialogueAt="$emit('addDialogueAt',dialogue.id+1)" @save="$emit('save')"/>
        </div>
    </div>
</template>

<script setup>
import dialogueBox from './dialogueBox.vue'
import highlightTools from './highlightTools.vue'
import {ref} from 'vue'

const props = defineProps({
    dialogues: Array
})
const emit = defineEmits([
    'updateDialogue',
    'save',
    'updateDialogue',
    'addDialogue',
    'addDialogueAt',
    'deleteDialogue'
])

const currentHightlight = ref(0)

function updateDialogue(dialg) {
    emit('updateDialogue',dialg)
}

function selectComponent(id) {
    props.dialogues.forEach(d => {
        if (d.id == id) {
            d.highlight = true;
            currentHightlight.value = d.id;
        }
        else {
            d.highlight = false;
        }
    });
}
</script>