<script setup lang="ts">
import { onMounted, ref } from 'vue'
import Splide from '@splidejs/splide'

import Partner1Image from 'assets/images/cl-1.png'
import Partner2Image from 'assets/images/cl-2.png'
import Partner3Image from 'assets/images/cl-3.png'
import Partner4Image from 'assets/images/cl-4.png'
import Partner5Image from 'assets/images/cl-5.png'

const partnerList = ref([
  {
    id: 1,
    image: Partner1Image,
    link: '#'
  },
  {
    id: 2,
    image: Partner5Image,
    link: '#'
  },
  {
    id: 3,
    image: Partner2Image,
    link: '#'
  },
  {
    id: 4,
    image: Partner3Image,
    link: '#'
  },
  {
    id: 5,
    image: Partner4Image,
    link: '#'
  },
  {
    id: 6,
    image: Partner5Image,
    link: '#'
  }
])

onMounted(() => {
  new Splide('#partners-carousel', {
    arrows: false,
    autoplay: true,
    drag: true,
    gap: '2rem',
    pagination: false,
    perPage: 5,
    speed: 3000,
    type: 'loop',
    breakpoints: {
      576: {
        perPage: 2
      },
      768: {
        perPage: 3
      },
      992: {
        perPage: 4
      },
      1200: {
        perPage: 5
      }
    }
  }).mount()
})
</script>

<template>
  <section class="our-partner pb-6 pt-6">
    <div class="container">
      <div class="section-title mb-6 w-75 mx-auto text-center">
        <h4 class="mb-1 theme1">Our Partners</h4>

        <h2 class="mb-1">Our Amazing <span class="theme">Partners</span></h2>

        <p>
          We collaborate with outstanding partners who help us achieve
          excellence and drive innovation across every project.
        </p>
      </div>

      <div
        class="row align-items-center partner-in partner-slider slick-initialized slick-slider"
      >
        <div class="splide" id="partners-carousel" aria-label="Partners">
          <div class="splide__track">
            <ul class="splide__list">
              <li
                class="splide__slide"
                v-for="partner in partnerList"
                :key="partner.id"
              >
                <div tabindex="-1" aria-hidden="true">
                  <div class="partner-item p-4 py-2 rounded bg-lgrey">
                    <img :src="partner.image" alt="" />
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
