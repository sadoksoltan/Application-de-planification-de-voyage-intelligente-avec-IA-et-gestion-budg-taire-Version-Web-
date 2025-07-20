<script setup lang="ts">
import ImageViewer from 'awesome-image-viewer'

import Appbar from 'pages/components/Appbar.vue'
import Banner2 from 'pages/components/Banner2.vue'
import DiscountAction from 'pages/components/DiscountAction.vue'
import Footer from 'pages/components/Footer.vue'

import Trending3Image from 'images/trending/trending3.jpg'
import Trending2Image from 'images/trending/trending2.jpg'
import Trending4Image from 'images/trending/trending4.jpg'
import Trending5Image from 'images/trending/trending5.jpg'
import Trending6Image from 'images/trending/trending6.jpg'
import Destination4Image from 'images/destination/destination4.jpg'
import Destination3Image from 'images/destination/destination3.jpg'
import Destination10Image from 'images/destination/destination10.jpg'

function showImage(idx: number) {
  new ImageViewer({
    images: [
      { mainUrl: Trending3Image },
      { mainUrl: Destination10Image },
      { mainUrl: Trending2Image },
      { mainUrl: Trending4Image },
      { mainUrl: Trending6Image },
      { mainUrl: Trending4Image },
      { mainUrl: Destination4Image },
      { mainUrl: Trending5Image },
      { mainUrl: Destination3Image }
    ],
    currentSelected: idx
  })
}
</script>

<template>
  <Appbar />

  <Banner2 page-title="Gallery Masonary" />

  <div class="gallery pb-0 pt-6">
    <div class="container">
      <div class="section-title mb-6 text-center w-75 mx-auto">
        <h4 class="mb-1 theme1">Our Gallery</h4>

        <h2 class="mb-1">
          Some Beautiful
          <span class="theme"> Snapshoots</span>
        </h2>

        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore.
        </p>
      </div>

      <div class="row blog-main">
        <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12 mansonry-item">
          <div class="gallery-item mb-4 rounded overflow-hidden">
            <div class="gallery-image">
              <img src="images/trending/trending3.jpg" alt="image" />

              <div class="overlay"></div>
            </div>

            <div class="gallery-content">
              <h5
                class="white text-center position-absolute bottom-0 pb-4 left-50 mb-0 w-100"
              >
                Barcelona - Spain
              </h5>

              <ul>
                <li @click="showImage(0)">
                  <a href="#">
                    <i class="fa fa-eye"></i>
                  </a>
                </li>

                <li>
                  <a href="#">
                    <i class="fa fa-link"></i>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12 mansonry-item">
          <div class="gallery-item mb-4 rounded overflow-hidden">
            <div class="gallery-image">
              <img src="images/destination/destination10.jpg" alt="image" />

              <div class="overlay"></div>
            </div>

            <div class="gallery-content">
              <h5
                class="white text-center position-absolute bottom-0 pb-4 left-50 mb-0 w-100"
              >
                Moscow - Russia
              </h5>

              <ul>
                <li @click="showImage(1)">
                  <a href="#">
                    <i class="fa fa-eye"></i>
                  </a>
                </li>

                <li>
                  <a href="#">
                    <i class="fa fa-link"></i>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12 mansonry-item">
          <div class="gallery-item mb-4 rounded overflow-hidden">
            <div class="gallery-image">
              <img src="images/trending/trending2.jpg" alt="image" />
              <div class="overlay"></div>
            </div>
            ]

            <div class="gallery-content">
              <h5
                class="white text-center position-absolute bottom-0 pb-4 left-50 mb-0 w-100"
              >
                Bangkok - Thailand
              </h5>

              <ul>
                <li @click="showImage(2)">
                  <a href="#">
                    <i class="fa fa-eye"></i>
                  </a>
                </li>

                <li>
                  <a href="#">
                    <i class="fa fa-link"></i>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12 mansonry-item">
          <div class="gallery-item mb-4 rounded overflow-hidden">
            <div class="gallery-image">
              <img src="images/trending/trending4.jpg" alt="image" />

              <div class="overlay"></div>
            </div>

            <div class="gallery-content">
              <h5
                class="white text-center position-absolute bottom-0 pb-4 left-50 mb-0 w-100"
              >
                FLorida - USA
              </h5>

              <ul>
                <li @click="showImage(3)">
                  <a href="#">
                    <i class="fa fa-eye"></i>
                  </a>
                </li>

                <li>
                  <a href="#">
                    <i class="fa fa-link"></i>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12 mansonry-item">
          <div class="gallery-item mb-4 rounded overflow-hidden">
            <div class="gallery-image">
              <img src="images/trending/trending4.jpg" alt="image" />

              <div class="overlay"></div>
            </div>

            <div class="gallery-content">
              <h5
                class="white text-center position-absolute bottom-0 pb-4 left-50 mb-0 w-100"
              >
                Tokyo - Japan
              </h5>

              <ul>
                <li @click="showImage(5)">
                  <a href="#">
                    <i class="fa fa-eye"></i>
                  </a>
                </li>

                <li>
                  <a href="#">
                    <i class="fa fa-link"></i>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12 mansonry-item">
          <div class="gallery-item mb-4 rounded overflow-hidden">
            <div class="gallery-image">
              <img src="images/trending/trending6.jpg" alt="image" />

              <div class="overlay"></div>
            </div>

            <div class="gallery-content">
              <h5
                class="white text-center position-absolute bottom-0 pb-4 left-50 mb-0 w-100"
              >
                Bali - Indonesia
              </h5>

              <ul>
                <li @click="showImage(4)">
                  <a href="#">
                    <i class="fa fa-eye"></i>
                  </a>
                </li>

                <li>
                  <a href="#">
                    <i class="fa fa-link"></i>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12 mansonry-item">
          <div class="gallery-item mb-4 rounded overflow-hidden">
            <div class="gallery-image">
              <img src="images/destination/destination4.jpg" alt="image" />

              <div class="overlay"></div>
            </div>

            <div class="gallery-content">
              <h5
                class="white text-center position-absolute bottom-0 pb-4 left-50 mb-0 w-100"
              >
                Bangkok - Thailand
              </h5>

              <ul>
                <li @click="showImage(6)">
                  <a href="#">
                    <i class="fa fa-eye"></i>
                  </a>
                </li>

                <li>
                  <a href="#">
                    <i class="fa fa-link"></i>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12 mansonry-item">
          <div class="gallery-item mb-4 rounded overflow-hidden">
            <div class="gallery-image">
              <img src="images/destination/destination3.jpg" alt="image" />

              <div class="overlay"></div>
            </div>

            <div class="gallery-content">
              <h5
                class="white text-center position-absolute bottom-0 pb-4 left-50 mb-0 w-100"
              >
                Bangkok - Thailand
              </h5>

              <ul>
                <li @click="showImage(8)">
                  <a href="#">
                    <i class="fa fa-eye"></i>
                  </a>
                </li>

                <li>
                  <a href="#">
                    <i class="fa fa-link"></i>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12 mansonry-item">
          <div class="gallery-item mb-4 rounded overflow-hidden">
            <div class="gallery-image">
              <img src="images/trending/trending5.jpg" alt="image" />

              <div class="overlay"></div>
            </div>

            <div class="gallery-content">
              <h5
                class="white text-center position-absolute bottom-0 pb-4 left-50 mb-0 w-100"
              >
                Tokyo - Japan
              </h5>

              <ul>
                <li @click="showImage(7)">
                  <a href="#">
                    <i class="fa fa-eye"></i>
                  </a>
                </li>

                <li>
                  <a href="#">
                    <i class="fa fa-link"></i>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <DiscountAction />

  <Footer />
</template>
