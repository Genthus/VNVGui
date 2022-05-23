<template>
    <div class="dialogueBox">
        <form action="">
            <div class="type">
                <input @change="updateDialogue" v-model="newDialogue.type" placeholder="newDialogue.type">
            </div>
            <div class="idNumber">
                <input @change="updateDialogue" type="number" v-model="newDialogue.id" placeholder="newDialogue.id">
            </div>
            <div class="character" v-if="newDialogue.type === 'text'">
                <input @change="updateDialogue" v-model="newDialogue.character" placeholder="{{newDialogue.character}}"/>
            </div>
            <div class="text">
                <textarea @change="updateDialogue" v-model="newDialogue.text" placeholder="{{newDialogue.text}}"></textarea>
            </div>
            <button @click="$emit('deleteDialogue')">Delete</button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'dialogueBox',
    props: {
        dialogue: Object,
    },
    data() {
        return {
            newDialogue : this.dialogue
        }
    },
    methods: {
        updateDialogue() {
            this.$emit('updateDialogue',this.newDialogue)
        }
    }
}
</script>

<style scoped>
.dialogueBox {
    width: 1160px;
    height: 150px;
    flex: none;
    order: 0;
    flex-grow: 0;
    background: #EDEDED;
    border-radius: 11px;
    justify-content: left;
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
</style>