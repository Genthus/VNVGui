<template>
    <div class="flex flex-col flex-nowrap overflow-scroll p-2">
        <draggable class="bg-blue-100  rounded-lg shadow-md" 
        :list="dialogues" 
        :group="{name:'people'}" 
        item-key="uniqueId"
        @end="$emit('updateNumbers')">
            <template #item="{element}">
                <dialogueBox 
                @updateDialogue="updateDialogue" 
                @deleteDialogue="$emit('deleteDialogue', element.id)"
                @click="selectComponent(element.id)"
                @save="$emit('save')"
                @addDialogueAt="$emit('addDialogueAt',element.id)"
                :dialogue="element"/>
            </template>
        </draggable>
        <HighlightTools v-if="dialogues.length == 0"/>
    </div>
</template>

<script setup>
import dialogueBox from './dialogueBox.vue'
import {ref} from 'vue'
import draggable from "vuedraggable"
import highlightTools from './highlightTools.vue';
import HighlightTools from './highlightTools.vue';

const props = defineProps({
    dialogues: Array
})
const emit = defineEmits([
    'updateDialogue',
    'save',
    'updateDialogue',
    'addDialogue',
    'addDialogueAt',
    'deleteDialogue',
    'updateNumbers'
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