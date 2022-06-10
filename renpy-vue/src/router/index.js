import { createRouter, createWebHashHistory } from 'vue-router'
import sceneEditor from '../views/sceneEditor.vue'
import projectView from '../views/projectView.vue'
import projectManager from '../views/projectManager.vue'

const routes = [
  {
    path: '/projects',
    name: 'projectManager',
    component: projectManager
  },
  {
    path: '/project/:projectId',
    name: 'projectView',
    component: projectView,
  },
  {
    path: '/project/:projectId/sceneEditor/:sceneId',
    name: 'sceneEditor',
    component: sceneEditor
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
