
<template>
    <div class="dropZone" :data-active="active" @dragenter.prevent="setActive"
    @dragover.prevent="setActive" @dragleave.prevent="setInactive"
    @drop.prevent="onDrop">
        <slot :dropZoneActive="active"></slot>
    </div>
</template>

<script>
import {ref} from 'vue'

export default {
    name: "dropZone",
    emits: ['files-dropped'],
    data() {
        return {
            active: ref(false),
            inactiveTimeout: null
        }
    },
    methods: {
        setActive() {
            this.active.value = true
            clearTimeout(this.inactiveTimeout)
        },
        setInactive() {
            this.inactiveTimeout = setTimeout(() => {
                this.active.value = false
            }, 50);
        },
        onDrop(e) {
            this.$emit('files-dropped', [...e.dataTransfer.files])
        },
        preventDefaults(e) {
            e.preventDefault()
        }
    },
    events: ['dragenter','dragover','dragleave','drop'],
    mounted() {
        this.events.forEach((eventName) => {
            document.body.addEventListener(eventName,this.preventDefaults)
        });
    },
    unmounted() {

        this.events.forEach((eventName) => {
            document.body.removeEventListener(eventName,this.preventDefaults)
        });
    }
}
</script>

<style scoped>
.dropZone {
    width:20%;
    height:10%;
}
</style>