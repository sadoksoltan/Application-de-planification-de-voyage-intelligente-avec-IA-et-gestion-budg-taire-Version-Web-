<script setup lang="ts">
import { onMounted, ref } from 'vue'

const preloader = ref(true)
const scrollToTop = ref(false)

onMounted(() => {
  window.addEventListener('scroll', handleScrollToTop)
})

setTimeout(() => {
  preloader.value = false
}, 1000)

function handleScrollToTop() {
  // If user scrolls 1000px, back to top button is shown
  if (window.scrollY > 1000) {
    scrollToTop.value = true
    return
  }

  scrollToTop.value = false
}

function scrollToTopPosition() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}
</script>

<template>
  <div id="preloader" v-if="preloader">
    <div id="status"></div>
  </div>

  <div id="back-to-top" v-show="scrollToTop" @click="scrollToTopPosition">
    <a href="#"></a>
  </div>

  <router-view></router-view>
</template>
