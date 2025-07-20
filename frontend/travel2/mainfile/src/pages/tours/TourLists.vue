<script setup lang="ts">
import { onMounted, ref } from 'vue'
import Splide from '@splidejs/splide'
import '@splidejs/splide/css'

import Appbar from 'pages/components/Appbar.vue'
import Banner2 from 'pages/components/Banner2.vue'
import DiscountAction from 'pages/components/DiscountAction.vue'
import Footer from 'pages/components/Footer.vue'
import axios from '@/axios'

import Destination10Image from 'images/destination/destination10.jpg'
import Destination11Image from 'images/destination/destination11.jpg'
import Destination12Image from 'images/destination/destination12.jpg'
import Destination13Image from 'images/destination/destination13.jpg'
import Destination14Image from 'images/destination/destination14.jpg'
import Destination15Image from 'images/destination/destination15.jpg'
import Destination17Image from 'images/destination/destination17.jpg'

interface Tour {
  id: number
  title: string
  location: string
  reviews: number
  price: number
  image: string
}

const tourList = ref<Tour[]>([
  {
    id: 1,
    title: 'Leeds Castle, Cliffs of Dover',
    location: 'Crotia',
    reviews: 200,
    price: 200,
    image: Destination17Image
  },
  {
    id: 2,
    title: 'Adriatic Adventure-Zagreb To Athens',
    location: 'Greece',
    reviews: 200,
    price: 200,
    image: Destination15Image
  },
  {
    id: 3,
    title: 'The Spanish Riviera Cost Bay',
    location: 'Spain',
    reviews: 200,
    price: 200,
    image: Destination11Image
  },
  {
    id: 4,
    title: 'Adriatic Adventure-Zagreb To Athens',
    location: 'Grrece',
    reviews: 200,
    price: 200,
    image: Destination12Image
  },
  {
    id: 5,
    title: 'Highlights scenery of Vietnam',
    location: 'Vitenam',
    reviews: 200,
    price: 200,
    image: Destination13Image
  },
  {
    id: 6,
    title: 'The Spanish Riviera Cost Bay',
    location: 'Spain',
    reviews: 200,
    price: 200,
    image: Destination10Image
  },
  {
    id: 7,
    title: ' Empire Prestige Causeway Bay',
    location: 'Egypt',
    reviews: 200,
    price: 200,
    image: Destination14Image
  }
])

// Ajout dynamique des tours depuis l'API
const apiTours = ref<Tour[]>([])
const loading = ref(true)

// Utilise l'URL complète du backend pour les images dynamiques
const API_BASE_URL = 'http://localhost:8000'

const fetchTours = async () => {
  loading.value = true
  try {
    const { data } = await axios.get('/api/tours')
    apiTours.value = data
  } catch (e) {
    apiTours.value = []
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchTours()
  new Splide('#destination-carousel', {
    arrows: false,
    autoplay: true,
    drag: true,
    gap: '2rem',
    interval: 7000,
    pagination: false,
    perPage: 1,
    speed: 3000,
    type: 'loop'
  }).mount()
})
</script>

<template>
  <Appbar />

  <Banner2 page-title="Tour Lists Leftside" headline="Tour List" />

  <section class="trending pt-6 pb-0 bg-lgrey">
    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <div
            class="list-results d-flex align-items-center justify-content-between"
          >
            <div class="list-results-sort">
              <p class="m-0">
                <span v-if="!loading">
                  Showing 1-{{ tourList.length + apiTours.length }} of
                  {{ tourList.length + apiTours.length }} results
                </span>
                <span v-else>Chargement...</span>
              </p>
            </div>
            <div
              class="click-menu d-flex align-items-center justify-content-between"
            >
              <div class="change-list f-active me-2">
                <router-link to="/tour-list">
                  <i class="fa fa-bars rounded"></i>
                </router-link>
              </div>
              <div class="change-grid me-2">
                <router-link to="/tour-grid">
                  <i class="fa fa-th rounded"></i>
                </router-link>
              </div>
              <div
                class="sortby input-box d-flex align-items-center justify-content-between ml-2"
              >
                <select class="niceSelect">
                  <option value="1">Sort By</option>
                  <option value="2">Average rating</option>
                  <option value="3">Price: low to high</option>
                  <option value="4">Price: high to low</option>
                </select>
              </div>
            </div>
          </div>

          <div class="destination-list">
            <!-- Affiche d'abord les tours dynamiques -->
            <div
              class="trend-full bg-white rounded box-shadow overflow-hidden p-4 mb-4"
              v-for="tour in apiTours"
              :key="'api-' + tour.id"
            >
              <div class="row">
                <div class="col-lg-4 col-md-3">
                  <div class="trend-item2 rounded">
                    <router-link
                      to="/tour-single"
                      :style="{
                        backgroundImage: tour.image
                          ? `url('${API_BASE_URL}/storage/${tour.image}')`
                          : 'url(images/destination/destination10.jpg)'
                      }"
                    ></router-link>
                    <div class="color-overlay"></div>
                  </div>
                </div>
                <div class="col-lg-5 col-md-6">
                  <div
                    class="trend-content position-relative text-md-start text-center"
                  >
                    <small>6+ Hours | Full Day Tours</small>
                    <h3 class="mb-1">
                      <router-link to="/tour-single">
                        {{ tour.title }}
                      </router-link>
                    </h3>
                    <h6 class="theme mb-0">
                      <i class="icon-location-pin"></i>
                      {{ tour.location }}
                    </h6>
                    <p class="mt-4 mb-0">
                      Taking Safety Measures <br />
                      <a href="#"
                        ><span class="theme">Free cancellation</span></a
                      >
                    </p>
                  </div>
                </div>
                <div class="col-lg-3 col-md-3">
                  <div class="trend-content text-md-end text-center">
                    <div class="rating d-flex justify-content-end gap-1">
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                    </div>
                    <small>{{ tour.reviews }} Reviews</small>
                    <div class="trend-price my-2">
                      <span class="mb-0">From</span>
                      <h3 class="mb-0">{{ tour.price }}</h3>
                      <small>Per Adult</small>
                    </div>
                    <router-link to="/tour-single" class="nir-btn">
                      View Detail
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
            <!-- Puis les tours statiques -->
            <div
              class="trend-full bg-white rounded box-shadow overflow-hidden p-4 mb-4"
              v-for="tour in tourList"
              :key="'static-' + tour.id"
            >
              <div class="row">
                <div class="col-lg-4 col-md-3">
                  <div class="trend-item2 rounded">
                    <router-link
                      to="/tour-single"
                      :style="{
                        backgroundImage: tour.image
                          ? `url('${tour.image}')`
                          : 'url(images/destination/destination10.jpg)'
                      }"
                    />
                    <div class="color-overlay"></div>
                  </div>
                </div>
                <div class="col-lg-5 col-md-6">
                  <div
                    class="trend-content position-relative text-md-start text-center"
                  >
                    <small>6+ Hours | Full Day Tours</small>
                    <h3 class="mb-1">
                      <router-link to="/tour-single">
                        {{ tour.title }}
                      </router-link>
                    </h3>
                    <h6 class="theme mb-0">
                      <i class="icon-location-pin"></i>
                      {{ tour.location }}
                    </h6>
                    <p class="mt-4 mb-0">
                      Taking Safety Measures <br />
                      <a href="#"
                        ><span class="theme">Free cancellation</span></a
                      >
                    </p>
                  </div>
                </div>
                <div class="col-lg-3 col-md-3">
                  <div class="trend-content text-md-end text-center">
                    <div class="rating d-flex justify-content-end gap-1">
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                    </div>
                    <small>{{ tour.reviews }} Reviews</small>
                    <div class="trend-price my-2">
                      <span class="mb-0">From</span>
                      <h3 class="mb-0">{{ tour.price }}</h3>
                      <small>Per Adult</small>
                    </div>
                    <router-link to="/tour-single" class="nir-btn">
                      View Detail
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="text-center"
              v-if="!loading && apiTours.length + tourList.length === 0"
            >
              <p>Aucun tour trouvé.</p>
            </div>
          </div>
        </div>

        <div class="col-lg-4 ps-lg-4">
          <div class="sidebar-sticky">
            <div class="list-sidebar">
              <div class="sidebar-item mb-4">
                <h3 class="">Categories Type</h3>
                <ul class="sidebar-category1">
                  <li>
                    <input type="checkbox" checked />
                    Tours
                    <span class="float-end">92</span>
                  </li>
                  <li>
                    <input type="checkbox" />
                    Attractions
                    <span class="float-end">22</span>
                  </li>
                  <li>
                    <input type="checkbox" />
                    Day Trips
                    <span class="float-end">35</span>
                  </li>
                  <li>
                    <input type="checkbox" />
                    Outdoor Activities
                    <span class="float-end">41</span>
                  </li>
                  <li>
                    <input type="checkbox" />
                    Concert &amp; Show
                    <span class="float-end">11</span>
                  </li>
                  <li>
                    <input type="checkbox" />
                    Indoor
                    <span class="float-end">61</span>
                  </li>
                  <li>
                    <input type="checkbox" />
                    Sight Seeing
                    <span class="float-end">18</span>
                  </li>
                  <li>
                    <input type="checkbox" />
                    Travels
                    <span class="float-end">88</span>
                  </li>
                </ul>
              </div>

              <div class="sidebar-item mb-4">
                <h3 class="">Duration Type</h3>
                <ul class="sidebar-category1">
                  <li>
                    <input type="checkbox" />
                    up to 1 hour
                    <span class="float-end">92</span>
                  </li>
                  <li>
                    <input type="checkbox" />
                    1 to 2 hour
                    <span class="float-end">22</span>
                  </li>
                  <li>
                    <input type="checkbox" />
                    2 to 4 hour
                    <span class="float-end">35</span>
                  </li>
                  <li>
                    <input type="checkbox" />
                    4 to 8 hour
                    <span class="float-end">41</span>
                  </li>
                  <li>
                    <input type="checkbox" />
                    8 to 1 Day
                    <span class="float-end">11</span>
                  </li>
                  <li>
                    <input type="checkbox" />
                    1 Day to 2 Days
                    <span class="float-end">61</span>
                  </li>
                </ul>
              </div>

              <div class="sidebar-item mb-4">
                <h3 class="">Duration Type</h3>
                <div class="range-slider mt-0">
                  <p class="text-start mb-2">Price Range</p>
                  <div
                    data-min="0"
                    data-unit="$"
                    data-max="2000"
                    aria-disabled="false"
                    data-min-name="min_price"
                    data-max-name="max_price"
                    class="range-slider-ui ui-slider ui-slider-horizontal ui-widget ui-widget-content ui-corner-all"
                  >
                    <span class="min-value">0 $</span>
                    <span class="max-value">20000 $</span>
                    <div
                      class="ui-slider-range ui-widget-header ui-corner-all full"
                      style="left: 0%; width: 100%"
                    ></div>
                    <div
                      class="ui-slider-range ui-widget-header ui-corner-all"
                      style="left: 0%; width: 100%"
                    ></div>
                    <a
                      class="ui-slider-handle ui-state-default ui-corner-all"
                      href="#"
                      style="left: 0%"
                    ></a>
                    <a
                      class="ui-slider-handle ui-state-default ui-corner-all"
                      href="#"
                      style="left: 100%"
                    ></a>
                  </div>
                  <div class="clearfix"></div>
                </div>
              </div>

              <div class="sidebar-item">
                <h3>Related Destinations</h3>
                <div class="sidebar-destination">
                  <div class="row about-slider slick-initialized slick-slider">
                    <div
                      class="splide"
                      aria-label="Destination"
                      id="destination-carousel"
                    >
                      <div class="splide__track">
                        <ul class="splide__list">
                          <li class="splide__slide">
                            <div tabindex="-1" aria-hidden="true">
                              <div class="trend-item1">
                                <div
                                  class="trend-image position-relative rounded"
                                >
                                  <img
                                    src="images/destination/destination17.jpg"
                                    alt="image"
                                  />
                                  <div
                                    class="trend-content d-flex align-items-center justify-content-between position-absolute bottom-0 p-4 w-100 z-index"
                                  >
                                    <div class="trend-content-title">
                                      <h5 class="mb-0">
                                        <router-link
                                          tabindex="-1"
                                          class="theme1"
                                          to="/tour-single"
                                        >
                                          Tokyo
                                        </router-link>
                                      </h5>
                                      <h4 class="mb-0 white">Japan</h4>
                                    </div>
                                    <span
                                      class="white bg-theme p-1 px-2 rounded"
                                    >
                                      21 Tours
                                    </span>
                                  </div>
                                  <div class="color-overlay"></div>
                                </div>
                              </div>
                            </div>
                          </li>
                          <li class="splide__slide">
                            <div tabindex="-1" aria-hidden="true">
                              <div class="trend-item1">
                                <div
                                  class="trend-image position-relative rounded"
                                >
                                  <img
                                    src="images/destination/destination14.jpg"
                                    alt="image"
                                  />
                                  <div
                                    class="trend-content d-flex align-items-center justify-content-between position-absolute bottom-0 p-4 w-100 z-index"
                                  >
                                    <div class="trend-content-title">
                                      <h5 class="mb-0">
                                        <router-link
                                          tabindex="-1"
                                          class="theme1"
                                          to="/tour-single"
                                        >
                                          Tokyo
                                        </router-link>
                                      </h5>
                                      <h4 class="mb-0 white">Japan</h4>
                                    </div>
                                    <span
                                      class="white bg-theme p-1 px-2 rounded"
                                    >
                                      21 Tours
                                    </span>
                                  </div>
                                  <div class="color-overlay"></div>
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
        </div>
      </div>
    </div>
  </section>

  <DiscountAction />

  <Footer />
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

.niceSelect:focus {
  border-color: #999;
}
</style>
