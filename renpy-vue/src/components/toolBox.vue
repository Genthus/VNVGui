<template>
    <div class="dialoguetoolBox">
        <div class="buttons">
            <button>Button</button>
            <button>Button</button>
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