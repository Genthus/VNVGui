<template>
    <div class="p-4 relative" :class="newDialogue.type">
        <div class="flex flex-row justify-center gap-8 mx-auto" v-if="newDialogue.type == ''">
            <button class="bg-indigo-500 block py-4 px-12 rounded-md shadow-md text-white" @click="setType('text')">Text</button>
            <button class="bg-indigo-500 block py-4 px-12 rounded-md shadow-md text-white" @click="setType('jump')">Jump</button>
            <button class="bg-indigo-500 block py-4 px-12 rounded-md shadow-md text-white" @click="setType('show')">Show</button>
            <button class="bg-indigo-500 block py-4 px-12 rounded-md shadow-md text-white" @click="setType('scene')">Scene</button>
            <button class="bg-indigo-500 block py-4 px-12 rounded-md shadow-md text-white" @click="setType('script')">Script</button>
            <button class="bg-indigo-500 block py-4 px-12 rounded-md shadow-md text-white" @click="$emit('deleteDialogue')">Delete</button>
        </div>
        <form class="space-y-4" action="" v-if="dialogue.type != ''">
            <div class="bg-white/50 rounded-lg absolute top-0 right-0 p-2 flex flex-wrap flex-row gap-3">
                <span class="text-md text-right">{{newDialogue.type}}</span>
                <span class="text-md text-right">{{newDialogue.id}}</span>
                <svg @click="$emit('deleteDialogue')" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </div>
            <div class="bg-white block w-2/3 text-xl shadow-inner rounded-lg p-3" v-if="newDialogue.type === 'text'">
                <input @change="updateDialogue" v-model="newDialogue.character" placeholder="{{newDialogue.character}}"/>
            </div>
            <div class="bg-white block w-full text-xl shadow-inner rounded-lg p-3">
                <textarea @change="updateDialogue" v-model="newDialogue.text" placeholder="{{newDialogue.text}}"></textarea>
            </div>
        </form>
    </div>
</template>

<script setup>
import {ref} from 'vue'

const props = defineProps({
    dialogue: Object
})
const emit = defineEmits([
    'updateDialogue',
    'deleteDialogue'
])

const newDialogue = ref(props.dialogue)

function updateDialogue() {
    emit('updateDialogue', newDialogue.value)
}

function setType(t) {
    newDialogue.value.type = t;
}
</script>