import { createRouter, createWebHashHistory } from 'vue-router'
import sceneEditor from '../views/sceneEditor.vue'
import projectView from '../views/projectView.vue'

const routes = [
  {
    path: '/sceneEditor/:id',
    name: 'sceneEditor',
    component: sceneEditor
  },
  {
    path: '/',
    name: 'projectView',
    component: projectView
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
