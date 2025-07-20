<script setup lang="ts">
import Shape2Image from 'images/shape2.png'
</script>

<template>
  <section
    class="trending pb-0 pt-6"
    :style="`background-image: url('${Shape2Image}')`"
  >
    <div class="container">
      <div class="section-title mb-6 w-75 mx-auto text-center">
        <h4 class="mb-1 theme1">Top Deals</h4>

        <h2 class="mb-1">
          The Last
          <span class="theme">Minute Deals</span>
        </h2>

        <p>
          Discover the beauty of the world around you, immerse yourself in
          diverse cultures, and create lasting memories through your travels.
          Embrace every moment as an opportunity for growth and adventure.
        </p>
      </div>

      <div class="trend-box">
        <div class="row">
          <div class="col-lg-5 mb-4">
            <div class="trend-item1 rounded box-shadow mb-4">
              <div class="trend-image position-relative">
                <img
                  src="images/trending/trendingb-2.jpg"
                  alt="image"
                  class=""
                />

                <div class="trend-content1 p-4">
                  <h5 class="theme1 mb-1">
                    <i class="flaticon-location-pin"></i>
                    Norway
                  </h5>

                  <h3 class="mb-1 white">
                    <router-link to="/tour-grid" class="white">
                      Norway Lake
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

                    <span class="ms-2 white">(16)</span>
                  </div>

                  <div
                    class="entry-meta d-flex align-items-center justify-content-between"
                  >
                    <div class="entry-author d-flex align-items-center">
                      <p class="mb-0 white">
                        <span class="theme1 fw-bold fs-5">$180.00</span>
                        | Per person
                      </p>
                    </div>

                    <div class="entry-author">
                      <i class="icon-calendar white"></i>
                      <span class="fw-bold white ms-1">6 Days Tours</span>
                    </div>
                  </div>
                </div>

                <div class="overlay"></div>
              </div>
            </div>

            <div class="trend-item1 rounded box-shadow mb-4">
              <div class="trend-image position-relative">
                <img
                  src="images/trending/trending-large.jpg"
                  alt="image"
                  class=""
                />

                <div class="trend-content1 p-4">
                  <h5 class="theme1 mb-1">
                    <i class="flaticon-location-pin"></i>
                    Egpyt
                  </h5>

                  <h3 class="mb-1">
                    <router-link to="/tour-grid" class="white">
                      Pyramid Land
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

                    <span class="ms-2 white">(16)</span>
                  </div>

                  <div
                    class="entry-meta d-flex align-items-center justify-content-between"
                  >
                    <div class="entry-author d-flex align-items-center">
                      <p class="mb-0 white">
                        <span class="theme1 fw-bold fs-5">$180.00</span>
                        | Per person
                      </p>
                    </div>

                    <div class="entry-author">
                      <i class="icon-calendar white"></i>
                      <span class="fw-bold white ms-1">6 Days Tours</span>
                    </div>
                  </div>
                </div>

                <div class="overlay"></div>
              </div>
            </div>

            <div class="trend-item1 rounded box-shadow">
              <div class="trend-image position-relative">
                <img
                  src="images/trending/trendingb-1.jpg"
                  alt="image"
                  class=""
                />

                <div class="trend-content1 p-4">
                  <h5 class="theme1 mb-1">
                    <i class="flaticon-location-pin"></i> Usa
                  </h5>

                  <h3 class="mb-1">
                    <router-link to="/tour-grid" class="white">
                      New York City
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

                    <span class="ms-2 white">(12)</span>
                  </div>

                  <div
                    class="entry-meta d-flex align-items-center justify-content-between"
                  >
                    <div class="entry-author d-flex align-items-center">
                      <p class="mb-0 white">
                        <span class="theme1 fw-bold fs-5"> $140.00</span>
                        | Per person
                      </p>
                    </div>

                    <div class="entry-author">
                      <i class="icon-calendar white"></i>
                      <span class="fw-bold white ms-1">3 Days Tours</span>
                    </div>
                  </div>
                </div>

                <div class="overlay"></div>
              </div>
            </div>
          </div>

          <div class="col-lg-7">
            <div class="row">
              <div class="col-lg-6 col-md-6 mb-4">
                <div class="trend-item rounded box-shadow">
                  <div class="trend-image position-relative">
                    <img
                      src="images/trending/trending1.jpg"
                      alt="image"
                      class=""
                    />
                    <div class="color-overlay"></div>
                  </div>

                  <div
                    class="trend-content p-4 pt-5 position-relative bg-white"
                  >
                    <div class="trend-meta bg-theme white px-3 py-2 rounded">
                      <div class="entry-author">
                        <i class="icon-calendar"></i>
                        <span class="fw-bold">4 Days Tours</span>
                      </div>
                    </div>

                    <h5 class="theme mb-1">
                      <i class="flaticon-location-pin"></i> Spain
                    </h5>

                    <h3 class="mb-1">
                      <router-link to="/tour-grid">
                        Barcelona city beach
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

                      <span class="ms-2">(21)</span>
                    </div>

                    <p class="border-b pb-2 mb-2">
                      Explore new horizons, embrace different cultures, and
                      create unforgettable memories.
                    </p>

                    <div class="entry-meta">
                      <div class="entry-author d-flex align-items-center">
                        <p class="mb-0">
                          <span class="theme fw-bold fs-5">$220.00</span>
                          | Per person
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-lg-6 col-md-6 mb-4">
                <div class="trend-item rounded box-shadow">
                  <div class="trend-image position-relative">
                    <img
                      src="images/trending/trending2.jpg"
                      alt="image"
                      class=""
                    />
                    <div class="color-overlay"></div>
                  </div>

                  <div
                    class="trend-content p-4 pt-5 position-relative bg-white"
                  >
                    <div class="trend-meta bg-theme white px-3 py-2 rounded">
                      <div class="entry-author">
                        <i class="icon-calendar"></i>
                        <span class="fw-bold">7 Days Tours</span>
                      </div>
                    </div>

                    <h5 class="theme mb-1">
                      <i class="flaticon-location-pin"></i>
                      Indonesia
                    </h5>

                    <h3 class="mb-1">
                      <router-link to="/tour-grid">Bali Province</router-link>
                    </h3>

                    <div class="rating-main d-flex align-items-center pb-2">
                      <div class="rating d-flex gap-1">
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                      </div>

                      <span class="ms-2">(11)</span>
                    </div>

                    <p class="border-b pb-2 mb-2">
                      Discover the beauty of the world around you, immerse
                      yourself in diverse cultures, and create lasting memories
                      through your travels. Embrace every moment as an
                      opportunity for growth and adventure.
                    </p>

                    <div class="entry-meta">
                      <div class="entry-author d-flex align-items-center">
                        <p class="mb-0">
                          <span class="theme fw-bold fs-5"> $210.00</span> | Per
                          person
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-lg-6 col-md-6 mb-4">
                <div class="trend-item rounded box-shadow">
                  <div class="trend-image position-relative">
                    <img
                      src="images/trending/trending3.jpg"
                      alt="image"
                      class=""
                    />
                    <div class="color-overlay"></div>
                  </div>

                  <div
                    class="trend-content p-4 pt-5 position-relative bg-white"
                  >
                    <div class="trend-meta bg-theme white px-3 py-2 rounded">
                      <div class="entry-author">
                        <i class="icon-calendar"></i>
                        <span class="fw-bold">3 Days Tours</span>
                      </div>
                    </div>

                    <h5 class="theme mb-1">
                      <i class="flaticon-location-pin"></i> Russia
                    </h5>

                    <h3 class="mb-1">
                      <router-link to="/tour-grid">Red City Land</router-link>
                    </h3>

                    <div class="rating-main d-flex align-items-center pb-2">
                      <div class="rating d-flex gap-1">
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                      </div>

                      <span class="ms-2">(25)</span>
                    </div>

                    <p class="border-b pb-2 mb-2">
                      Explore new horizons, embrace different cultures, and
                      create unforgettable memories.
                    </p>

                    <div class="entry-meta">
                      <div class="entry-author d-flex align-items-center">
                        <p class="mb-0">
                          <span class="theme fw-bold fs-5"> $120.00</span> | Per
                          person
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-lg-6 col-md-6 mb-4">
                <div class="trend-item rounded box-shadow">
                  <div class="trend-image position-relative">
                    <img
                      src="images/trending/trending4.jpg"
                      alt="image"
                      class=""
                    />
                    <div class="color-overlay"></div>
                  </div>

                  <div
                    class="trend-content p-4 pt-5 position-relative bg-white"
                  >
                    <div class="trend-meta bg-theme white px-3 py-2 rounded">
                      <div class="entry-author">
                        <i class="icon-calendar"></i>

                        <span class="fw-bold">5 Days Tours</span>
                      </div>
                    </div>

                    <h5 class="theme mb-1">
                      <i class="flaticon-location-pin"></i> Bangladesh
                    </h5>

                    <h3 class="mb-1">
                      <router-link to="/tour-grid">
                        Cox's bazar Beach
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
                      <span class="ms-2">(32)</span>
                    </div>

                    <p class="border-b pb-2 mb-2">
                      Explore new horizons, embrace different cultures, and
                      create unforgettable memories.
                    </p>

                    <div class="entry-meta">
                      <div class="entry-author d-flex align-items-center">
                        <p class="mb-0">
                          <span class="theme fw-bold fs-5">$100.00</span>
                          | Per person
                        </p>
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
</template>
