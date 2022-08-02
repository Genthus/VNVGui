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