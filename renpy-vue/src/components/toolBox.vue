<template>
    <div class="dialoguetoolBox">
        <div class="buttons">
            <button @click="$emit('save')">Save</button>
            <button @click="$emit('addDialogue')">New Line</button>
            <button>Button</button>
            <button>Button</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'toolBox',

}
</script>

<style scoped>
.dialoguetoolBox {
    width: 1160px;
    height: 100px;
    flex: none;
    order: 0;
    flex-grow: 0;
    background: #EDEDED;
    border-radius: 11px;
    justify-content: left;
}

.buttons {
    display:flex;
}
</style>