<script setup lang="ts">
import { onMounted, ref } from 'vue'
import Splide from '@splidejs/splide'
import '@splidejs/splide/css'

import InstagramImage1 from 'images/insta/ins-1.jpg'
import InstagramImage2 from 'images/insta/ins-2.jpg'
import InstagramImage3 from 'images/insta/ins-3.jpg'
import InstagramImage4 from 'images/insta/ins-4.jpg'
import InstagramImage5 from 'images/insta/ins-5.jpg'
import InstagramImage6 from 'images/insta/ins-6.jpg'
import InstagramImage7 from 'images/insta/ins-7.jpg'
import InstagramImage8 from 'images/insta/ins-8.jpg'
import InstagramImage9 from 'images/insta/ins-9.jpg'
import InstagramImage10 from 'images/insta/ins-10.jpg'
import BackgroundPatternImage from 'images/background_pattern.png'
import Shape8Image from 'images/shape8.png'

const instagramPhotoList = ref([
  {
    id: 1,
    image: InstagramImage1
  },
  {
    id: 2,
    image: InstagramImage2
  },
  {
    id: 3,
    image: InstagramImage3
  },
  {
    id: 4,
    image: InstagramImage4
  },
  {
    id: 5,
    image: InstagramImage5
  },
  {
    id: 6,
    image: InstagramImage6
  },
  {
    id: 7,
    image: InstagramImage7
  },
  {
    id: 8,
    image: InstagramImage8
  },
  {
    id: 9,
    image: InstagramImage9
  },
  {
    id: 10,
    image: InstagramImage10
  }
])

onMounted(() => {
  new Splide('#footer-instagram-carousel', {
    arrows: false,
    autoplay: true,
    drag: true,
    gap: '2rem',
    pagination: false,
    perPage: 8,
    speed: 1500,
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
  <footer
    class="pt-20 pb-4"
    :style="`background-image: url('${BackgroundPatternImage}')`"
  >
    <div
      class="section-shape top-0"
      :style="`background-image: url('${Shape8Image}')`"
    ></div>

    <div class="insta-main pb-10">
      <div class="container">
        <div class="insta-inner">
          <div class="follow-button">
            <h5 class="m-0 rounded">
              <i class="fab fa-instagram"></i> Follow on Instagram
            </h5>
          </div>

          <div
            class="splide"
            id="footer-instagram-carousel"
            aria-label="Instagram Photos"
          >
            <div class="splide__track">
              <ul class="splide__list">
                <li
                  class="splide__slide"
                  v-for="photos in instagramPhotoList"
                  :key="photos.id"
                >
                  <div aria-hidden="true" tabindex="-1">
                    <div class="insta-image rounded">
                      <router-link to="/gallery1" tabindex="-1">
                        <img :src="photos.image" alt="insta" />
                      </router-link>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-upper pb-4">
      <div class="container">
        <div class="row">
          <div class="col-lg-4 col-md-6 col-sm-12 mb-4 pe-4">
            <div class="footer-about">
              <img src="images/logo-white.png" alt="" />

              <p class="mt-3 mb-3 white">
                Traveling is not just an escape; it’s an opening to the world.
                Each destination offers a new culture, unique flavors, and
                unforgettable encounters. Whether exploring the colorful streets
                of a historic city or savoring local cuisine in a quaint
                restaurant, every experience enriches our understanding of life.
                Allow yourself to be carried away by adventure and discover
                everything the world has to offer!
              </p>

              <ul>
                <li class="white"><strong>PO Box:</strong> +216 ** *** ***</li>

                <li class="white">
                  <strong>Location:</strong> Monastir, Tunisia
                </li>

                <li class="white">
                  <strong>Email:</strong> soltansadok3@gmail.com
                </li>

                <li class="white"><strong>Website:</strong> *********</li>
              </ul>
            </div>
          </div>

          <div class="col-lg-2 col-md-6 col-sm-12 mb-4">
            <div class="footer-links">
              <h3 class="white">Quick link</h3>

              <ul>
                <li>
                  <router-link to="/about">About Us</router-link>
                </li>

                <li>
                  <a href="#">Delivery Information</a>
                </li>

                <li>
                  <a href="#">Privacy Policy</a>
                </li>

                <li>
                  <a href="#">Terms &amp; Conditions</a>
                </li>

                <li>
                  <a href="#">Customer Service</a>
                </li>

                <li>
                  <a href="#">Return Policy</a>
                </li>
              </ul>
            </div>
          </div>

          <div class="col-lg-2 col-md-6 col-sm-12 mb-4">
            <div class="footer-links">
              <h3 class="white">Categories</h3>

              <ul>
                <li>
                  <a href="#">Travel</a>
                </li>

                <li>
                  <a href="#">Technology</a>
                </li>

                <li>
                  <a href="#">Lifestyle</a>
                </li>

                <li>
                  <a href="#">Destinations</a>
                </li>

                <li>
                  <a href="#">Entertainment</a>
                </li>

                <li>
                  <a href="#">Business</a>
                </li>
              </ul>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 col-sm-12 mb-4">
            <div class="footer-links">
              <h3 class="white">Newsletter</h3>
              <div class="newsletter-form">
                <p class="mb-3">
                  Join our community of over 200,000 global readers who receives
                  emails filled with news, promotions, and other good stuff.
                </p>

                <form
                  action="#"
                  method="get"
                  accept-charset="utf-8"
                  class="border-0 d-flex align-items-center"
                  @submit.prevent="() => {}"
                >
                  <input type="text" placeholder="Email Address" />

                  <button class="nir-btn ms-2">Subscribe</button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-payment">
      <div class="container">
        <div
          class="row footer-pay align-items-center justify-content-between text-lg-start text-center"
        >
          <div class="col-lg-8 footer-payment-nav mb-4">
            <ul>
              <li class="me-2">We Support:</li>

              <li class="me-2">
                <i class="fab fa-cc-mastercard fs-4"></i>
              </li>

              <li class="me-2">
                <i class="fab fa-cc-paypal fs-4"></i>
              </li>

              <li class="me-2">
                <i class="fab fa-cc-stripe fs-4"></i>
              </li>

              <li class="me-2">
                <i class="fab fa-cc-visa fs-4"></i>
              </li>

              <li class="me-2">
                <i class="fab fa-cc-discover fs-4"></i>
              </li>
            </ul>
          </div>

          <div class="col-lg-4 footer-payment-nav mb-4">
            <ul class="d-flex align-items-center">
              <li class="me-2 w-75 input-box">
                <select>
                  <option>English</option>
                  <option>Tunisien</option>
                  <option>Russian</option>
                  <option>Japanese</option>
                  <option>Korean</option>
                </select>
              </li>

              <li class="w-25 input-box">
                <select>
                  <option>$ USD</option>
                  <option>$ TND</option>
                  <option>$ YEN</option>
                  <option>$ IN</option>
                  <option>$ NP</option>
                </select>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-copyright">
      <div class="container">
        <div
          class="copyright-inner rounded p-3 d-md-flex align-items-center justify-content-between"
        >
          <div class="copyright-text">
            <p class="m-0 white">
              {{ new Date().getFullYear() }}
              Travelin. All rights reserved.
            </p>
          </div>

          <div class="social-links">
            <ul class="d-flex gap-1">
              <li>
                <a href="#">
                  <i class="fab fa-facebook" aria-hidden="true"></i>
                </a>
              </li>

              <li>
                <a href="#">
                  <i class="fab fa-twitter" aria-hidden="true"></i>
                </a>
              </li>

              <li>
                <a href="#">
                  <i class="fab fa-instagram" aria-hidden="true"></i>
                </a>
              </li>

              <li>
                <a href="#">
                  <i class="fab fa-linkedin" aria-hidden="true"></i>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <div id="particles-js">
      <canvas
        class="particles-js-canvas-el"
        width="1903"
        height="1717"
        style="width: 100%; height: 100%"
      ></canvas>
    </div>
  </footer>
</template>

<style scoped>
select {
  appearance: none;
  -moz-appearance: none;
  -webkit-appearance: none;
}

.input-box {
  position: relative;
}

.input-box::after {
  position: absolute;
  top: 55%;
  right: 1px;
  pointer-events: none;
  content: url('../../assets/chevron-down.svg');
  transform: translate(-50%, -50%);
}
</style>
