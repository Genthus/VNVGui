<template>
    <div class="bar">
        <div class="buttons">
            <button @click="$emit('addDialogueAt')">New Line</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'highlightTools',
}
</script>

<style scoped>
.bar {
    width: 100%;
    paddin:auto;
    flex: none;
    background: #d3993d;
    border-radius: 11px;
    justify-content: left;
}

.buttons {
    top:50%;
    display:flex;
    justify-content: center;
}

button {
    margin: 3px 1%;
}
</style>