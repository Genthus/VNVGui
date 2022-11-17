<template>
    <div class="flex flex-row gap-4 p-4">
        <dialogueView class="basis-3/4 bg-white shadow-inner rounded-xl"
        @save="saveScene" 
        @updateDialogue="updateDialogue" 
        @addDialogue="addDialogue" 
        @addDialogueAt="addDialogueAt"
        @deleteDialogue="deleteDialogue"
        @updateNumbers="updateNumbers"
        :dialogues="lines"/>
        <dialogueOptions class="grow bg-white shadow-inner rounded-xl"
        :resources="resourceList"
        :resourcesObject="resourcesObject"
        @reloadResources="loadResources"/>
    </div>
</template>

<script setup>
import dialogueView from '../components/dialogueView.vue'
import dialogueOptions from '../components/dialogueOptions.vue'
import {ref, onMounted} from 'vue'
import {useRoute, useRouter} from 'vue-router'
const route = useRoute()
const router = useRouter()

const id = ref(0)
const name = ref("")
const lines = ref([])
const uniqueId = ref(0)
const resourceList = ref([])
const resourcesObject = ref([])

function unsavedChanges() {
    router.push({path: route.fullPath, params: {unsaved : true}})
}

function loadDialogues(sceneId) {
    fetch("http://localhost:5000/getScene?projectId=" + route.params.projectId + '&sceneId=' + sceneId).then(response => {
        if (!response.ok) {
            throw new Error("Request failed")
        }
        return response.json()
    })
    .then(data => {
        id.value = data.id
        name.value = data.name
        lines.value = data.lines
        lines.value.forEach(l => {
            l.uniqueId = uniqueId.value++;
        });
    })
    .catch(error => console.log(error))
}

function loadResources() {
    fetch("http://localhost:5000/getResourceList?projectId=" + route.params.projectId).then(response => {
        if (!response.ok) {
            throw new Error("Request failed")
        }
        return response.json()
    })
    .then(data => {
        resourceList.value = Object.keys(data)
        resourcesObject.value = data
    })
    .catch(error => console.log(error))
}

async function saveScene() {
    await fetch("http://localhost:5000/saveScene?projectId=" + route.params.projectId + '&sceneId='+route.params.sceneId, {
        method: 'POST',
        headers: {
            'Accept' : 'application/json',
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({'id': id.value, 'name': name.value,'lines': lines.value})
    });
    unsavedChanges()
}

function updateDialogue(dialg) {
    lines.value[dialg.id] = dialg;
    unsavedChanges()
}

function addDialogue() {
    const newDialg = {
        id: lines.value.length,
        type: '',
        character: '',
        text: '',
        menu: [] 
    }
    lines.value.push(newDialg);
    updateNumbers()
    unsavedChanges()
}

function addDialogueAt(pos) {
    const newDialg = {
        id: pos,
        type: '',
        character: '',
        text: '',
        uniqueId: uniqueId.value++,
        menu: []
    }
    lines.value.splice(pos,0,newDialg);
    for (let i = 0; i < lines.value.length; i++) {
        lines.value[i].id = i;
    }
    updateNumbers()
    unsavedChanges()
}

function deleteDialogue(i) {
    lines.value.splice(i,1);
    for (let i = 0; i < lines.value.length; i++) {
        lines.value[i].id = i;
    }
    updateNumbers()
    unsavedChanges()
}

function updateNumbers() {
    for (let i = 0; i < lines.value.length; i++) {
        lines.value[i].id = i;
    }
}

onMounted (()=> {
    loadDialogues(route.params.sceneId)
    loadResources()
})

</script>
