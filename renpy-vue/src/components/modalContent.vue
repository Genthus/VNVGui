<template>
    <div class="notif">
        <dropZone class="drop-area"
            @files-dropped="addFiles" #default="{ dropZoneActive }">
                <label for="file-input">
                    <span v-if="dropZoneActive">
                        <span>Drop Them Here</span>
                        <span class="smaller">to add them</span>
                    </span>
                    <span v-else>
                        <span>Drag Your Files Here</span>
                        <span class="smaller">
                            or <strong><em>click here</em></strong> to select files
                        </span>
                    </span>
                    <input type="file" id="file-input" multiple @change="onInputChange" />
                </label>
                <ul class="image-list" v-show="files.length">
                    <filePreview  v-for="file  of  files" :key="file.id" :file="file"  tag="li" @remove="removeFile" />
                </ul>
        </dropZone>
        <button @click.prevent="uploadFiles(files)"  class="upload-button">Upload</button>
        <br>
        <button @click="$emit('close')">Close</button>
    </div>
</template>

<script>
import dropZone from './dropZone.vue'
import useFileList from '../compositions/file-list'
import filePreview from './filePreview.vue'
import createUploader from '../compositions/file-uploader'

const {files,addFiles,removeFiles} = useFileList()
const {uploadFiles} = createUploader('http://localhost:5000')

export default {
    name: "modalContent",
    components: {
        dropZone,
        filePreview
    },
    data() {
        return {
            files,
            addFiles,
            removeFiles,
            uploadFiles
        }
    },
    methods: {
        onInputChange(e) {
            addFiles(e.target.files)
            e.target.value= null
        }
    },
}
</script>

<style scoped>
.modal > div {
    background-color: #fff;
    padding: 5%;
    border-radius: 11px;
}
</style>