<template> 
<div class="" v-show="title == selectedTitle">
    <ul class="flex flex-col flex-wrap overflow-scroll gap-2 p-2">
        <resourceFile :key="fileName.fileName" v-for="fileName of fileNames" :fileName="fileName" tag="li"/>
    </ul>
</div>
</template>

<script setup>
import {inject} from 'vue'
import resourceFile from './resourceFile.vue'

defineProps({
    'title' : String,
    'fileNames': Object
})
const selectedTitle = inject('selectedTitle', 'character')
console.log(selectedTitle)
</script>

<style scoped>
.resourceBox {
    position: relative;
    width:100%;
    height: 90%;
}

.files {
    display: flex;
	position: relative;
	list-style: none;
	flex-direction: column;
    overflow-y: scroll;
	align-items: flex-start;
	padding: 1%;
	gap: 1%;

}
</style>