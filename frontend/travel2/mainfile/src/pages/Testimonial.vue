<script setup lang="ts">
import { onMounted } from 'vue'
import Splide, { type Splide as TSplide } from '@splidejs/splide'
import '@splidejs/splide/css'

import Appbar from 'pages/components/Appbar.vue'
import Banner2 from 'pages/components/Banner2.vue'
import OurTestimonial from 'pages/components/Testimonial.vue'
import DiscountAction from 'pages/components/DiscountAction.vue'
import Footer from 'pages/components/Footer.vue'

import BG1Image from 'images/bg/bg1.jpg'
import TestimonialImage from 'images/testimonial.png'

let splide: TSplide

onMounted(() => {
  new Splide('#testimonial-carousel-1', {
    arrows: false,
    autoplay: true,
    drag: true,
    gap: '2rem',
    interval: 7000,
    pagination: false,
    perPage: 1,
    speed: 5000,
    type: 'loop'
  }).mount()

  splide = new Splide('#testimonial-carousel-2', {
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
  <Appbar />

  <Banner2 page-title="Testimonials" />

  <OurTestimonial />

  <section
    class="testimonial pt-10"
    :style="{ backgroundImage: `url('${BG1Image}')` }"
  >
    <div class="container">
      <div class="testimonial-in">
        <div class="row align-items-center">
          <div class="col-lg-5">
            <div class="section-title">
              <h4 class="mb-1 theme1">Our Testimonails</h4>

              <h2 class="mb-1 white">
                Good Reviews By
                <span class="theme">Clients</span>
              </h2>

              <p class="mb-0 white">
                Explore new horizons, embrace different cultures, and create
                unforgettable memories.
              </p>
            </div>
          </div>

          <div class="col-lg-7">
            <div class="row about-slider">
              <div
                class="splide"
                id="testimonial-carousel-1"
                aria-label="Testimonial"
              >
                <div class="splide__track">
                  <ul class="splide__list">
                    <li class="splide__slide">
                      <div tabindex="-1" aria-hidden="true">
                        <div class="testimonial-item1">
                          <div class="details d-flex">
                            <i class="fa fa-quote-left fs-1 mb-0"></i>
                            <div class="author-content ms-4">
                              <p class="mb-4 white fs-5 fw-normal">
                                Discover the beauty of the world around you,
                                immerse yourself in diverse cultures, and create
                                lasting memories through your travels. Embrace
                                every moment as an opportunity for growth and
                                adventure.
                              </p>

                              <div
                                class="author-info d-flex align-items-center"
                              >
                                <a href="#" tabindex="-1">
                                  <img
                                    src="images/testimonial/img3.jpg"
                                    alt=""
                                  />
                                </a>

                                <div class="author-title ms-3">
                                  <h5 class="m-0">
                                    <a href="#" class="theme1" tabindex="-1">
                                      Jared Erondu
                                    </a>
                                  </h5>

                                  <span class="white">Supervisor</span>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </li>

                    <li class="splide__slide">
                      <div tabindex="-1" aria-hidden="true">
                        <div class="testimonial-item1">
                          <div class="details d-flex">
                            <i class="fa fa-quote-left fs-1 mb-0"></i>
                            <div class="author-content ms-4">
                              <p class="mb-4 white fs-5 fw-normal">
                                Discover the beauty of the world around you,
                                immerse yourself in diverse cultures, and create
                                lasting memories through your travels. Embrace
                                every moment as an opportunity for growth and
                                adventure.
                              </p>

                              <div
                                class="author-info d-flex align-items-center"
                              >
                                <a href="#" tabindex="-1">
                                  <img
                                    src="images/testimonial/img3.jpg"
                                    alt=""
                                  />
                                </a>

                                <div class="author-title ms-3">
                                  <h5 class="m-0">
                                    <a href="#" class="theme1" tabindex="-1">
                                      Jared Erondu
                                    </a>
                                  </h5>

                                  <span class="white">Supervisor</span>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="dot-overlay"></div>
  </section>

  <section
    class="testimonial pb-0"
    :style="{ backgroundImage: `url('${TestimonialImage}')` }"
  >
    <div class="container">
      <div class="section-title mb-6 text-center w-75 mx-auto">
        <h4 class="mb-1 theme1">Our Testimonails</h4>

        <h2 class="mb-1">
          Good Reviews By
          <span class="theme">Clients</span>
        </h2>

        <p>
          Discover the beauty of the world around you, immerse yourself in
          diverse cultures, and create lasting memories through your travels.
          Embrace every moment as an opportunity for growth and adventure.
        </p>
      </div>

      <div class="row align-items-center">
        <div class="col-lg-7 pe-lg-4">
          <div class="row review-slider slick-initialized slick-slider">
            <button
              type="button"
              aria-label="Previous"
              class="slick-prev slick-arrow d-none d-lg-block"
              @click="prev"
            >
              Previous
            </button>

            <div
              class="splide"
              aria-label="Testimonial"
              id="testimonial-carousel-2"
            >
              <div class="splide__track">
                <ul class="splide__list">
                  <li class="splide__slide">
                    <div aria-hidden="true" tabindex="-1">
                      <div class="testimonial-item1 rounded">
                        <div class="author-info d-flex align-items-center mb-4">
                          <a href="#" tabindex="-1">
                            <img src="images/testimonial/img1.jpg" alt="" />
                          </a>

                          <div class="author-title ms-3">
                            <h5 class="m-0 theme">Jared Erondu</h5>

                            <span>Supervisor</span>
                          </div>
                        </div>

                        <div class="details">
                          <p class="m-0">
                            <i class="fa fa-quote-left me-2 fs-1"></i>

                            Traveling is not just an escape; it’s an opening to
                            the world. Each destination offers a new culture,
                            unique flavors, and unforgettable encounters.
                            Whether exploring the colorful streets of a historic
                            city or savoring local cuisine in a quaint
                            restaurant, every experience enriches our
                            understanding of life. Allow yourself to be carried
                            away by adventure and discover everything the world
                            has to offer!
                          </p>
                        </div>
                      </div>
                    </div>
                  </li>

                  <li class="splide__slide">
                    <div aria-hidden="true" tabindex="-1">
                      <div class="testimonial-item1 rounded">
                        <div class="author-info d-flex align-items-center mb-4">
                          <a href="#" tabindex="-1">
                            <img src="images/testimonial/img1.jpg" alt="" />
                          </a>

                          <div class="author-title ms-3">
                            <h5 class="m-0 theme">Jared Erondu</h5>

                            <span>Supervisor</span>
                          </div>
                        </div>

                        <div class="details">
                          <p class="m-0">
                            <i class="fa fa-quote-left me-2 fs-1"></i>

                            Traveling is not just an escape; it’s an opening to
                            the world. Each destination offers a new culture,
                            unique flavors, and unforgettable encounters.
                            Whether exploring the colorful streets of a historic
                            city or savoring local cuisine in a quaint
                            restaurant, every experience enriches our
                            understanding of life. Allow yourself to be carried
                            away by adventure and discover everything the world
                            has to offer!
                          </p>
                        </div>
                      </div>
                    </div>
                  </li>
                </ul>
              </div>
            </div>

            <button
              type="button"
              aria-label="Next"
              class="slick-next slick-arrow d-none d-lg-block"
              @click="next"
            >
              Next
            </button>
          </div>
        </div>

        <div class="col-lg-5 ps-lg-4">
          <div class="testimonial-image">
            <img src="images/testi.png" alt="" />
          </div>
        </div>
      </div>
    </div>
  </section>

  <DiscountAction />
  <Footer />
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
