<template>
    <div class="root">
        <button @click="isOpen = true">Open</button>
        <teleport to="body">
            <div class="modal" v-if="isOpen">
                <modalContent
                    @close="isOpen = false"
                />
            </div>
        </teleport>
    </div>
</template>

<script>
import { ref } from 'vue'
import modalContent from './modalContent.vue'
export default {
    name: "notificationHandler",
    components: {
        modalContent
    },
    data() {
        return {
            isOpen : ref(false),
        }
    }
}
</script>

<style scoped>
.root {
    position: relative;
}

.modal {
    position:absolute;
    top: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.2);
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

</style>