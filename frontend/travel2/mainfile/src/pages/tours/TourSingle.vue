<script setup lang="ts">
import { onMounted, ref } from 'vue'
import Splide from '@splidejs/splide'
import '@splidejs/splide/css'

import Appbar from '../components/Appbar.vue'
import DiscountAction from '../components/DiscountAction.vue'
import OurPartners from '../components/OurPartners.vue'
import Footer from '../components/Footer.vue'

import Shap8Image from 'images/shape8.png'

const accrodianIdx = ref(1)

onMounted(() => {
  new Splide('#destination-carousel', {
    arrows: false,
    autoplay: true,
    drag: true,
    interval: 7000,
    pagination: false,
    perPage: 4,
    speed: 3000,
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
</script>

<template>
  <Appbar />

  <div class="banner trending overflow-hidden">
    <div
      class="section-shape section-shape1 top-inherit bottom-0"
      :style="`background-image: url('${Shap8Image}')`"
    ></div>

    <div class="banner-slide">
      <div class="row shop-slider">
        <div
          class="splide"
          id="destination-carousel"
          aria-label="Tour Destinations"
        >
          <div class="splide__track">
            <ul class="splide__list">
              <li class="splide__slide">
                <div tabindex="-1" aria-hidden="true">
                  <div class="trend-item1 box-shadow bg-white text-center">
                    <div class="trend-image position-relative">
                      <img alt="image" src="images/new-deal/deal1.jpg" />

                      <div class="overlay"></div>
                    </div>
                  </div>
                </div>
              </li>

              <li class="splide__slide">
                <div tabindex="-1" aria-hidden="true">
                  <div class="trend-item1 box-shadow bg-white text-center">
                    <div class="trend-image position-relative">
                      <img alt="image" src="images/new-deal/deal4.jpg" />

                      <div class="overlay"></div>
                    </div>
                  </div>
                </div>
              </li>

              <li class="splide__slide">
                <div tabindex="-1" aria-hidden="true">
                  <div class="trend-item1 box-shadow bg-white text-center">
                    <div class="trend-image position-relative">
                      <img alt="image" src="images/new-deal/deal5.jpg" />

                      <div class="overlay"></div>
                    </div>
                  </div>
                </div>
              </li>

              <li class="splide__slide">
                <div tabindex="-1" aria-hidden="true">
                  <div class="trend-item1 box-shadow bg-white text-center">
                    <div class="trend-image position-relative">
                      <img alt="image" src="images/new-deal/deal1.jpg" />

                      <div class="overlay"></div>
                    </div>
                  </div>
                </div>
              </li>

              <li class="splide__slide">
                <div tabindex="-1" aria-hidden="true">
                  <div class="trend-item1 box-shadow bg-white text-center">
                    <div class="trend-image position-relative">
                      <img alt="image" src="images/new-deal/deal2.jpg" />

                      <div class="overlay"></div>
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <div
      class="banner-breadcrum position-absolute top-50 mx-auto w-50 start-50 text-center translate-middle"
    >
      <div class="breadcrumb-content text-center">
        <h1 class="mb-0 white">Tour Single</h1>

        <nav aria-label="breadcrumb" class="d-block">
          <ul class="breadcrumb">
            <li class="breadcrumb-item">
              <a href="#">Home</a>
            </li>

            <li class="breadcrumb-item active" aria-current="page">
              Tour Single One
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>

  <section class="trending pt-6 pb-0 bg-lgrey">
    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <div class="single-content">
            <div id="highlight">
              <div class="single-full-title border-b mb-2 pb-2">
                <div class="single-title">
                  <h2 class="mb-1">Adriatic Adventure-Zagreb to Athens</h2>

                  <div class="rating-main d-md-flex align-items-center">
                    <p class="mb-0 me-2">
                      <i class="icon-location-pin"></i>
                      Greater London, United Kingdom
                    </p>

                    <div class="rating me-2 d-flex gap-1">
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                    </div>

                    <span>(1,186 Reviews)</span>
                  </div>
                </div>
              </div>

              <div class="description-images mb-4">
                <img
                  src="images/trending/trending-large.jpg"
                  alt=""
                  class="w-100 rounded"
                />
              </div>

              <div class="description mb-2">
                <h4>Description</h4>

                Traveling is not just an escape; it’s an opening to the world.
                Each destination offers a new culture, unique flavors, and
                unforgettable encounters. Whether exploring the colorful streets
                of a historic city or savoring local cuisine in a quaint
                restaurant, every experience enriches our understanding of life.
                Allow yourself to be carried away by adventure and discover
                everything the world has to offer!
              </div>

              <div class="tour-includes mb-4">
                <table>
                  <tbody>
                    <tr>
                      <td>
                        <i
                          aria-hidden="true"
                          class="fa fa-clock-o pink mr-1"
                        ></i>
                        5 Days
                      </td>

                      <td>
                        <i class="fa fa-group pink mr-1" aria-hidden="true"></i>
                        Max People : 26
                      </td>
                      <td>
                        <i
                          aria-hidden="true"
                          class="fa fa-calendar pink mr-1"
                        ></i>
                        Jan 18 - Dec 25
                      </td>
                    </tr>

                    <tr>
                      <td>
                        <i class="fa fa-user pink mr-1" aria-hidden="true"></i>
                        Min Age : 10+
                      </td>

                      <td>
                        <i
                          aria-hidden="true"
                          class="fa fa-map-signs pink mr-1"
                        ></i>
                        Pickup : Airport
                      </td>

                      <td>
                        <i
                          class="fa fa-file-alt pink mr-1"
                          aria-hidden="true"
                        ></i>
                        Langauge - English, Thai
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <div class="description mb-2">
                <div class="row">
                  <div class="col-lg-6 col-md-6 mb-2">
                    <div class="desc-box bg-grey p-4 rounded">
                      <h5 class="mb-2">Departure &amp; Return Location</h5>

                      <p class="mb-0">
                        John F.K. International Airport(Google Map)
                      </p>
                    </div>
                  </div>

                  <div class="col-lg-6 col-md-6 mb-2">
                    <div class="desc-box bg-grey p-4 rounded">
                      <h5 class="mb-2">Bedroom</h5>
                      <p class="mb-0">4 Bedrooms</p>
                    </div>
                  </div>

                  <div class="col-lg-6 col-md-6 mb-2">
                    <div class="desc-box bg-grey p-4 rounded">
                      <h5 class="mb-2">Departure Time</h5>
                      <p class="mb-0">3 Hours Before Flight Time</p>
                    </div>
                  </div>

                  <div class="col-lg-6 col-md-6 mb-2">
                    <div class="desc-box bg-grey p-4 rounded">
                      <h5 class="mb-2">Departure Time</h5>
                      <p class="mb-0">3 Hours Before Flight Time</p>
                    </div>
                  </div>

                  <div class="col-lg-6 col-md-6 mb-2">
                    <div class="desc-box bg-grey p-4 rounded">
                      <h5 class="mb-2">Price Includes</h5>
                      <ul>
                        <li class="d-block pb-1">
                          <i class="fa fa-check pink mr-1"></i> Air Fares
                        </li>
                        <li class="d-block pb-1">
                          <i class="fa fa-check pink mr-1"></i> 3 Nights Hotel
                          Accomodation
                        </li>
                        <li class="d-block pb-1">
                          <i class="fa fa-check pink mr-1"></i> Tour Guide
                        </li>
                        <li class="d-block">
                          <i class="fa fa-check pink mr-1"></i> Entrance Fees
                        </li>
                      </ul>
                    </div>
                  </div>

                  <div class="col-lg-6 col-md-6 mb-2">
                    <div class="desc-box bg-grey p-4 rounded">
                      <h5 class="mb-2">Departure &amp; Return Location</h5>

                      <ul>
                        <li class="d-block pb-1">
                          <i class="fa fa-close pink mr-1"></i>
                          Guide Service Fee
                        </li>

                        <li class="d-block pb-1">
                          <i class="fa fa-close pink mr-1"></i>
                          Driver Service Fee
                        </li>

                        <li class="d-block pb-1">
                          <i class="fa fa-close pink mr-1"></i>
                          Any Private Expenses
                        </li>

                        <li class="d-block">
                          <i class="fa fa-close pink mr-1"></i>
                          Room Service Fees
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>

              <div class="description mb-4">
                <h4>What to Expect</h4>

                Traveling is not just an escape; it’s an opening to the world.
                Each destination offers a new culture, unique flavors, and
                unforgettable encounters. Whether exploring the colorful streets
                of a historic city or savoring local cuisine in a quaint
                restaurant, every experience enriches our understanding of life.
                Allow yourself to be carried away by adventure and discover
                everything the world has to offer!
              </div>
            </div>

            <div
              id="iternary"
              data-grp-name="faq-accrodion"
              class="accrodion-grp faq-accrodion mb-4"
            >
              <div class="accrodion" :class="{ active: accrodianIdx === 1 }">
                <div class="accrodion-title rounded" @click="accrodianIdx = 1">
                  <h5 class="mb-0">
                    <span>Day 1</span>
                    - Barcelona - Zaragoza - Madrid
                  </h5>
                </div>

                <div
                  class="accrodion-content"
                  :class="{ 'd-none': accrodianIdx !== 1 }"
                >
                  <div class="inner">
                    <p>
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                      Ipsa, inventore cumque veniam, praesentium velit incidunt
                      rem quas a, quos eos ipsum, reprehenderit voluptatem.
                    </p>
                  </div>
                </div>
              </div>

              <div class="accrodion" :class="{ active: accrodianIdx === 2 }">
                <div class="accrodion-title rounded" @click="accrodianIdx = 2">
                  <h5 class="mb-0">
                    <span>Day 2</span>
                    - Zurich - Biel/Bienne - Neuchatel - Geneva
                  </h5>
                </div>

                <div
                  class="accrodion-content"
                  :class="{ 'd-none': accrodianIdx !== 2 }"
                >
                  <div class="inner">
                    <p>
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                      Ipsa, inventore cumque veniam, praesentium velit incidunt
                      rem quas a, quos eos ipsum, reprehenderit voluptatem.
                    </p>
                  </div>
                </div>
              </div>

              <div class="accrodion" :class="{ active: accrodianIdx === 3 }">
                <div class="accrodion-title rounded" @click="accrodianIdx = 3">
                  <h5 class="mb-0">
                    <span>Day 3</span>
                    - Enchanting Engelberg
                  </h5>
                </div>

                <div
                  class="accrodion-content"
                  :class="{ 'd-none': accrodianIdx !== 3 }"
                >
                  <div class="inner">
                    <p>
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                      Ipsa, inventore cumque veniam, praesentium velit incidunt
                      rem quas a, quos eos ipsum, reprehenderit voluptatem.
                    </p>
                  </div>
                </div>
              </div>

              <div class="accrodion" :class="{ active: accrodianIdx === 4 }">
                <div class="accrodion-title rounded" @click="accrodianIdx = 4">
                  <h5 class="mb-0">
                    <span>Day 4</span>
                    - Barcelona - Zaragoza - Madrid
                  </h5>
                </div>

                <div
                  class="accrodion-content"
                  :class="{ 'd-none': accrodianIdx !== 4 }"
                >
                  <div class="inner">
                    <p>
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                      Ipsa, inventore cumque veniam, praesentium velit incidunt
                      rem quas a, quos eos ipsum, reprehenderit voluptatem.
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <div id="single-map" class="single-map mb-4">
              <h4>Map</h4>

              <div class="map rounded overflow-hidden">
                <div style="width: 100%">
                  <iframe
                    height="400"
                    class="rounded overflow-hidden"
                    src="https://maps.google.com/maps?width=100%25&height=600&hl=en&q=Monastir,%20Tunisia&t=&z=14&ie=UTF8&iwloc=B&output=embed"
                  ></iframe>
                </div>
              </div>
            </div>

            <div id="single-review" class="single-review mb-4">
              <h4>Average Reviews</h4>

              <div class="row d-flex align-items-center">
                <div class="col-lg-4 col-md-4">
                  <div class="review-box bg-title text-center py-4 p-2 rounded">
                    <h2 class="mb-1 white"><span>2.2</span>/5</h2>

                    <h4 class="white mb-1">
                      "Feel so much worst than thinking"
                    </h4>

                    <p class="mb-0 white font-italic">From 40 Reviews</p>
                  </div>
                </div>

                <div class="col-lg-8 col-md-8">
                  <div class="review-progress">
                    <div class="progress-item mb-1">
                      <p class="mb-0">Cleanliness</p>

                      <div class="progress rounded">
                        <div
                          role="progressbar"
                          aria-valuenow="40"
                          aria-valuemin="0"
                          style="width: 40%"
                          aria-valuemax="100"
                          class="progress-bar bg-theme"
                        >
                          <span class="sr-only">40% Complete</span>
                        </div>
                      </div>
                    </div>

                    <div class="progress-item mb-1">
                      <p class="mb-0">Facilities</p>

                      <div class="progress rounded">
                        <div
                          role="progressbar"
                          aria-valuenow="30"
                          aria-valuemin="0"
                          aria-valuemax="100"
                          style="width: 30%"
                          class="progress-bar bg-theme"
                        >
                          <span class="sr-only">30% Complete</span>
                        </div>
                      </div>
                    </div>

                    <div class="progress-item mb-1">
                      <p class="mb-0">Value for money</p>

                      <div class="progress rounded">
                        <div
                          role="progressbar"
                          aria-valuenow="60"
                          aria-valuemin="0"
                          style="width: 60%"
                          aria-valuemax="100"
                          class="progress-bar bg-theme"
                        >
                          <span class="sr-only">60% Complete</span>
                        </div>
                      </div>
                    </div>

                    <div class="progress-item mb-1">
                      <p class="mb-0">Service</p>

                      <div class="progress rounded">
                        <div
                          role="progressbar"
                          aria-valuenow="20"
                          aria-valuemin="0"
                          style="width: 20%"
                          aria-valuemax="100"
                          class="progress-bar bg-theme"
                        >
                          <span class="sr-only">20% Complete</span>
                        </div>
                      </div>
                    </div>

                    <div class="progress-item">
                      <p class="mb-0">Location</p>

                      <div class="progress rounded">
                        <div
                          role="progressbar"
                          aria-valuenow="45"
                          aria-valuemin="0"
                          style="width: 45%"
                          aria-valuemax="100"
                          class="progress-bar bg-theme"
                        >
                          <span class="sr-only">45% Complete</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div id="single-comments" class="single-comments single-box mb-4">
              <h5 class="border-b pb-2 mb-2">
                Showing 16 verified guest comments
              </h5>

              <div class="comment-box">
                <div class="comment-image">
                  <img src="images/reviewer/1.jpg" alt="image" />
                </div>

                <div class="comment-content rounded">
                  <h5 class="mb-1">Helena</h5>

                  <p class="comment-date">April 25, 2022 at 10:46 am</p>

                  <div class="comment-rate">
                    <div class="rating mar-right-15 d-flex gap-1">
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                    </div>
                    <span class="comment-title">The worst hotel ever"</span>
                  </div>

                  <p class="comment">
                    Take in the iconic skyline and visit the neighbourhood
                    hangouts that you've only ever seen on TV. Take in the
                    iconic skyline and visit the neighbourhood.
                  </p>

                  <div class="comment-like">
                    <div class="like-title">
                      <a href="#" class="nir-btn">Reply</a>
                    </div>

                    <div class="like-btn pull-right">
                      <a href="#" class="like">
                        <i class="fa fa-thumbs-up"></i>
                      </a>

                      <a href="#" class="disike"
                        ><i class="fa fa-thumbs-down"></i>
                      </a>
                    </div>
                  </div>
                </div>
              </div>

              <div class="comment-box">
                <div class="comment-image">
                  <img src="images/reviewer/2.jpg" alt="image" />
                </div>

                <div class="comment-content rounded">
                  <h5 class="mb-1">Helena</h5>

                  <p class="comment-date">April 25, 2022 at 10:46 am</p>

                  <div class="comment-rate">
                    <div class="rating mar-right-15 d-flex gap-1">
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                      <span class="fa fa-star checked"></span>
                    </div>

                    <span class="comment-title">
                      Was too noisy and not suitable for business meetings"
                    </span>
                  </div>

                  <p class="comment">
                    Take in the iconic skyline and visit the neighbourhood
                    hangouts that you've only ever seen on TV. Take in the
                    iconic skyline and visit the neighbourhood.
                  </p>

                  <div class="comment-like">
                    <div class="like-title">
                      <a href="#" class="nir-btn">Reply</a>
                    </div>

                    <div class="like-btn pull-right">
                      <a href="#" class="like">
                        <i class="fa fa-thumbs-up"></i>
                      </a>

                      <a href="#" class="disike">
                        <i class="fa fa-thumbs-down"></i>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div id="single-add-review" class="single-add-review">
              <h4>Write a Review</h4>

              <form>
                <div class="row">
                  <div class="col-md-6">
                    <div class="form-group mb-2">
                      <input type="text" placeholder="Name" />
                    </div>
                  </div>

                  <div class="col-md-6">
                    <div class="form-group mb-2">
                      <input type="email" placeholder="Email" />
                    </div>
                  </div>

                  <div class="col-md-12">
                    <div class="form-group mb-2">
                      <textarea>Comment</textarea>
                    </div>
                  </div>

                  <div class="col-md-6">
                    <div class="form-btn">
                      <a href="#" class="nir-btn">Submit Review</a>
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>

        <div class="col-lg-4 ps-lg-4">
          <div class="sidebar-sticky sticky1">
            <div
              class="tabs-navbar bg-lgrey mb-4 bordernone rounded overflow-hidden"
            >
              <div class="row">
                <div class="col-md-12">
                  <ul id="tabs" class="nav nav-tabs bordernone mb-0">
                    <li class="active">
                      <a
                        data-toggle="tab"
                        href="#highlight"
                        class="rounded box-shadow mb-2 border-all"
                      >
                        Highlight
                      </a>
                    </li>

                    <li>
                      <a
                        data-toggle="tab"
                        href="#iternary"
                        class="rounded box-shadow mb-2 border-all"
                      >
                        Iternary
                      </a>
                    </li>

                    <li>
                      <a
                        data-toggle="tab"
                        href="#single-map"
                        class="rounded box-shadow mb-2 border-all"
                      >
                        Map
                      </a>
                    </li>

                    <li>
                      <a
                        data-toggle="tab"
                        href="#single-review"
                        class="rounded box-shadow mb-2 border-all"
                      >
                        Reviews
                      </a>
                    </li>

                    <li>
                      <a
                        data-toggle="tab"
                        href="#single-comments"
                        class="rounded box-shadow mb-2 border-all"
                      >
                        Comments
                      </a>
                    </li>

                    <li>
                      <a
                        data-toggle="tab"
                        href="#single-add-review"
                        class="rounded box-shadow mb-2 border-all"
                      >
                        Add Reviews
                      </a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <DiscountAction style="padding-top: 0 !important" />

  <OurPartners />

  <Footer />
</template>

<style scoped>
.splide {
  height: 600px;
}

.trend-image img {
  height: 500px;
}
</style>
