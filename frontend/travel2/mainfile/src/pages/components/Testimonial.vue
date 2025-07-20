<script setup lang="ts">
import { onMounted, ref } from 'vue'
import Splide, { type Splide as TSplide } from '@splidejs/splide'
import '@splidejs/splide/css'

import TestimonialImage from 'images/testimonial.png'
import TestimonialImage1 from 'images/testimonial/img1.jpg'

const testimonialList = ref([
  {
    id: 1,
    name: 'Emily Carter',
    designation: 'Project Manager',
    image: TestimonialImage1,
    description:
      'Working with this team has been an absolute pleasure. Their dedication and attention to detail helped us deliver our project on time and beyond expectations.'
  },
  {
    id: 2,
    name: 'Daniel Thompson',
    designation: 'Tech Lead',
    image: TestimonialImage,
    description:
      'A highly professional team that understands the importance of quality and collaboration. I would gladly work with them again on future projects.'
  }
])

let splide: TSplide

onMounted(() => {
  splide = new Splide('#testimonial-carousel', {
    arrows: false,
    autoplay: true,
    drag: true,
    gap: '2rem',
    pagination: false,
    perPage: 1,
    speed: 3000,
    type: 'loop'
  }).mount()
})

const prev = () => splide.go('<')

const next = () => splide.go('>')
</script>

<template>
  <section
    class="testimonial pt-9"
    :style="`background-image: url('${TestimonialImage}')`"
  >
    <div class="container">
      <div class="section-title mb-6 text-center w-75 mx-auto">
        <h4 class="mb-1 theme1">Our Testimonails</h4>

        <h2 class="mb-1">
          Good Reviews By
          <span class="theme">Clients</span>
        </h2>

        <p>
          Traveling is not just an escape; it’s an opening to the world. Each destination offers a new culture, unique flavors, and unforgettable encounters. Whether exploring the colorful streets of a historic city or savoring local cuisine in a quaint restaurant, every experience enriches our understanding of life. Allow yourself to be carried away by adventure and discover everything the world has to offer!


        </p>
      </div>

      <div class="row align-items-center">
        <div class="col-lg-5 pe-4">
          <div class="testimonial-image">
            <img src="images/travel2.png" alt="" />
          </div>
        </div>

        <div class="col-lg-7 ps-4">
          <div class="row review-slider slick-initialized slick-slider">
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
              id="testimonial-carousel"
              aria-label="Testimonial"
            >
              <div class="splide__track">
                <ul class="splide__list">
                  <li
                    class="splide__slide"
                    v-for="testimonial in testimonialList"
                    :key="testimonial.id"
                  >
                    <div aria-hidden="true" tabindex="-1">
                      <div class="testimonial-item1 rounded">
                        <div class="author-info d-flex align-items-center mb-4">
                          <img src="images/testimonial/img1.jpg" alt="" />

                          <div class="author-title ms-3">
                            <h5 class="m-0 theme">
                              {{ testimonial.name }}
                            </h5>

                            <span> {{ testimonial.designation }}</span>
                          </div>
                        </div>

                        <div class="details">
                          <p class="m-0">
                            <i class="fa fa-quote-left me-2 fs-1"></i>

                            {{ testimonial.description }}
                          </p>
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
    </div>
  </section>
</template>

<style scoped>
.slick-slider {
  position: relative;
  display: block;
  box-sizing: border-box;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  -webkit-touch-callout: none;
  -khtml-user-select: none;
  -ms-touch-action: pan-y;
  touch-action: pan-y;
  -webkit-tap-highlight-color: transparent;
}

.testimonial .review-slider .slick-prev {
  left: 16px;
}

.testimonial .review-slider .slick-prev,
.testimonial .review-slider .slick-next {
  bottom: -80px;
  top: inherit;
  background: #029e9d;
  border-radius: 50%;
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

.testimonial .review-slider .slick-prev::before,
.testimonial .review-slider .slick-next::before {
  color: #fff;
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

.testimonial .review-slider .slick-prev:hover,
.testimonial .review-slider .slick-prev:focus,
.testimonial .review-slider .slick-next:hover,
.testimonial .review-slider .slick-next:focus {
  background: #17233e;
}
</style>
