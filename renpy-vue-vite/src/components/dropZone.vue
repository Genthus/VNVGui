
<template>
    <div class="dropZone" :data-active="active" @dragenter.prevent="setActive"
    @dragover.prevent="setActive" @dragleave.prevent="setInactive"
    @drop.prevent="onDrop">
        <slot :dropZoneActive="active"></slot>
    </div>
</template>

<script setup>
import {ref, onMounted, onUnmounted} from 'vue'
const emit = defineEmits([
    'files-dropped'
])

const active = ref(false)
const inactiveTimeout = ref(null)
const events = ['dragenter', 'dragover', 'dragleave', 'drop']

function setActive() {
    active.value = true
    clearTimeout(inactiveTimeout.value)
}
function setInactive() {
    inactiveTimeout.value = setTimeout(() => {
        active.value = false
    }, 50);
}
function onDrop(e) {
    emit('files-dropped', [...e.dataTransfer.files])
}
function preventDefaults(e) {
    e.preventDefault()
}

onMounted(()=> {
    events.forEach((eventName) => {
        document.body.addEventListener(eventName,preventDefaults)
    });
})

onUnmounted(()=> {
    events.forEach((eventName) => {
        document.body.removeEventListener(eventName,preventDefaults)
    });
})
</script>

<style scoped>
.dropZone {
    width:100%;
    height:100%;
    border-radius: 11px;
}
</style>