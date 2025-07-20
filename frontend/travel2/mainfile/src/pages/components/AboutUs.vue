<script setup lang="ts">
import Shape4Image from 'images/shape4.png'
</script>

<template>
  <section
    class="about-us pb-6 pt-6"
    style="background-position: center"
    :style="`background-image: url('${Shape4Image}')`"
  >
    <div class="container">
      <div class="section-title mb-6 w-50 mx-auto text-center">
        <h4 class="mb-1 theme1">3 Step of The Perfect Tour</h4>

        <h2 class="mb-1">
          Find
          <span class="theme">Travel Perfection</span>
        </h2>

        <p>
          Explore new horizons, embrace different cultures, and create
          unforgettable memories.
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
                    <router-link to="/about">
                      Tell Us What You want To Do
                    </router-link>
                  </h4>

                  <p class="mb-0">
                    Explore new horizons, embrace different cultures, and create
                    unforgettable memories.
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
                    <router-link to="/about">
                      Share Your Travel Locations
                    </router-link>
                  </h4>

                  <p class="mb-0">
                    Explore new horizons, embrace different cultures, and create
                    unforgettable memories.
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
                    <router-link to="/about">
                      Share Your Travel Preference
                    </router-link>
                  </h4>

                  <p class="mb-0">
                    Explore new horizons, embrace different cultures, and create
                    unforgettable memories.
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
                    <router-link to="/about">
                      We are 100% Trusted Tour Agency
                    </router-link>
                  </h4>

                  <p class="mb-0">
                    Explore new horizons, embrace different cultures, and create
                    unforgettable memories.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="white-overlay"></div>
  </section>
</template>
