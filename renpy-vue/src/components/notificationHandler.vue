<template>
    <div class="relative">
        <button class="p-3 w-96 bg-purple-500 rounded-lg justify-center text-white shadow-md" @click="isOpen = true">Open Resources</button>
        <teleport to="body">
            <div class="absolute bg-purple-500 bg-opacity-20 top-0 left-0 w-screen h-screen flex justify-center items-center" v-if="isOpen">
                <resourceLoader @close="isOpen = false; $emit('reloadResources')"/>
            </div>
        </teleport>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import resourceLoader from './resourceLoader.vue'

const isOpen = ref(false)
</script>