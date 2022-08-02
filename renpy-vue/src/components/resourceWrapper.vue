<template>
<div class="w-full flex flex-col">
    <ul class="flex flex-wrap text-sm text-center border-b">
        <li :class="{'bg-blue-400' : selectedTitle == title}" class="mr-2 inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-blue-300" v-for="title in tabTitles" :key="title" @click="selectedTitle = title">
            {{title}}
        </li>
    </ul>
    <div class="grow">
        <slot></slot>
    </div>
</div>
</template>

<script setup>
import {ref, provide} from 'vue'
defineProps({
    'tabTitles' : Array
})
const selectedTitle = ref('character')

provide("selectedTitle", selectedTitle)
</script>