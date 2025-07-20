<script setup lang="ts">
import { onMounted, onUnmounted } from 'vue'

import Appbar from './components/Appbar.vue'
import Banner2 from './components/Banner2.vue'
import OurTeam from './components/OurTeam.vue'
import Testimonial from './components/Testimonial.vue'
import Footer from './components/Footer.vue'

import BackgroundPatternImage from 'images/background_pattern.png'
import Shape8Image from 'images/shape8.png'

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
  <Appbar />

  <Banner2 page-title="About Us" />

  <section
    class="about-us pt-6"
    style="background-position: bottom right"
    :style="{ backgroundImage: `url('${BackgroundPatternImage}')` }"
  >
    <div class="container">
      <div class="about-image-box">
        <div class="row d-flex align-items-center justify-content-between">
          <div class="col-lg-6 ps-4">
            <div class="about-content text-center text-lg-start">
              <h4 class="theme d-inline-block mb-0">Get To Know Us</h4>

              <h2 class="border-b mb-2 pb-1">
                Explore All Tour of the world with us.
              </h2>

              <p class="border-b mb-2 pb-2">
                Traveling is not just an escape; it’s an opening to the world.
                Each destination offers a new culture, unique flavors, and
                unforgettable encounters. Whether exploring the colorful streets
                of a historic city or savoring local cuisine in a quaint
                restaurant, every experience enriches our understanding of life.
                Allow yourself to be carried away by adventure and discover
                everything the world has to offer!
              </p>

              <div class="about-listing">
                <ul class="d-flex justify-content-between">
                  <li><i class="icon-location-pin theme"></i> Tour Guide</li>
                  <li><i class="icon-briefcase theme"></i> Friendly Price</li>
                  <li>
                    <i class="icon-folder theme"></i> Reliable Tour Package
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <div class="col-lg-6 mb-4 pe-4">
            <div
              class="about-image"
              style="animation: none; background: transparent"
            >
              <img src="images/travel.png" alt="" />
            </div>
          </div>

          <div class="col-lg-12">
            <div
              class="counter-main w-75 float-start z-index3 position-relative"
            >
              <div
                class="counter p-4 pb-0 box-shadow bg-white rounded mt-minus"
              >
                <div class="row" id="counter-section">
                  <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
                    <div class="counter-item border-end pe-4">
                      <div class="counter-content">
                        <h2 class="value mb-0 theme" id="counter1"></h2>
                        <span class="m-0">Years Experiences</span>
                      </div>
                    </div>
                  </div>

                  <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
                    <div class="counter-item border-end pe-4">
                      <div class="counter-content">
                        <h2 class="value mb-0 theme" id="counter2"></h2>
                        <span class="m-0">Tour Packages</span>
                      </div>
                    </div>
                  </div>

                  <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
                    <div class="counter-item border-end pe-4">
                      <div class="counter-content">
                        <h2 class="value mb-0 theme" id="counter3"></h2>
                        <span class="m-0">Happy Customers</span>
                      </div>
                    </div>
                  </div>

                  <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
                    <div class="counter-item">
                      <div class="counter-content">
                        <h2 class="value mb-0 theme" id="counter4"></h2>
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

  <section class="about-us pb-0">
    <div
      class="section-shape section-shape1"
      :style="{ backgroundImage: `url('${Shape8Image}')` }"
    ></div>

    <div class="container">
      <div class="section-title mb-6 w-50 mx-auto text-center">
        <h4 class="mb-1 theme1">Core Features</h4>

        <h2 class="mb-1">Find <span class="theme">Travel Perfection</span></h2>

        <p>
          Explore new horizons, embrace different cultures, and create
          unforgettable memories.
        </p>
      </div>

      <div class="why-us">
        <div class="why-us-box">
          <div class="row">
            <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
              <div class="why-us-item p-5 pt-6 pb-6 border rounded bg-white">
                <div class="why-us-content">
                  <div class="why-us-icon mb-1">
                    <i class="icon-flag theme"></i>
                  </div>

                  <h4>
                    <router-link to="/about">
                      Tell Us What You want To Do
                    </router-link>
                  </h4>

                  <p class="mb-2">
                    Explore new horizons, embrace different cultures, and create
                    unforgettable memories.
                  </p>

                  <p class="mb-0 theme">100+ Reviews</p>
                </div>
              </div>
            </div>

            <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
              <div class="why-us-item p-5 pt-6 pb-6 border rounded bg-white">
                <div class="why-us-content">
                  <div class="why-us-icon mb-1">
                    <i class="icon-location-pin theme"></i>
                  </div>

                  <h4>
                    <router-link to="/about">
                      Share Your Travel Locations
                    </router-link>
                  </h4>

                  <p class="mb-2">
                    Explore new horizons, embrace different cultures, and create
                    unforgettable memories.
                  </p>

                  <p class="mb-0 theme">100+ Reviews</p>
                </div>
              </div>
            </div>

            <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
              <div class="why-us-item p-5 pt-6 pb-6 border rounded bg-white">
                <div class="why-us-content">
                  <div class="why-us-icon mb-1">
                    <i class="icon-directions theme"></i>
                  </div>

                  <h4>
                    <router-link to="/about">
                      Share Your Travel Preference
                    </router-link>
                  </h4>

                  <p class="mb-2">
                    Explore new horizons, embrace different cultures, and create
                    unforgettable memories.
                  </p>

                  <p class="mb-0 theme">100+ Reviews</p>
                </div>
              </div>
            </div>

            <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
              <div class="why-us-item p-5 pt-6 pb-6 border rounded bg-white">
                <div class="why-us-content">
                  <div class="why-us-icon mb-1">
                    <i class="icon-compass theme"></i>
                  </div>

                  <h4>
                    <router-link to="/about">
                      Here 100% Trusted Tour Agency
                    </router-link>
                  </h4>

                  <p class="mb-2">
                    Explore new horizons, embrace different cultures, and create
                    unforgettable memories.
                  </p>

                  <p class="mb-0 theme">100+ Reviews</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <OurTeam />

  <Testimonial />

  <Footer />
</template>
