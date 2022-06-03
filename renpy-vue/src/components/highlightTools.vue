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
    padding: 0.5% 0%;
    flex: none;
    background: #f0f0f0;
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