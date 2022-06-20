<template>
   <div class="dialogueOptionsBox">
       <ResourceWrapper :tabTitles="resources">
           <ResourceBox v-for="title in resources" :key="title+'Tab'" 
           :title="title"
           :fileNames="resourcesObject[title]"/>
       </ResourceWrapper>
        <div class="optionBox">
            <notificationHandler
            @reloadResources="$emit('reloadResources')"/>
        </div>
   </div> 
</template>

<script setup>
import notificationHandler from './notificationHandler.vue'
import ResourceWrapper from './resourceWrapper.vue'
import ResourceBox from './resourceBox.vue'

defineProps([
    'resources',
    'resourcesObject'
])
</script>

<style scoped>
.dialogueOptionsBox {
    position:relative;
    width: 22%;
    height: 92%;
    overflow-y: scroll;
    background: #2a2929;
    border-radius: 11px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding:1%;
    gap:1%;
}
.optionBox {
    width: 100%;
    height: 5%;
    flex: none;
    order: 0;
    flex-grow: 0;
    background: #EDEDED;
    border-radius: 11px;
    justify-content: center;
}
</style>