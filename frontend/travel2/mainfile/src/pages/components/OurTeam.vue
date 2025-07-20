<script setup lang="ts">
import { onMounted, ref } from 'vue'
import Splide from '@splidejs/splide'
import '@splidejs/splide/css'

import TeamImage1 from 'images/team/img1.jpg'
import TeamImage2 from 'images/team/img2.jpg'
import TeamImage3 from 'images/team/img3.jpg'
import TeamImage4 from 'images/team/img4.jpg'

const teamList = ref([
  {
    id: 1,
    name: 'Salmon Thuir',
    designation: 'Senior Agent',
    image: TeamImage1
  },
  {
    id: 2,
    name: 'Horke Pels',
    designation: 'Head Officer',
    image: TeamImage2
  },
  {
    id: 3,
    name: 'Solden Kalos',
    designation: 'Supervisor',
    image: TeamImage3
  },
  {
    id: 4,
    name: 'Nelson Bam',
    designation: 'Quality Assurance',
    image: TeamImage4
  },
  {
    id: 5,
    name: 'Salmon Thuir',
    designation: 'Senior Agent',
    image: TeamImage1
  }
])

onMounted(() => {
  new Splide('#team-list-carousel', {
    arrows: false,
    autoplay: true,
    drag: true,
    gap: '2rem',
    pagination: false,
    perPage: 4,
    speed: 3000,
    type: 'loop',
    breakpoints: {
      576: {
        perPage: 1
      },
      768: {
        perPage: 2
      },
      992: {
        perPage: 3
      },
      1200: {
        perPage: 4
      },
      1400: {
        perPage: 5
      }
    }
  }).mount()
})
</script>

<template>
  <section class="our-team pb-6">
    <div class="container">
      <div class="section-title mb-6 w-75 mx-auto text-center">
        <h4 class="mb-1 theme1">Tour Guides</h4>

        <h2 class="mb-1">Our Amazing <span class="theme">Partners</span></h2>

        <p>
          We collaborate with outstanding partners who help us achieve
          excellence and drive innovation across every project.
        </p>
      </div>

      <div class="team-main">
        <div class="splide" id="team-list-carousel" aria-label="Our Team">
          <div class="splide__track">
            <ul class="splide__list">
              <li class="splide__slide" v-for="team in teamList" :key="team.id">
                <div aria-hidden="true" tabindex="-1" class="team-list rounded">
                  <div class="team-image">
                    <img :src="team.image" alt="team" />
                  </div>

                  <div class="team-content text-center p-3 bg-theme">
                    <h4 class="mb-0 white">{{ team.name }}</h4>

                    <p class="mb-0 white">{{ team.designation }}</p>
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
