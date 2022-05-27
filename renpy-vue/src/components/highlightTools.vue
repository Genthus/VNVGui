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
    width: 1160px;
    height: 30px;
    margin: 1% 0;
    flex: none;
    order: 0;
    flex-grow: 0;
    background: #b8b8b8;
    border-radius: 11px;
    justify-content: left;
}

.buttons {
    display:flex;
    justify-content: center;
}

button {
    margin: 3px 1%;
}
</style>