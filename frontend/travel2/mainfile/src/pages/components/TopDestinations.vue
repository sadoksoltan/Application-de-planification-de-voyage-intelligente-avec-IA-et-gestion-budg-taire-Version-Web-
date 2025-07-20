<template>
  <section class="trending pb-5 pt-0">
    <div class="container">
      <div class="section-title mb-6 w-50 mx-auto text-center">
        <h4 class="mb-1 theme1">Top Destinations</h4>

        <h2 class="mb-1">
          Explore <span class="theme">Top Destinations</span>
        </h2>

        <p>
          Discover the most popular travel spots around the world, handpicked to
          offer you unforgettable experiences and breathtaking views.
        </p>
      </div>

      <div class="row align-items-center">
        <div class="col-lg-5 mb-4">
          <div class="trend-item1">
            <div class="trend-image position-relative rounded">
              <img src="images/destination/destination1.jpg" alt="image" />

              <div
                class="trend-content d-flex align-items-center justify-content-between position-absolute bottom-0 p-4 w-100 z-index"
              >
                <div class="trend-content-title">
                  <h5 class="mb-0">
                    <router-link to="/tour-grid" class="theme1">
                      England
                    </router-link>
                  </h5>

                  <h3 class="mb-0 white">London</h3>
                </div>

                <span class="white bg-theme p-1 px-2 rounded">15 Tours</span>
              </div>

              <div class="color-overlay"></div>
            </div>
          </div>
        </div>

        <div class="col-lg-7">
          <div class="row">
            <div class="col-lg-6 col-md-6 col-sm-6 mb-4">
              <div class="trend-item1">
                <div class="trend-image position-relative rounded">
                  <img src="images/destination/destination17.jpg" alt="image" />

                  <div
                    class="trend-content d-flex align-items-center justify-content-between position-absolute bottom-0 p-4 w-100 z-index"
                  >
                    <div class="trend-content-title">
                      <h5 class="mb-0">
                        <router-link to="/tour-grid" class="theme1">
                          Italy
                        </router-link>
                      </h5>

                      <h3 class="mb-0 white">Caspian Valley</h3>
                    </div>

                    <span class="white bg-theme p-1 px-2 rounded">
                      18 Tours
                    </span>
                  </div>

                  <div class="color-overlay"></div>
                </div>
              </div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6 mb-4">
              <div class="trend-item1">
                <div class="trend-image position-relative rounded">
                  <img src="images/destination/destination14.jpg" alt="image" />

                  <div
                    class="trend-content d-flex align-items-center justify-content-between position-absolute bottom-0 p-4 w-100 z-index"
                  >
                    <div class="trend-content-title">
                      <h5 class="mb-0">
                        <router-link to="/tour-grid" class="theme1">
                          Tokyo
                        </router-link>
                      </h5>

                      <h3 class="mb-0 white">Japan</h3>
                    </div>

                    <span class="white bg-theme p-1 px-2 rounded">
                      21 Tours
                    </span>
                  </div>

                  <div class="color-overlay"></div>
                </div>
              </div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6 mb-4">
              <div class="trend-item1">
                <div class="trend-image position-relative rounded">
                  <img src="images/destination/destination15.jpg" alt="image" />

                  <div
                    class="trend-content d-flex align-items-center justify-content-between position-absolute bottom-0 p-4 w-100"
                  >
                    <div class="trend-content-title">
                      <h5 class="mb-0">
                        <router-link to="/tour-grid" class="theme1">
                          Moscow
                        </router-link>
                      </h5>

                      <h3 class="mb-0 white">Russia</h3>
                    </div>

                    <span class="white bg-theme p-1 px-2 rounded">
                      15 Tours
                    </span>
                  </div>

                  <div class="color-overlay"></div>
                </div>
              </div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6 mb-4">
              <div class="trend-item1">
                <div class="trend-image position-relative rounded">
                  <img src="images/destination/destination16.jpg" alt="image" />

                  <div
                    class="trend-content d-flex align-items-center justify-content-between position-absolute bottom-0 p-4 w-100 z-index"
                  >
                    <div class="trend-content-title">
                      <h5 class="mb-0">
                        <router-link to="/tour-grid" class="theme1">
                          Florida
                        </router-link>
                      </h5>

                      <h3 class="mb-0 white">America</h3>
                    </div>

                    <span class="white bg-theme p-1 px-2 rounded">
                      32 Tours
                    </span>
                  </div>

                  <div class="color-overlay"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
