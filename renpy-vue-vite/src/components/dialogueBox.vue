<template>
    <div class="dialogueBox" :class="newDialogue.type">
        <div class="typeButtons" v-if="newDialogue.type == ''">
            <button @click="setType('text')">Text</button>
            <button @click="setType('jump')">Jump</button>
            <button @click="setType('show')">Show</button>
            <button @click="setType('scene')">Scene</button>
            <button @click="setType('script')">Script</button>
            <button @click="$emit('deleteDialogue')">Delete</button>
        </div>
        <form action="" v-if="dialogue.type != ''">
            <div class="type">
                <input @change="updateDialogue" v-model="newDialogue.type" placeholder="newDialogue.type">
            </div>
            <div class="idNumber">
                <input @change="updateDialogue" type="number" v-model="newDialogue.id" placeholder="newDialogue.id">
            </div>
            <div class="character" v-if="newDialogue.type === 'text'">
                <input @change="updateDialogue" v-model="newDialogue.character" placeholder="{{newDialogue.character}}"/>
            </div>
            <div class="textBox">
                <textarea @change="updateDialogue" v-model="newDialogue.text" placeholder="{{newDialogue.text}}"></textarea>
            </div>
            <button @click="$emit('deleteDialogue')">Delete</button>
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

<style scoped>
.dialogueBox {
    width: 100%;
    height: auto;
    flex: none;
    order: 0;
    flex-grow: 0;
    background: #EDEDED;
    border-radius: 11px;
    justify-content: center;
}

form {
    padding: 1%;
}

.character {
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 18px;
    line-height: 21px;
}

.text  {
    
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 14px;
}

.typeButtons {
    padding: 2%;
    display:flex;
    justify-content: center;
}

.typeButtons button {
    width: 100px;
    height: 100px;
    margin: 0 2%;
}

.text {
    background: rgb(80, 126, 218);
}
.jump {
    background: #92e052;
}
.show {
    background: #e463d3;
}
.scene {
    background: #e9d060;
}
.script {
    background: #ee7171;
}
</style>