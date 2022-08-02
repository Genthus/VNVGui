<template>
    <div class="bg-slate-200 rounded-lg shadow-lg">
        <div class="p-2 flex flex-wrap justify-center items-center gap-4">
            <button class="bg-indigo-500 block py-4 px-12 rounded-md shadow-md text-white" @click="$emit('addDialogueAt')">New Line</button>
            <button class="bg-indigo-500 block py-4 px-12 rounded-md shadow-md text-white" @click="$emit('save')">Save</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'highlightTools',
}
</script>