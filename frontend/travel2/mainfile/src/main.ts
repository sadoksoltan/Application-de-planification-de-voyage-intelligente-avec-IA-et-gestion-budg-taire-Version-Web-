import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import { routes } from './router/index'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'
import './smooth.js'
import './style.css'
import App from './App.vue'
import 'vue-toastification/dist/index.css'
const router = createRouter({
  history: createWebHistory(),
  routes,
  // @ts-ignore
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }
  }
})

router.afterEach(() => {
  document.body.classList.remove('modal-open')
  document.body.style.overflow = 'auto'
  document.body.style.paddingRight = ''
  document.querySelectorAll('.modal-backdrop').forEach((el) => el.remove())
})

createApp(App).use(router).mount('#app')
