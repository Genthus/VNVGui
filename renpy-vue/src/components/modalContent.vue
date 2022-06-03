<template>
    <div class="notif">
        <h2> Notification </h2>
        <p> filler text </p>
        <button @click="$emit('close')">Close</button>
    </div>
</template>

<script>

export default {
    name: "modalContent",
    emits: ['close']
}
</script>

<style scoped>
.modal > div {
    background-color: #fff;
    padding: 5%;
    border-radius: 11px;
}
</style>