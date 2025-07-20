<script setup lang="ts">
import Appbar from 'pages/components/Appbar.vue'
import Banner2 from 'pages/components/Banner2.vue'
import DiscountAction from 'pages/components/DiscountAction.vue'
import Footer from 'pages/components/Footer.vue'
</script>

<template>
  <Appbar />

  <Banner2 page-title="Service Detail" />

  <section class="about-us pt-6 pb-0">
    <div class="container">
      <div class="about-image-box">
        <div class="row">
          <div class="col-lg-8 col-sm-12 pe-lg-4">
            <div class="about-content">
              <h2 class="mb-3">Share Your Travel Locations</h2>

              <div class="about-image rounded mb-3 overflow-hidden">
                <img src="images/trending/trending4.jpg" alt="" class="w-100" />
              </div>

              <p class="mb-3">
                Monastir is a beautiful coastal city in Tunisia, known for its
                rich history, stunning beaches, and welcoming atmosphere.
                Nestled along the Mediterranean Sea, it offers a perfect blend
                of culture, relaxation, and adventure.
                <br /><br />
                From the historic Ribat fortress to the vibrant marina and
                charming medina, Monastir has something for every traveler.
                Whether you're exploring ancient monuments or enjoying the local
                cuisine, you'll find unforgettable moments in this seaside gem.
              </p>

              <div class="services-image d-flex mt-3 mb-3">
                <div class="me-2 rounded overflow-hidden">
                  <img
                    src="images/trending/trending5.jpg"
                    alt=""
                    class="w-100"
                  />
                </div>

                <div class="ms-2 rounded overflow-hidden">
                  <img
                    src="images/trending/trending6.jpg"
                    alt=""
                    class="w-100"
                  />
                </div>
              </div>

              <p class="mb-0">
                Monastir is a beautiful coastal city in Tunisia, known for its
                rich history, stunning beaches, and welcoming atmosphere.
                Nestled along the Mediterranean Sea, it offers a perfect blend
                of culture, relaxation, and adventure.
                <br /><br />
                From the historic Ribat fortress to the vibrant marina and
                charming medina, Monastir has something for every traveler.
                Whether you're exploring ancient monuments or enjoying the local
                cuisine, you'll find unforgettable moments in this seaside gem.
              </p>
            </div>
          </div>

          <div class="col-lg-4 col-sm-12 ps-lg-4">
            <div class="sidebar-sticky">
              <div class="list-sidebar">
                <div class="sidebar-item mb-4">
                  <h3 class="">All Categories</h3>
                  <ul class="sidebar-category">
                    <li>
                      <a href="#">Travel Management</a>
                    </li>

                    <li>
                      <a href="#">Tour Services</a>
                    </li>

                    <li>
                      <a href="#">Trip Consulting</a>
                    </li>

                    <li class="active">
                      <a href="#">Travel Preference</a>
                    </li>

                    <li>
                      <a href="#">Tour Agency</a>
                    </li>

                    <li>
                      <a href="#">Top Destination</a>
                    </li>

                    <li>
                      <a href="#">Your Booking</a>
                    </li>

                    <li>
                      <a href="#">TOp Pick</a>
                    </li>
                  </ul>
                </div>

                <div class="popular-post sidebar-item mb-4">
                  <h3 class="">Related Services</h3>
                  <div class="sidebar-tabs">
                    <div class="post-tabs">
                      <div class="tab-content" id="postsTabContent1">
                        <div
                          id="popular"
                          role="tabpanel"
                          class="tab-pane fade active show"
                        >
                          <article class="post mb-3 border-b pb-3">
                            <div
                              class="s-content d-flex align-items-center justify-space-between"
                            >
                              <div class="sidebar-image w-25 me-3">
                                <router-link to="/detail-1">
                                  <img
                                    src="images/trending/trending1.jpg"
                                    alt=""
                                  />
                                </router-link>
                              </div>

                              <div class="content-list w-75">
                                <h5 class="mb-1">
                                  <router-link to="/detail-1">
                                    An Incredibly Easy Method That Works For All
                                  </router-link>
                                </h5>

                                <div class="date">10 Apr 2021</div>
                              </div>
                            </div>
                          </article>

                          <article class="post border-b pb-3 mb-3">
                            <div
                              class="s-content d-flex align-items-center justify-space-between"
                            >
                              <div class="sidebar-image w-25 me-3">
                                <router-link to="/detail-1">
                                  <img
                                    src="images/trending/trending2.jpg"
                                    alt=""
                                  />
                                </router-link>
                              </div>

                              <div class="content-list w-75">
                                <h5 class="mb-1">
                                  <router-link to="/detail-1">
                                    15 Unheard Ways To Achieve Greater Walker
                                  </router-link>
                                </h5>

                                <div class="date">29 Mar 2021</div>
                              </div>
                            </div>
                          </article>

                          <article class="post">
                            <div
                              class="s-content d-flex align-items-center justify-space-between"
                            >
                              <div class="sidebar-image w-25 me-3">
                                <router-link to="/detail-1">
                                  <img
                                    src="images/trending/trending4.jpg"
                                    alt=""
                                  />
                                </router-link>
                              </div>

                              <div class="content-list w-75">
                                <h5 class="mb-1">
                                  <router-link to="/detail-1">
                                    15 Unheard Ways To Achieve Greater Walker
                                  </router-link>
                                </h5>

                                <div class="date">21 Feb 2021</div>
                              </div>
                            </div>
                          </article>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="sidebar-item mb-4">
                  <h3 class="">Tags</h3>

                  <ul class="sidebar-tags d-flex flex-wrap gap-1">
                    <li>
                      <a href="#">Tour</a>
                    </li>

                    <li>
                      <a href="#">Rental</a>
                    </li>

                    <li>
                      <a href="#">City</a>
                    </li>

                    <li>
                      <a href="#">Yatch</a>
                    </li>

                    <li>
                      <a href="#">Activity</a>
                    </li>

                    <li>
                      <a href="#">Museum</a>
                    </li>

                    <li>
                      <a href="#">Beauty</a>
                    </li>

                    <li>
                      <a href="#">Classic</a>
                    </li>

                    <li>
                      <a href="#">Creative</a>
                    </li>

                    <li>
                      <a href="#">Designs</a>
                    </li>

                    <li>
                      <a href="#">Featured</a>
                    </li>

                    <li>
                      <a href="#">Free Style</a>
                    </li>

                    <li>
                      <a href="#">Programs</a>
                    </li>

                    <li>
                      <a href="#">Travel</a>
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

  <DiscountAction />

  <Footer />
</template>
