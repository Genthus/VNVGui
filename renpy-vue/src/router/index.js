import { createRouter, createWebHashHistory } from 'vue-router'
import sceneEditor from '../views/sceneEditor.vue'
import projectView from '../views/projectView.vue'
import projectManager from '../views/projectManager.vue'

const routes = [
  {
    path: '/sceneEditor/:id',
    name: 'sceneEditor',
    component: sceneEditor
  },
  {
    path: '/projects',
    name: 'projectManager',
    component: projectManager
  },
  {
    path: '/project/:id',
    name: 'projectView',
    component: projectView
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
