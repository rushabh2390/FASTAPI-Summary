import { createRouter, createWebHashHistory } from 'vue-router'
import FileUpload from '@/components/FileUpload'

const routes = [
  {
    path: '/',
    name: 'FileUpload',
    component: FileUpload
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
