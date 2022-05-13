import { createRouter, createWebHashHistory } from 'vue-router'
import sceneEditor from '../views/sceneEditor.vue'

const routes = [
  {
    path: '/',
    name: 'sceneEditor',
    component: sceneEditor
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
