<script setup lang="ts">
import SectionBG1Image from 'images/section-bg1.png'
import Shape8Image from 'images/shape8.png'
</script>

<template>
  <section
    class="discount-action pt-6"
    style="background-position: center"
    :style="`background-image: url('${SectionBG1Image}')`"
  >
    <div
      class="section-shape section-shape1 top-inherit bottom-0"
      :style="`background-image: url('${Shape8Image}')`"
    ></div>

    <div class="container">
      <div class="call-banner rounded pt-10 pb-14">
        <div class="call-banner-inner w-75 mx-auto text-center px-5">
          <div class="trend-content-main">
            <div class="trend-content mb-5 pb-2 px-5">
              <h5 class="mb-1 theme">Love Where Your're Going</h5>

              <h2>
                Explore Your Life,
                <span class="theme1"> Travel Where You Want!</span>
              </h2>

              <p>
                Discover the beauty of the world around you, immerse yourself in
                diverse cultures, and create lasting memories through your
                travels. Embrace every moment as an opportunity for growth and
                adventure.
              </p>
            </div>

            <div class="video-button text-center position-relative">
              <div class="call-button text-center">
                <button
                  type="button"
                  class="play-btn js-video-button"
                  data-video-id="870769596"
                  data-channel="vimeo"
                >
                  <i class="fa fa-play bg-blue"></i>
                </button>
              </div>

              <div class="video-figure"></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="white-overlay"></div>
  </section>
</template>
