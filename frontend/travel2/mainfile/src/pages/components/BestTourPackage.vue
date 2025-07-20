<script setup lang="ts">
import { onMounted, ref } from 'vue'
import Splide, { type Splide as TSplide } from '@splidejs/splide'
import '@splidejs/splide/css'

import Trending1Image from 'images/trending/trending1.jpg'
import Trending2Image from 'images/trending/trending2.jpg'
import Trending3Image from 'images/trending/trending3.jpg'

let splide: TSplide

const tourpackagesList = ref([
  {
    id: 1,
    days: 9,
    location: 'Piazza castello',
    image: Trending2Image,
    name: 'Crotia',
    review_count: 12,
    description:
      'Explore new horizons, embrace different cultures, and create unforgettable memories.',
    price: 170
  },
  {
    id: 2,
    days: 9,
    location: 'Greece',
    image: Trending1Image,
    name: 'Santorini, Oia',
    review_count: 38,
    description:
      'Explore new horizons, embrace different cultures, and create unforgettable memories.',
    price: 180
  },
  {
    id: 3,
    days: 9,
    location: 'Maldives',
    image: Trending3Image,
    name: 'Hurawalhi Island',
    review_count: 18,
    description:
      'Explore new horizons, embrace different cultures, and create unforgettable memories.',
    price: 260
  },

  {
    id: 4,
    days: 9,
    location: 'Greece',
    image: Trending1Image,
    name: 'Santorini, Oia',
    review_count: 38,
    description:
      'Explore new horizons, embrace different cultures, and create unforgettable memories.',
    price: 180
  }
])

onMounted(() => {
  splide = new Splide('#tour-package-carousel', {
    arrows: false,
    autoplay: true,
    drag: true,
    gap: '2rem',
    pagination: false,
    perPage: 3,
    speed: 1500,
    type: 'loop',
    breakpoints: {
      768: {
        perPage: 1
      },
      992: {
        perPage: 2
      },
      1200: {
        perPage: 3
      }
    }
  }).mount()
})

const prev = () => splide.go('<')

const next = () => splide.go('>')
</script>

<template>
  <section class="trending pb-0">
    <div class="container">
      <div class="row align-items-center justify-content-between mb-6">
        <div class="col-lg-7">
          <div class="section-title text-center text-lg-start">
            <h4 class="mb-1 theme1">Top Pick</h4>

            <h2 class="mb-1">
              Best
              <span class="theme">Tour Packages</span>
            </h2>

            <p>
              Explore new horizons, embrace different cultures, and create
              unforgettable memories.
            </p>
          </div>
        </div>

        <div class="col-lg-5"></div>
      </div>

      <div class="trend-box">
        <div class="row item-slider slick-initialized slick-slider">
          <button
            class="slick-prev slick-arrow d-none d-lg-block"
            aria-label="Previous"
            type="button"
            @click="prev"
          >
            Previous
          </button>

          <div
            class="splide"
            id="tour-package-carousel"
            aria-label="Best Tour Packages"
          >
            <div class="splide__track">
              <ul class="splide__list">
                <li
                  class="splide__slide"
                  v-for="tour in tourpackagesList"
                  :key="tour.id"
                >
                  <div aria-hidden="true" tabindex="-1">
                    <div class="trend-item box-shadow rounded">
                      <div class="trend-image position-relative">
                        <img :src="tour.image" alt="image" />

                        <div class="color-overlay"></div>
                      </div>

                      <div class="trend-content p-4 pt-5 position-relative">
                        <div
                          class="trend-meta bg-theme white px-3 py-2 rounded"
                        >
                          <div class="entry-author">
                            <i class="icon-calendar"></i>

                            <span class="fw-bold ms-1">
                              {{ tour.days }} Days Tour
                            </span>
                          </div>
                        </div>

                        <h5 class="theme mb-1">
                          <i class="flaticon-location-pin"></i>
                          {{ tour.location }}
                        </h5>

                        <h3 class="mb-1">
                          <router-link to="/tour-grid" tabindex="-1">
                            {{ tour.name }}
                          </router-link>
                        </h3>

                        <div class="rating-main d-flex align-items-center pb-2">
                          <div class="rating d-flex gap-1">
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star checked"></span>
                            <span class="fa fa-star checked"></span>
                          </div>

                          <span class="ms-2">({{ tour.review_count }})</span>
                        </div>

                        <p class="border-b pb-2 mb-2">
                          Explore new horizons, embrace different cultures, and
                          create unforgettable memories.
                        </p>

                        <div class="entry-meta">
                          <div class="entry-author d-flex align-items-center">
                            <p class="mb-0">
                              <span class="theme fw-bold fs-5">
                                ${{ tour.price }}
                              </span>
                              | Per person
                            </p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>

          <button
            class="slick-next slick-arrow d-none d-lg-block"
            aria-label="Next"
            type="button"
            @click="next"
          >
            Next
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.slick-slider {
  position: relative;
}

.item-slider .slick-prev,
.item-slider .slick-next {
  top: -124px;
  background: #fff;
  border-radius: 5px;
  border: 1px solid #f1f1f1;
  width: 50px;
  height: 50px;
  line-height: 1;
}

.slick-prev,
.slick-next {
  font-size: 0;
  line-height: 0;
  position: absolute;
  top: 50%;
  display: block;
  width: 40px;
  height: 40px;
  margin-top: -20px;
  padding: 0;
  cursor: pointer;
  color: transparent;
  border: none;
  outline: none;
  background: #e29f12;
  line-height: 40px;
  z-index: 1;
  transition: all ease-in-out 0.3s;
}

.item-slider .slick-prev::before,
.item-slider .slick-next::before {
  color: #777;
  font-size: 28px;
  line-height: 1.5;
}

.slick-prev:before {
  content: '\f104';
}

.slick-prev:before,
.slick-next:before {
  font-family: 'fontawesome';
  font-size: 21px !important;
  line-height: 2;
  opacity: 1;
  color: #fff;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.slick-next:before {
  content: '\f105';
}

.item-slider .slick-prev:hover,
.item-slider .slick-prev:focus,
.item-slider .slick-next:hover,
.item-slider .slick-next:focus {
  background: #029e9d;
  border-color: #029e9d;
}

.slick-prev:hover:before,
.slick-next:hover::before {
  color: white;
}

.slick-prev:focus:before,
.slick-next:focus::before {
  color: white;
}
</style>
