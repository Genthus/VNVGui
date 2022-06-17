<template>
<div class="resourceFile">
    <component :is="tag" class ='file-preview'>
        <img :src="imageFile" :alt="fileName.name" :title="fileName.name">
    </component>
</div>
</template>
<script setup>
import {ref ,onMounted} from 'vue'
import { useRoute } from 'vue-router';
const route = useRoute()
const props = defineProps({
    tag: {type: String, default: 'li'},
    'fileName' : Object
})

const imageFile = ref({})

async function getFileImage() {
    const response = await fetch("http://localhost:5000/getFile?projectId=" 
                                + route.params.projectId 
                                + "&fileDir="+props.fileName.fileDir, {
        method: 'GET',
    });
    const blob = await response.blob()
    imageFile.value = URL.createObjectURL(blob)
    console.log(imageFile.value)
}

onMounted(() => {
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