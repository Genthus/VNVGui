<template>
    <div class="dialogueBox">
        <h3>{{dialogue.type}}</h3>
        <h2>{{dialogue.character}}</h2>
        <p>{{dialogue.text}}</p>
    </div>
</template>

<script>
export default {
    name: 'dialogueBox',
    props: {
        dialogue: Object,
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
}

.dialogueBox h2 {
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 18px;
    line-height: 21px;
    position: relative;
    left: 3.38%;
    right: 4.01%;
    top: 0.2%;
    bottom: 96.33%;
}

.dialogueBox p {
    position: relative;
    left: 3.38%;
    right: 4.01%;
    top: 3.50%;
    bottom: 87.63%;
    
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 14px;
}
</style>