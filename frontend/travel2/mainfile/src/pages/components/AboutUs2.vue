<script setup lang="ts">
import { onMounted, onUnmounted } from 'vue'

import Shape4Image from 'images/bg/bg-trans.png'

type TCounter = {
  element: HTMLElement | null
  targetValue: number
}

let counters: TCounter[] = []
const duration = 10000
const intervalTime = 20
let startTime = 0

let counterSection: HTMLElement | null
let observer: IntersectionObserver

onMounted(() => {
  counters = [
    { element: document.getElementById('counter1'), targetValue: 20 },
    { element: document.getElementById('counter2'), targetValue: 530 },
    { element: document.getElementById('counter3'), targetValue: 850 },
    { element: document.getElementById('counter4'), targetValue: 320 }
  ]

  observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          startTime = 0
          requestAnimationFrame(animateCount)
        }
      })
    },
    { threshold: 0.5 }
  )

  counterSection = document.getElementById('counter-section')
  observer.observe(counterSection!)
})

onUnmounted(() => {
  observer.unobserve(counterSection!)
})

function animateCount(timestamp: number) {
  if (!startTime) {
    startTime = timestamp
  }

  const elapsedTime = timestamp - startTime

  counters.forEach((counter) => {
    const increment = counter.targetValue / (duration / intervalTime)
    const currentValue = Math.min(counter.targetValue, increment * elapsedTime)

    if (counter.element) {
      counter.element.textContent = Math.round(currentValue).toString()
    }
  })

  if (elapsedTime < duration) {
    requestAnimationFrame(animateCount)
  } else {
    counters.forEach((counter) => {
      if (counter.element) {
        counter.element.textContent = counter.targetValue.toString()
      }
    })
  }
}
</script>

<template>
  <section
    class="about-us pt-0"
    :style="`background-image: url('${Shape4Image}')`"
  >
    <div class="container">
      <div class="about-image-box">
        <div class="row d-flex align-items-center justify-content-between">
          <div class="col-lg-6 mb-4 pe-4">
            <div class="about-image overflow-hidden">
              <img src="images/travel1.png" alt="" />
            </div>
          </div>

          <div class="col-lg-6 mb-4 ps-4">
            <div class="about-content text-center text-lg-start mb-4">
              <h4 class="theme d-inline-block mb-0">Get To Know Us</h4>

              <h2 class="border-b mb-2 pb-1">
                Explore All Tour of the world with us.
              </h2>

              <p class="border-b mb-2 pb-2">
                Explore new horizons, embrace different cultures, and create
                unforgettable memories.
              </p>

              <div class="about-listing">
                <ul class="d-flex justify-content-between">
                  <li>
                    <i class="icon-location-pin theme"></i>
                    Tour Guide
                  </li>

                  <li>
                    <i class="icon-briefcase theme"></i>
                    Friendly Price
                  </li>

                  <li>
                    <i class="icon-folder theme"></i>
                    Reliable Tour Package
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <div class="col-lg-12" id="counter-section">
            <div class="counter-main w-75 float-end">
              <div class="counter p-4 pb-0 box-shadow bg-white rounded">
                <div class="row">
                  <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
                    <div class="counter-item border-end pe-4">
                      <div class="counter-content">
                        <h2 class="value mb-0 theme" id="counter1">20</h2>
                        <span class="m-0">Years Experiences</span>
                      </div>
                    </div>
                  </div>

                  <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
                    <div class="counter-item border-end pe-4">
                      <div class="counter-content">
                        <h2 class="value mb-0 theme" id="counter2">530</h2>
                        <span class="m-0">Tour Packages</span>
                      </div>
                    </div>
                  </div>

                  <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
                    <div class="counter-item border-end pe-4">
                      <div class="counter-content">
                        <h2 class="value mb-0 theme" id="counter3">850</h2>
                        <span class="m-0">Happy Customers</span>
                      </div>
                    </div>
                  </div>

                  <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
                    <div class="counter-item">
                      <div class="counter-content">
                        <h2 class="value mb-0 theme" id="counter4">320</h2>
                        <span class="m-0">Award Winning</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="white-overlay"></div>
  </section>
</template>
