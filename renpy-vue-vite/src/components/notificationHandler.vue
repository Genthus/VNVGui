<template>
    <div class="root">
        <button @click="isOpen = true">Open Resources</button>
        <teleport to="body">
            <div class="modal" v-if="isOpen">
                <resourceLoader @close="isOpen = false"/>
            </div>
        </teleport>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import resourceLoader from './resourceLoader.vue'

const isOpen = ref(false)
</script>

<style scoped>
.root {
    position: relative;
}

.modal {
    position:absolute;
    top: 0;
    left: 0;
    background-color: rgba(86, 71, 174, 0.199);
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

button {
    margin:1%;
}

</style>