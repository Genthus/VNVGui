<template>
    <div class="p-4 relative rounded-lg mb-4" 
    :class="{
        'bg-green-400': newDialogue.type == 'text',
        'bg-teal-400': newDialogue.type == 'jump',
        'bg-blue-400': newDialogue.type == 'show',
        'bg-amber-400': newDialogue.type == 'scene',
        'bg-purple-400': newDialogue.type == 'sfx',
        'bg-orange-400': newDialogue.type == 'music',
        'bg-yellow-400': newDialogue.type == 'script',
        'bg-gray-400': newDialogue.type == 'menu',
        'bg-gray-800': newDialogue.type == 'game end',
    }">
        <div class="flex flex-row justify-center gap-1 mx-auto" v-if="newDialogue.type == ''">
            <button class="bg-indigo-500 block py-4 px-8 rounded-md shadow-md text-white" @click="setType('text')">Text</button>
            <button class="bg-indigo-500 block py-4 px-8 rounded-md shadow-md text-white" @click="setType('jump')">Jump</button>
            <button class="bg-indigo-500 block py-4 px-8 rounded-md shadow-md text-white" @click="setType('show')">Show</button>
            <button class="bg-indigo-500 block py-4 px-8 rounded-md shadow-md text-white" @click="setType('scene')">Scene</button>
            <button class="bg-indigo-500 block py-4 px-8 rounded-md shadow-md text-white" @click="setType('sfx')">SFX</button>
            <button class="bg-indigo-500 block py-4 px-8 rounded-md shadow-md text-white" @click="setType('music')">Music</button>
            <button class="bg-indigo-500 block py-4 px-8 rounded-md shadow-md text-white" @click="setType('script')">Script</button>
            <button class="bg-indigo-500 block py-4 px-8 rounded-md shadow-md text-white" @click="setType('menu')">Menu</button>
            <button class="bg-indigo-500 block py-4 px-8 rounded-md shadow-md text-white" @click="setType('game end')">Game End</button>
            <button class="bg-indigo-500 block py-4 px-8 rounded-md shadow-md text-white" @click="$emit('deleteDialogue')">Delete</button>
        </div>
        <form class="space-y-4" action="" v-if="dialogue.type != ''">
            <span class="text-xl text-right text-white font-bold">{{newDialogue.type}}</span>
            <div class="bg-slate-200/50 rounded-l-lg absolute top-0 right-0 p-2 flex flex-wrap flex-row gap-3">
                <span class="text-md text-right">#{{newDialogue.id}}</span>
                <svg @click="$emit('deleteDialogue')" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </div>
            <div class="bg-white block w-2/3 text-xl shadow-inner rounded-lg p-3" v-if="newDialogue.type === 'text'">
                <input class="w-full font-semibold" @change="updateDialogue" v-model="newDialogue.character" placeholder="{{newDialogue.character}}"/>
            </div>
            <div class="bg-white block w-full min-h-24 text-lg shadow-inner rounded-lg p-3" v-if="newDialogue.type != 'menu' && newDialogue.type != 'game end'">
                <textarea class="w-full min-h-full" @change="updateDialogue" v-model="newDialogue.text" placeholder="{{newDialogue.text}}"></textarea>
            </div>
            <div v-if="newDialogue.type=='menu'">
                <div v-for="menu in newDialogue.menu" class="bg-gray-600 p-2 m-2 rounded-lg flex justify-center">
                    <input class="m-2 font-semibold bg-white block w-1/3 text-xl shadow-inner rounded-lg p-3" @change="updateDialogue" v-model="menu.text" placeholder="text"/>
                    <input class="m-2 font-semibold bg-white block w-1/3 text-xl shadow-inner rounded-lg p-3" @change="updateDialogue" v-model="menu.destination" placeholder="destination scene"/>
                    <svg @click="deleteMenu(menu.id)" class="w-6 h-6" fill="none" stroke="white" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </div>
                <button v-if='dialogue.highlight==true' class="bg-blue-700 text-white rounded-lg w-48 p-2 mt-4 text-lg font-medium" @click="newDialogue.menu.push({name:'',destination:'', id: newDialogue.menu.length})">Create menu option</button>
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
    'deleteDialogue',
])

const newDialogue = ref(props.dialogue)

function updateDialogue() {
    emit('updateDialogue', newDialogue.value)
}

function setType(t) {
    newDialogue.value.type = t;
    if (t == 'menu') {
        menu = []
    }
}

function deleteMenu(id) {
    newDialogue.value.menu.splice(id,1);
}
</script>