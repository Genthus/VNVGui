<template>
<div class="tabs">
    <ul class="tabsHeader">
        <li v-for="title in tabTitles" :key="title" @click="selectedTitle = title">
            {{title}}
        </li>
    </ul>
    <div class="resources">
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

<style scoped>
.tabs {
    width: 100%;
    height: 93%;
    margin: auto;
}
.tabsHeader {
    position: relative;
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
}

.tabsHeader li {
    text-align: center;
    padding: 2%;
    background-color: aliceblue;
    border-radius: 11px;
    cursor:pointer;
    transform: 0.4s all ease-out;
    margin-right: 3%;
}

.resources {
    border: solid 2px black;
    border-radius: 11px;
    display: flex;
    overflow-y: scroll;
    flex-wrap: wrap;
    height: 95%;
}
</style>