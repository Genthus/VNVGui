<template>
<div class="w-full flex flex-row flex-grow-0 items-center">
    <component :is="tag" class ='relative w-full h-48 p-2 aspect-square overflow-hidden bg-blue-200 rounded-lg'>
        <img class="block h-full w-full object-scale-down" :src="imageFile" :alt="fileName[1].name" :title="fileName[1].name">
    </component>
</div>
</template>
<script setup>
import {ref ,onMounted} from 'vue'
import { useRoute } from 'vue-router';
const route = useRoute()
const props = defineProps({
    tag: {type: String, default: 'li'},
    'fileName' : []
})

const imageFile = ref({})

async function getFileImage() {
    const response = await fetch("http://localhost:5000/getFile?projectId=" 
                                + route.params.projectId 
                                + "&fileDir="+props.fileName[1].fileDir, {
        method: 'GET',
    });
    const blob = await response.blob()
    imageFile.value = URL.createObjectURL(blob)
    console.log(imageFile.value)
}

onMounted(() => {
	console.log(props.fileName)
    getFileImage()

})
</script>

<style scoped lang="scss">
.resourceFile {
	width: 50%;
	height: 50%;
	background: #6c6;
	border-radius: 11px;
	margin-bottom: 1%;
	padding: 1%;
    order: 0;
    flex-grow: 0;
	display: flex;
	flex-direction: row;
	align-items: center;
}

.file-preview {
	height: 100%;
	margin: 1% 2.5%;
	position: relative;
	border: solid 2px #000;
	border-radius: 11px;
	background-color: #fff;
	aspect-ratio: 1/1;
	overflow: hidden;
	img {
		width: 100%;
		height: 100%;
		display: block;
		object-fit: scale-down;
	}
}
</style>