<template> 
<div class="" v-show="title == selectedTitle">
    <draggable class="flex flex-col flex-wrap overflow-scroll gap-2 p-2"
    :list = "Object.entries(fileNames)"
    :group="{name:'people', pull: 'clone', put: false}" 
    :clone="placeResource"
    item-key="fileName">
        <template #item="{element}">
            <resourceFile :fileName="element" tag="li"/>
        </template>
    </draggable>
</div>
</template>

<script setup>
import {inject} from 'vue'
import resourceFile from './resourceFile.vue'
import draggable from "vuedraggable"

const props = defineProps({
    'title' : String,
    'fileNames': Object
})
const selectedTitle = inject('selectedTitle', 'character')

function placeResource(element) {
    return {
        text: element[1].fileName,
        type: (element[1].type == 'character' ? 'show' : (element[1].type == 'background' ? 'scene' : (element[1].type == 'sfx' ? 'sfx' : 'music'))),
        id: -1
    }
}

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