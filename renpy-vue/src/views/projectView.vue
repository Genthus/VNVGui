<template>
    <div class="w-full">
        <sceneGraph :scenes="scenes" :jumps="jumps" v-if="!newSceneOpen" />
        <div
            class="container shadow-md mt-3 rounded-lg p-6 m-auto bg-green-400"
        >
            <span class="mb-2 text-lg font-bold tracking-tight text-white">{{
                name
            }}</span>
            <div
                class="flex flex-wrap flex-col justify-center p-2 items-center"
            >
                <ul :key="scene.id" v-for="scene in scenes">
                    <div
                        class="relative bg-white rounded-lg w-64 p-3 mt-4 text-lg font-medium"
                    >
                        <div
                            class="bg-white cursor-pointer mr-5"
                            @click="changeScene(scene.id)"
                        >
                            <h3 class="text-lg font-bold">{{ scene.name }}</h3>
                        </div>
                        <div
                            class="bg-slate-200/50 rounded-l-lg absolute top-0 right-0 p-2 flex flex-wrap flex-row gap-3"
                        >
                            <svg
                                @click="deleteScene(scene.id)"
                                class="w-6 h-6 cursor-pointer"
                                fill="none"
                                stroke="currentColor"
                                viewBox="0 0 24 24"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <path
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    stroke-width="2"
                                    d="M6 18L18 6M6 6l12 12"
                                ></path>
                            </svg>
                        </div>
                    </div>
                </ul>
                <div class="relative">
                    <button
                        class="bg-blue-700 text-white rounded-lg w-64 p-3 mt-4 text-lg font-medium"
                        @click="newSceneOpen = true"
                    >
                        New Scene
                    </button>
                    <teleport to="body">
                        <div
                            class="absolute bg-purple-500 bg-opacity-20 top-0 left-0 w-screen h-screen flex justify-center items-center"
                            v-if="newSceneOpen"
                        >
                            <div
                                class="w-1/2 h-2/6 bg-white rounded-xl shadow-xl border border-purple-600 flex flex-col justify-center items-center p-2"
                            >
                                <input
                                    class="rounded-lg text-lg mb-2 p-2 w-64 border border-blue-700 font-semibold"
                                    v-model="newSceneData.name"
                                />
                                <div
                                    class="input-errors"
                                    v-for="error of errorList"
                                    :key="error.id"
                                >
                                    <div class="error-msg">
                                        {{ error.message }}
                                    </div>
                                </div>
                                <button
                                    class="bg-blue-700 text-white rounded-lg w-64 p-3 mt-4 text-lg font-medium"
                                    @click="createScene(newSceneData.name)"
                                >
                                    Create
                                </button>
                                <button
                                    class="bg-purple-700 text-white rounded-lg w-32 p-3 mt-4 text-md font-medium"
                                    @click="newSceneOpen = false"
                                >
                                    Close
                                </button>
                            </div>
                        </div>
                    </teleport>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import sceneGraph from "../components/sceneGraph.vue";
import { Validate } from "../compositions/inputVal";

const router = useRouter();
const route = useRoute();

const emit = defineEmits(["projectLoaded"]);

const scenes = ref([]);
const name = ref("");
const jumps = ref([]);

const newSceneData = ref({
    name: "newScene",
});
const newSceneOpen = ref(false);
const rules = {
    name: {
        required: true,
        min: 1,
        max: 15,
        alphaNum: true,
    },
};
const errorList = ref([]);

function changeScene(id) {
    router.push({
        name: "sceneEditor",
        params: { projectId: route.params.projectId, sceneId: id },
    });
}

function loadProject(projectId) {
    fetch("http://localhost:5000/project?id=" + projectId)
        .then((response) => {
            if (!response.ok) {
                throw new Error("Request failed");
            }
            return response.json();
        })
        .then((data) => {
            scenes.value = data.scenes;
            name.value = data.projectName;
            jumps.value = data.jumps;
            emit("projectLoaded");
        })
        .catch((error) => console.log(error));
}

async function createScene(name) {
    const result = await Validate({ name: name }, rules);
    if (result.length > 0) {
        console.log("invalid");
        errorList.value = result;
        return;
    }
    const response = await fetch(
        "http://localhost:5000/createScene?projectId=" +
            route.params.projectId +
            "&name=" +
            name
    );
    if (!response.ok) {
        console.log("failed to create scene");
    } else {
        loadProject(route.params.projectId);
        newSceneOpen.value = false;
    }
}

async function deleteScene(id) {
    const response = await fetch(
        "http://localhost:5000/deleteScene?projectId=" +
            route.params.projectId +
            "&id=" +
            id
    );
    if (!response.ok) {
        console.log("failed to create scene");
    } else {
        loadProject(route.params.projectId);
    }
}

onMounted(() => {
    loadProject(route.params.projectId);
    newSceneOpen.value = false;
});
</script>
