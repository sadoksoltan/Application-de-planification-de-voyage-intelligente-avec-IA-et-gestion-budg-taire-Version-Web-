<script setup lang="ts">
import Appbar from 'pages/components/Appbar.vue'
import Banner2 from 'pages/components/Banner2.vue'
import AboutUs2 from 'pages/components/AboutUs2.vue'
import DiscountAction from 'pages/components/DiscountAction.vue'
import Footer from 'pages/components/Footer.vue'

import Shape4Image from 'images/shape4.png'
</script>

<template>
  <Appbar />

  <Banner2 page-title="Our Services" />

  <section
    class="about-us pb-6 pt-6"
    style="background-position: center"
    :style="{ backgroundImage: `url('${Shape4Image}')` }"
  >
    <div class="container">
      <div class="section-title mb-6 w-50 mx-auto text-center">
        <h4 class="mb-1 theme1">Core of The Perfect Tour</h4>

        <h2 class="mb-1">Find <span class="theme">Travel Perfection</span></h2>

        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore.
        </p>
      </div>

      <div class="why-us">
        <div class="why-us-box">
          <div class="row">
            <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
              <div
                class="why-us-item text-center p-4 py-5 border rounded bg-white"
              >
                <div class="why-us-content">
                  <div class="why-us-icon">
                    <i class="icon-flag theme"></i>
                  </div>

                  <h4>
                    <router-link to="/services-detail">
                      Tell Us What You want To Do
                    </router-link>
                  </h4>

                  <p class="mb-0">
                    Lorem ipsum dolor sit amet, consectetur adipiscing.
                  </p>
                </div>
              </div>
            </div>

            <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
              <div
                class="why-us-item text-center p-4 py-5 border rounded bg-white"
              >
                <div class="why-us-content">
                  <div class="why-us-icon">
                    <i class="icon-location-pin theme"></i>
                  </div>

                  <h4>
                    <router-link to="/services-detail">
                      Share Your Travel Locations
                    </router-link>
                  </h4>

                  <p class="mb-0">
                    Lorem ipsum dolor sit amet, consectetur adipiscing.
                  </p>
                </div>
              </div>
            </div>

            <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
              <div
                class="why-us-item text-center p-4 py-5 border rounded bg-white"
              >
                <div class="why-us-content">
                  <div class="why-us-icon">
                    <i class="icon-directions theme"></i>
                  </div>

                  <h4>
                    <router-link to="/services-detail">
                      Share Your Travel Preference
                    </router-link>
                  </h4>

                  <p class="mb-0">
                    Lorem ipsum dolor sit amet, consectetur adipiscing.
                  </p>
                </div>
              </div>
            </div>

            <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
              <div
                class="why-us-item text-center p-4 py-5 border rounded bg-white"
              >
                <div class="why-us-content">
                  <div class="why-us-icon">
                    <i class="icon-compass theme"></i>
                  </div>

                  <h4>
                    <router-link to="/services-detail">
                      We are 100% Trusted Tour Agency
                    </router-link>
                  </h4>

                  <p class="mb-0">
                    Lorem ipsum dolor sit amet, consectetur adipiscing.
                  </p>
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
                    <router-link to="/services-detail">
                      Here 100% Trusted Tour Agency
                    </router-link>
                  </h4>

                  <p class="mb-2">
                    Excepteur sint occaecat cupidatat non proident, sunt in
                    culpa qui officia.
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
                    <router-link to="/services-detail">
                      Share Your Travel Locations
                    </router-link>
                  </h4>

                  <p class="mb-2">
                    Excepteur sint occaecat cupidatat non proident, sunt in
                    culpa qui officia.
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
                    <router-link to="/services-detail">
                      Share Your Travel Preference
                    </router-link>
                  </h4>

                  <p class="mb-2">
                    Excepteur sint occaecat cupidatat non proident, sunt in
                    culpa qui officia.
                  </p>

                  <p class="mb-0 theme">100+ Reviews</p>
                </div>
              </div>
            </div>

            <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
              <div class="why-us-item p-5 pt-6 pb-6 border rounded bg-white">
                <div class="why-us-content">
                  <div class="why-us-icon mb-1">
                    <i class="icon-flag theme"></i>
                  </div>

                  <h4>
                    <router-link to="/services-detail">
                      Tell Us What You want To Do
                    </router-link>
                  </h4>

                  <p class="mb-2">
                    Excepteur sint occaecat cupidatat non proident, sunt in
                    culpa qui officia.
                  </p>

                  <p class="mb-0 theme">100+ Reviews</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="white-overlay"></div>
  </section>

  <AboutUs2 />

  <DiscountAction />

  <Footer />
</template>
