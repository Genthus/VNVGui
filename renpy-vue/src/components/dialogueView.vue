<template>
    <div class="flex flex-col flex-nowrap overflow-scroll p-2">
        <draggable
            class="bg-blue-100 rounded-lg shadow-md"
            :list="dialogues"
            :group="{ name: 'people' }"
            item-key="uniqueId"
            @end="$emit('updateNumbers')"
        >
            <template #item="{ element }">
                <div>
                    <HighlightTools
                        v-if="element.highlight == true"
                        @addDialogueAt="$emit('addDialogueAt', element.id)"
                        @save="$emit('save')"
                    />
                    <dialogueBox
                        @updateDialogue="updateDialogue"
                        @deleteDialogue="$emit('deleteDialogue', element.id)"
                        @click="selectComponent(element.id)"
                        @save="$emit('save')"
                        @addDialogueAt="$emit('addDialogueAt', element.id)"
                        :dialogue="element"
                    />
                    <HighlightTools
                        v-if="element.highlight == true"
                        @addDialogueAt="$emit('addDialogueAt', element.id + 1)"
                        @save="$emit('save')"
                    />
                </div>
            </template>
        </draggable>
        <HighlightTools
            v-if="dialogues.length == 0"
            @addDialogueAt="$emit('addDialogueAt', 0)"
            @save="$emit('save')"
        />
    </div>
</template>

<script setup>
import dialogueBox from "./dialogueBox.vue";
import { ref } from "vue";
import draggable from "vuedraggable";
import HighlightTools from "./highlightTools.vue";

const props = defineProps({
    dialogues: Array,
});
const emit = defineEmits([
    "updateDialogue",
    "save",
    "updateDialogue",
    "addDialogue",
    "addDialogueAt",
    "deleteDialogue",
    "updateNumbers",
]);

const currentHightlight = ref(0);

function updateDialogue(dialg) {
    emit("updateDialogue", dialg);
}

function selectComponent(id) {
    props.dialogues.forEach((d) => {
        if (d.id == id) {
            d.highlight = true;
            currentHightlight.value = d.id;
        } else {
            d.highlight = false;
        }
    });
}
</script>
