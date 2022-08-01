<template>
   <div class="dialogueOptionsBox">
       <div class="optionBox">
           <notificationHandler/>
       </div>
   </div> 
</template>

<script setup>
import notificationHandler from './notificationHandler.vue'
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
    gap: 1%;
    padding:1%;
}
.optionBox {
    width: 100%;
    height: auto;
    flex: none;
    order: 0;
    flex-grow: 0;
    background: #EDEDED;
    border-radius: 11px;
    justify-content: center;
}
</style>