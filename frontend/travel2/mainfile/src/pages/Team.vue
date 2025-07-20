<script setup lang="ts">
import Appbar from './components/Appbar.vue'
import Banner2 from './components/Banner2.vue'
import OurTeam from './components/OurTeam.vue'
import Footer from './components/Footer.vue'

import BGTransImage from 'images/bg/bg-trans.png'
import Shape8Image from 'images/shape8.png'
</script>

<template>
  <Appbar />

  <Banner2 page-title="Our Guide" />

  <OurTeam />

  <section
    class="about-us pt-0"
    :style="{ backgroundImage: `url('${BGTransImage}')` }"
  >
    <div class="container">
      <div class="about-image-box">
        <div class="row d-flex align-items-center justify-content-between">
          <div class="col-lg-6 mb-4 pe-4">
            <div class="about-image1 overflow-hidden rounded">
              <img src="images/destination/destination6.jpg" alt="" />
            </div>
          </div>

          <div class="col-lg-6 mb-4 ps-4">
            <div class="about-content text-center text-lg-start mb-4">
              <h4 class="theme d-inline-block mb-0">Pefect Team</h4>

              <h2 class="mb-2">Our Experience Guides</h2>

              <p class="mb-2">
                Traveling is not just an escape; it’s an opening to the world.
                Each destination offers a new culture, unique flavors, and
                unforgettable encounters. Whether exploring the colorful streets
                of a historic city or savoring local cuisine in a quaint
                restaurant, every experience enriches our understanding of life.
                Allow yourself to be carried away by adventure and discover
                everything the world has to offer!
              </p>

              <div class="about-listing border-b mb-2 pb-2">
                <h5 class="mb-1">
                  <i class="icon-location-pin theme"></i>
                  Expert Team Guide
                </h5>

                <p class="mb-0">
                  Explore new horizons, embrace different cultures, and create
                  unforgettable memories.
                </p>
              </div>

              <div class="about-listing border-b mb-2 pb-2">
                <h5 class="mb-1">
                  <i class="icon-briefcase theme"></i>
                  Correct Directions
                </h5>

                <p class="mb-0">
                  Explore new horizons, embrace different cultures, and create
                  unforgettable memories.
                </p>
              </div>

              <div class="about-listing">
                <h5 class="mb-1">
                  <i class="icon-folder theme"></i>
                  Save Money &amp; Time
                </h5>

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

    <div class="white-overlay"></div>
  </section>

  <section class="our-team pb-2">
    <div
      class="section-shape section-shape1"
      :style="{ backgroundImage: `url('${Shape8Image}')` }"
    ></div>

    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-4 mb-4">
          <div class="section-title text-lg-start text-center">
            <h4 class="mb-1 theme1">Tour Guides</h4>

            <h2>Meet Our <span class="theme"> Excellent Guides </span></h2>

            <p class="mb-0">
              Discover the beauty of the world around you, immerse yourself in
              diverse cultures, and create lasting memories through your
              travels. Embrace every moment as an opportunity for growth and
              adventure.
            </p>
          </div>
        </div>

        <div class="col-lg-8 mb-4">
          <div class="row team-main">
            <div class="col-lg-4 col-md-6 mb-4">
              <div class="team-list bg-white rounded">
                <div class="team-image">
                  <img src="images/team/img1.jpg" alt="team" />
                </div>

                <div class="team-content text-center p-3 bg-theme">
                  <h4 class="mb-0 white">Salmon Thuir</h4>
                  <p class="mb-0 white">Senior Agent</p>
                </div>
              </div>
            </div>

            <div class="col-lg-4 col-md-6 mb-4">
              <div class="team-list bg-white rounded">
                <div class="team-image">
                  <img src="images/team/img2.jpg" alt="team" />
                </div>

                <div class="team-content text-center p-3 bg-theme">
                  <h4 class="mb-0 white">Horke Pels</h4>
                  <p class="mb-0 white">Head Officer</p>
                </div>
              </div>
            </div>

            <div class="col-lg-4 col-md-6 mb-4">
              <div class="team-list bg-white rounded">
                <div class="team-image">
                  <img src="images/team/img4.jpg" alt="team" />
                </div>

                <div class="team-content text-center p-3 bg-theme">
                  <h4 class="mb-0 white">Solden kalos</h4>
                  <p class="mb-0 white">Supervisor</p>
                </div>
              </div>
            </div>

            <div class="col-lg-4 col-md-6 mb-4">
              <div class="team-list bg-white rounded">
                <div class="team-image">
                  <img src="images/team/img3.jpg" alt="team" />
                </div>

                <div class="team-content text-center p-3 bg-theme">
                  <h4 class="mb-0 white">Nelson Bam</h4>
                  <p class="mb-0 white">Quality Assurance</p>
                </div>
              </div>
            </div>

            <div class="col-lg-4 col-md-6 mb-4">
              <div class="team-list bg-white rounded">
                <div class="team-image">
                  <img src="images/team/img1.jpg" alt="team" />
                </div>

                <div class="team-content text-center p-3 bg-theme">
                  <h4 class="mb-0 white">Salmon Thuir</h4>
                  <p class="mb-0 white">Senior Agent</p>
                </div>
              </div>
            </div>

            <div class="col-lg-4 col-md-6 mb-4">
              <div class="team-list bg-white rounded">
                <div class="team-image">
                  <img src="images/team/img2.jpg" alt="team" />
                </div>

                <div class="team-content text-center p-3 bg-theme">
                  <h4 class="mb-0 white">Horke Pels</h4>
                  <p class="mb-0 white">Head Officer</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <Footer />
</template>
