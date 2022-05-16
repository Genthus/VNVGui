<template>
    <div class="dialogueBox">
        <form action="">
            <div class="type">
                <h3>{{newDialogue.type}}</h3>
            </div>
            <div class="character">
                <input v-model="newDialogue.character" placeholder="{{newDialogue.character}}"/>
            </div>
            <div class="text">
                <textarea v-model="newDialogue.text" placeholder="{{newDialogue.text}}"></textarea>
            </div>
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
            newDialogue : Object
        }
    },
    created() {
        this.newDialogue = this.dialogue
    }
}
</script>

<style>
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