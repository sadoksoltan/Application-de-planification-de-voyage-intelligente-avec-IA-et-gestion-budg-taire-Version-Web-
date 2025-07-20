<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

import BG7Image from 'images/bg/bg7.jpg'

const remainingDays = ref<string | number>('')
const remainingHours = ref<string | number>('')
const remainingMinutes = ref<string | number>('')
const remainingSeconds = ref<string | number>('')

let countDown: NodeJS.Timeout

onMounted(() => {
  countDown = setInterval(startTimer, 1000)
})

onUnmounted(() => {
  clearInterval(countDown)
})

function startTimer() {
  const countDownToTime = ref(new Date('Sep 26, 2026 00:00:00').getTime())

  const timeNow = new Date().getTime()
  const timeDifference = countDownToTime.value - timeNow
  const millisecondsInOneSecond = 1000
  const millisecondsInOneMinute = millisecondsInOneSecond * 60
  const millisecondsInOneHour = millisecondsInOneMinute * 60
  const millisecondsInOneDay = millisecondsInOneHour * 24
  const differenceInDays = timeDifference / millisecondsInOneDay
  const remainderDifferenceInHours =
    (timeDifference % millisecondsInOneDay) / millisecondsInOneHour
  const remainderDifferenceInMinutes =
    (timeDifference % millisecondsInOneHour) / millisecondsInOneMinute
  const remainderDifferenceInSeconds =
    (timeDifference % millisecondsInOneMinute) / millisecondsInOneSecond

  const days = Math.floor(differenceInDays)
  const hours = Math.floor(remainderDifferenceInHours)
  const minutes = Math.floor(remainderDifferenceInMinutes)
  const seconds = Math.floor(remainderDifferenceInSeconds)

  remainingDays.value = days
  remainingHours.value = hours
  remainingMinutes.value = minutes
  remainingSeconds.value = seconds
}
</script>

<template>
  <section
    class="comingsoon d-flex align-items-center"
    :style="{ backgroundImage: `url('${BG7Image}')` }"
  >
    <div class="container">
      <div class="comingsoon-content text-center">
        <div class="coming-title mb-3">
          <div class="logo-main mb-4">
            <img src="images/logo-white.png" alt="" />
          </div>

          <h1 class="white m-0">
            Under <span class="theme1">Construction</span>
          </h1>

          <p class="white m-0">
            Our website is under construction. <br />
            We will be here soon with our awesome new site, subscribe to be
            notified.
          </p>

          <p class="white mt-3">
            We are currently building an international recommendation system
            from scratch to improve your travel experience worldwide.
          </p>
        </div>

        <div class="coming-counter" data-date="2022-12-28 00:00:00">
          <div class="counter-box">
            <span class="days">{{ remainingDays }}</span> Days
          </div>

          <div class="counter-box">
            <span class="hours">{{ remainingHours }}</span> Hours
          </div>

          <div class="counter-box">
            <span class="minutes">{{ remainingMinutes }}</span> Minutes
          </div>

          <div class="counter-box">
            <span class="seconds">{{ remainingSeconds }}</span> Seconds
          </div>
        </div>
      </div>
    </div>

    <div class="overlay"></div>

    <div id="particles-js">
      <canvas
        class="particles-js-canvas-el"
        width="1903"
        height="911"
        style="width: 100%; height: 100%"
      ></canvas>
    </div>
  </section>
</template>

<style scoped>
.comingsoon {
  overflow: hidden;
}
</style>
