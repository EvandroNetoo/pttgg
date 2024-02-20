import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/summoner/:region/:gameNameTagLine/',
      name: 'summoner',
      component:  () => import('../views/Summoner.vue')
    },
  ]
})

export default router
