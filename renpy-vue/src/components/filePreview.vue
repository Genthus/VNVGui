<template>
    <component :is="tag" class="file-preview">
        <button @click="$emit('remove', file)" class="close-icon" aria-label="Remove">×</button>
        <img :src="file.url" :alt="file.file.name" :title="file.file.name" />
        <span class="status-indicator loading-indicator" v-show="file.status == 'loading'">In Progress</span>
        <span class="status-indicator success-indicator" v-show="file.status == true">Uploaded</span>
        <span class="status-indicator failure-indicator" v-show="file.status == false">Error</span>
    </component>
</template>

<script>
export default {
    name: 'filePreview',
    props: {
        file: { type: Object, required: true },
        tag: { type: String, default: 'li' },
    },
    emits: ['remove']
}
</script>