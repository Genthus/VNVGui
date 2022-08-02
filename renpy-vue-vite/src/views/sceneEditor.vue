<template>
    <div class="w-screen bg-slate-100 p-4 m-auto">
        <div class="flex flex-row gap-4 scroll-m-0">
            <dialogueView class="basis-3/4 bg-white shadow-inner rounded-lg"
            @save="saveScene" 
            @updateDialogue="updateDialogue" 
            @addDialogue="addDialogue" 
            @addDialogueAt="addDialogueAt"
            @deleteDialogue="deleteDialogue"
            :dialogues="lines"/>
            <dialogueOptions class="grow bg-white shadow-inner rounded-lg"/>
        </div>
    </div>
</template>

<script setup>
import dialogueView from '../components/dialogueView.vue'
import dialogueOptions from '../components/dialogueOptions.vue'
import {ref, onMounted} from 'vue'
import {useRoute} from 'vue-router'
const route = useRoute()

const id = ref(0)
const name = ref("")
const lines = ref([])
const uniqueId = ref(0)

function loadDialogues(sceneId) {
    fetch("http://localhost:5000/testProject").then(response => {
        if (!response.ok) {
            throw new Error("Request failed")
        }
        return response.json()
    })
    .then(data => {
        const scene = data.scenes[sceneId]
        console.log(scene)
        id.value = scene.id
        name.value = scene.name
        lines.value = scene.lines
        lines.value.forEach(l => {
            l.uniqueId = uniqueId.value++;
        });
    })
    .catch(error => console.log(error))
}

async function saveScene() {
    await fetch("http://localhost:5000/saveScene", {
        method: 'POST',
        headers: {
            'Accept' : 'application/json',
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({'id': id.value, 'name': name.value,'lines': lines.value})
    });
}

function updateDialogue(dialg) {
    lines.value[dialg.id] = dialg;
}

function addDialogue() {
    const newDialg = {
        id: lines.value.length,
        type: '',
        character: '',
        text: ''
    }
    lines.value.push(newDialg);
}

function addDialogueAt(pos) {
    const newDialg = {
        id: pos,
        type: '',
        character: '',
        text: '',
        uniqueId: uniqueId.value++
    }
    lines.value.splice(pos,0,newDialg);
    for (let i = 0; i < lines.value.length; i++) {
        lines.value[i].id = i;
    }
}

function deleteDialogue(i) {
    lines.value.splice(i,1);
}

onMounted (()=> {
    loadDialogues(route.params.id)
})

</script>