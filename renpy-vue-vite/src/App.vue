<template>
<div class="h-screen bg-gray-100">
  <nav class="basis-1/10 bg-white border-gray-200 px-2 sm:px-4 py-2.5 rounded">
    <div class="container flex flex-wrap justify-between items-center mx-auto">
      <div class="flex items-center">
        <span class="self-center text-xl font-semibold whitespace-nowrap">Renpy Vue</span>
      </div>
      <div class="block w-auto">
        <ul class="flex flex-row p-4 mt-4 bg-gray-50 rounded-lg border border-gray-100 space-x-8 mt-0  text-sm font-medium border-0 bg-white">
          <router-link to="/" class="block py-2 pr-4 pl-3 text-white bg-purple-700 rounded bg-transparent p-0">Project View</router-link>
        </ul>
      </div>
    </div>
  </nav>
  <router-view class="h-screen"/>
</div>
</template>
