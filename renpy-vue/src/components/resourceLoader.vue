<template>
    <div class="container h-5/6 bg-white rounded-xl shadow-xl border border-purple-600 flex flex-col justify-center items-center p-2">
        <dropZone class="bg-slate-100 shadow-inner items-center flex flex-col overflow-auto" @files-dropped="addFiles" #default="{ dropZoneActive }">
                <label for="file-input">
                    <span v-if="dropZoneActive">
                        <span>Drop Them Here</span>
                        <span class="smaller"> to add them</span>
                    </span>
                    <span v-else>
                        <span>Drag Your Files Here</span>
                        <span class="smaller">
                            or <strong><em>click here</em></strong> to select files
                        </span>
                    </span>
                    <input type="file" id="file-input" multiple @change="onInputChange" />
                </label>
                <ul class="w-full flex flex-col items-center overflow-scroll" v-show="files.length">
                    <filePreview v-for="file  of  files" :key="file.id" :file="file"  tag="li" 
					@remove="removeFile" 
					@editFileType="editFileType"
					@editFileName="editFileName"/>
                </ul>
        </dropZone>
        <button @click.prevent="uploadFiles(files)"  class="p-3 m-2 w-96 bg-purple-500 rounded-lg justify-center text-white shadow-md">Upload</button>
        <br>
        <button class="p-3 w-96 bg-blue-500 rounded-lg justify-center text-white shadow-md" @click="close">Close</button>
    </div>
</template>

<script setup>
import dropZone from './dropZone.vue'
import useFileList from '../compositions/file-list'
import filePreview from './filePreview.vue'
import createUploader from '../compositions/file-uploader'
import { useRoute } from 'vue-router'
const route = useRoute()

const {files,addFiles,removeFile, editFileName, editFileType} = useFileList()
const {uploadFiles} = createUploader('http://localhost:5000/uploadResource?projectId=' + route.params.projectId)

const emit = defineEmits([
    'close'
])

function onInputChange(e) {
    addFiles(e.target.files)
    e.target.value= null
}

function close() {
    files.value = []
    emit('close')
}
</script>

<style scoped lang="scss">
.notif {
    background-color: #fff;
    width: 60%;
    height: 60%;
    padding: 2%;
    border-radius: 11px;
	display: flex;
	flex-direction: column;
	justify-content: center;
}

.drop-area {
	height: 90%;
	background: #ffffff55;
	box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
	transition: .2s ease;
	&[data-active=true] {
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
		background: #ffffffcc;
	}
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
}
label {
	cursor: pointer;
	display: block;
	span {
		display: block;
	}
	input[type=file]:not(:focus-visible) {
		// Visually Hidden Styles taken from Bootstrap 5
		position: absolute !important;
		width: 1px !important;
		height: 1px !important;
		padding: 0 !important;
		margin: -1px !important;
		overflow: hidden !important;
		clip: rect(0, 0, 0, 0) !important;
		white-space: nowrap !important;
		border: 0 !important;
	}
	.smaller {
	}
}
.image-list {
	width: 95%;
	height: 80%;
	position: relative;
	display: flex;
	list-style: none;
	flex-direction: column;
    overflow-y: scroll;
	align-items: flex-start;
	padding: 1%;
	gap: 1%;

}
.filePreview {
	width: 100%;
}
.upload-button {
	display: block;
	appearance: none;
	border: 0;
	border-radius: 50px;
	padding: 0.75rem 3rem;
	margin: 1rem auto;
	font-weight: bold;
	background: #369;
	color: #fff;
	text-transform: uppercase;
}
button {
	cursor: pointer;
}
</style>