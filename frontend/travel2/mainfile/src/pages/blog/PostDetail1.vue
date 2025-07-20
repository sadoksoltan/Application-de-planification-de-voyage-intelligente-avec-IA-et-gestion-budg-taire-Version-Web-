<script setup lang="ts">
import { onMounted, ref } from 'vue'
import Splide from '@splidejs/splide'
import '@splidejs/splide/css'

import Appbar from 'pages/components/Appbar.vue'
import Footer from 'pages/components/Footer.vue'

import ReviewerImage1 from 'images/reviewer/1.jpg'
import ReviewerImage2 from 'images/reviewer/2.jpg'
import ReviewerImage3 from 'images/reviewer/3.jpg'
import TrendingImage10 from 'images/trending/trending10.jpg'
import TrendingImage12 from 'images/trending/trending12.jpg'
import TrendingImage13 from 'images/trending/trending13.jpg'

const blogPostsLIst = ref([
  {
    id: 1,
    title: 'How a developer duo at Deutsche Bank keep remote alive.',
    category: 'Techonology',
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod',
    image: TrendingImage10,
    author: {
      name: 'Sollmond Nell',
      image: ReviewerImage2
    }
  },
  {
    id: 2,
    title: "Inspire Runner with Autism Graces of Women's Running",
    category: 'Inspiration',
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod',
    image: TrendingImage12,
    author: {
      name: 'David Scott',
      image: ReviewerImage1
    }
  },
  {
    id: 3,
    title: 'Services To Grow Your Business Sell Affiliate Products',
    category: 'Pubilc',
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod',
    image: TrendingImage13,
    author: {
      name: 'Jonh Bolden',
      image: ReviewerImage3
    }
  },
  {
    id: 4,
    title: 'How a developer duo at Deutsche Bank keep remote alive.',
    category: 'Techonology',
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod',
    image: TrendingImage10,
    author: {
      name: 'Sollmond Nell',
      image: ReviewerImage2
    }
  }
])

onMounted(() => {
  new Splide('#blog-carousel', {
    arrows: false,
    autoplay: true,
    drag: true,
    gap: '2rem',
    pagination: false,
    perPage: 3,
    speed: 1500,
    type: 'loop',
    breakpoints: {
      768: {
        perPage: 1
      },
      1200: {
        perPage: 2
      }
    }
  }).mount()
})
</script>

<template>
  <Appbar />

  <div class="page-cover pt-10 pb-10 bg-lgrey border-b">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6 mb-4">
          <div class="cover-content text-center text-md-start">
            <div class="author-detail mb-2">
              <a href="#" class="tag white bg-theme py-1 px-3 me-2 rounded">
                #Technology
              </a>

              <a href="#" class="tag py-1 px-3">
                <i class="fa fa-eye"></i> 2500
              </a>
            </div>

            <h1 class="lh-sm">
              Apple honors eight developers with annual Apple Design Awards.
            </h1>

            <div class="author-detail d-flex align-items-center">
              <span class="me-3">
                <a href="#">
                  <i class="fa fa-clock"></i>
                  Posted On : 12 May 2021
                </a>
              </span>

              <span class="me-3">
                <a href="#">
                  <i class="fa fa-user"></i>
                  Jack Richard
                </a>
              </span>

              <span>
                <a href="#"> <i class="fa fa-comments"></i> 50 </a>
              </span>
            </div>
          </div>
        </div>

        <div class="col-lg-6 mb-4">
          <div class="box-shadow p-3 position-relative">
            <img
              alt="Image"
              class="w-100 rounded"
              src="images/trending/trending6.jpg"
            />

            <div
              class="video-button text-center position-absolute top-50 start-0 end-0 z-index1"
            >
              <div class="call-button text-center">
                <button
                  type="button"
                  class="play-btn js-video-button"
                  data-video-id="152879427"
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
  </div>

  <section class="blog blog-left pt-10">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-12 col-sm-12">
          <div class="blog-single">
            <div
              class="blog-single-in d-md-flex align-items-center mb-4 text-center text-md-start"
            >
              <div class="blog-date me-4">
                <div class="date text-center bg-theme p-5 py-4 rounded">
                  <h2 class="day mb-0 white">11</h2>

                  <div class="month white">May</div>
                </div>
              </div>

              <div class="blog-single-in-cont w-75">
                <div class="blog-content">
                  <h2 class="blog-title mb-0">
                    <router-link to="#">
                      Winners are recognized for outstanding app design
                    </router-link>
                  </h2>
                </div>
              </div>
            </div>

            <div class="blog-wrapper">
              <div class="blog-content">
                <div class="blog-imagelist mb-3">
                  <img src="images/bg/bg3.jpg" alt="image" class="rounded" />
                </div>

                <p class="mb-3">
                  Lorem ipsum dolor sit amet, consectetur adipis Vi ales elit
                  vitae lo bortis faucibus. Lorem ipsum dolor sit amet, conse
                  dolor sit amet, consectetu ctetur adipis Viales. Lorem ipsum
                  dolor sit amet, cons sit amet, consectetur adi ectetur adipis
                  Vi.
                  <br /><br />
                  It is a long established fact that a reader will be distracted
                  by the readable content of a page when looking at its layout.
                  The point of using Lorem Ipsum is that it has a more-or-less
                  normal distribution of letters, as opposed to using 'Content
                  here, content here', making it look like readable English.
                  Many desktop publishing packages and web page editors now use
                  Lorem Ipsum as their default model text, and a search for
                  'lorem ipsum' will uncover many web sites still in their
                  infancy.
                </p>
              </div>

              <!-- blog blockquote -->
              <div class="blog-quote mb-4 rounded">
                <p class="white">
                  “To take a trivial example, which ever undertakes laborious
                  physical work exercise, except obtain some advantage blinded”
                </p>

                <span class="white">By Michael Delwell</span>

                <i class="fas fa-quote-left"></i>
              </div>

              <div class="blog-imagelist mb-4">
                <div class="row">
                  <div class="col-md-6 col-sm-6 col-xs-12">
                    <img
                      src="images/trending/trending4.jpg"
                      alt="image"
                      class="rounded"
                    />
                  </div>

                  <div class="col-md-6 col-sm-6 col-xs-12">
                    <img
                      src="images/trending/trending2.jpg"
                      alt="image"
                      class="rounded"
                    />
                  </div>
                </div>
              </div>

              <p class="mb-4">
                as opposed to using 'Content here, content here', making it look
                like readable English. Many desktop publishing packages and web
                page editors now use Lorem Ipsum as their default model text,
                and a search for 'lorem ipsum' will uncover many web sites still
                in their infancy.
              </p>

              <!-- blog share -->
              <div
                class="blog-share d-flex justify-content-between align-items-center mb-4 bg-lgrey border rounded"
              >
                <div class="blog-share-tag">
                  <ul class="inline">
                    <li>
                      <strong>Posted In:</strong>
                    </li>

                    <li>
                      <a href="#">Fashion,</a>
                    </li>

                    <li>
                      <a href="#">Beauty,</a>
                    </li>

                    <li>
                      <a href="#">Vacation,</a>
                    </li>

                    <li>
                      <a href="#">Travel,</a>
                    </li>

                    <li>
                      <a href="#">News</a>
                    </li>
                  </ul>
                </div>

                <div class="header-social">
                  <ul class="d-flex gap-1">
                    <li>
                      <a href="#">
                        <i class="fab fa-facebook-f"></i>
                      </a>
                    </li>

                    <li>
                      <a href="#">
                        <i class="fab fa-google-plus-g"></i>
                      </a>
                    </li>

                    <li>
                      <a href="#">
                        <i class="fab fa-twitter"></i>
                      </a>
                    </li>

                    <li>
                      <a href="#"><i class="fab fa-linkedin-in"></i></a>
                    </li>
                  </ul>
                </div>
              </div>

              <!-- author detail -->
              <div class="blog-author mb-4 bg-grey border rounded">
                <div class="blog-author-item">
                  <div
                    class="row d-flex justify-content-between align-items-center"
                  >
                    <div class="col-md-3 col-sm-3 col-xs-12">
                      <div class="blog-thumb text-center position-relative">
                        <img src="images/reviewer/1.jpg" alt="" />
                      </div>
                    </div>

                    <div class="col-md-9 col-sm-9 col-xs-12">
                      <h3 class="title pink">
                        <a href="#">
                          About Author <span>Graphic Designer</span>
                        </a>
                      </h3>

                      <p class="m-0">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                        Vivamus sceler neque in euismod. Nam vitae urnasodales
                        neque in faucibus.
                      </p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- blog next prev -->
              <div class="blog-next mb-4 d-sm-flex align-items-center rounded">
                <a href="#" class="d-block bg-theme">
                  <div class="prev ps-4">
                    <i class="fa fa-arrow-left white"></i>

                    <p class="m-0 white">Previous Post</p>

                    <p class="m-0 white">The bedding was hardly able</p>
                  </div>
                </a>

                <a href="#" class="d-block bg-grey">
                  <div class="next pr-4 text-right">
                    <i class="fa fa-arrow-right"></i>

                    <p class="m-0">Previous Post</p>

                    <p class="m-0">The bedding was hardly able</p>
                  </div>
                </a>
              </div>

              <!-- blog comment list -->
              <div class="single-comments single-box mb-4">
                <h4 class="mb-4">Showing 16 verified guest comments</h4>

                <div class="comment-box">
                  <div class="comment-image mt-2">
                    <img src="images/reviewer/1.jpg" alt="image" />
                  </div>

                  <div class="comment-content rounded">
                    <h4 class="mb-1 Soldman Kell">Soldman Kell</h4>

                    <p class="comment-date">April 25, 2019 at 10:46 am</p>

                    <div class="comment-rate">
                      <div class="rating">
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                      </div>

                      <span class="comment-title">"The worst hotel ever"</span>
                    </div>

                    <p class="comment">
                      Take in the iconic skyline and visit the neighbourhood
                      hangouts that you've only ever seen on TV. Take in the
                      iconic skyline and visit the neighbourhood.
                    </p>

                    <div class="comment-like">
                      <div class="like-title float-left">
                        <a href="#" class="nir-btn mr-2">Reply</a>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="comment-box">
                  <div class="comment-image mt-2">
                    <img src="images/reviewer/2.jpg" alt="image" />
                  </div>

                  <div class="comment-content rounded">
                    <h4 class="mb-1">Burson Lesson</h4>

                    <p class="comment-date">April 25, 2019 at 10:46 am</p>

                    <div class="comment-rate">
                      <div class="rating">
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                      </div>

                      <span class="comment-title">
                        "Was too noisy and not suitable for business meetings"
                      </span>
                    </div>

                    <p class="comment">
                      Take in the iconic skyline and visit the neighbourhood
                      hangouts that you've only ever seen on TV. Take in the
                      iconic skyline and visit the neighbourhood.
                    </p>

                    <div class="comment-like">
                      <div class="like-title float-left">
                        <a href="#" class="nir-btn">Reply</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- blog review -->
              <div class="single-add-review">
                <h4 class="">Write a Review</h4>
                <form @submit.prevent="() => {}">
                  <div class="row">
                    <div class="col-lg-6">
                      <div class="form-group mb-2">
                        <input type="text" placeholder="Name" />
                      </div>
                    </div>

                    <div class="col-lg-6">
                      <div class="form-group mb-2">
                        <input type="email" placeholder="Email" />
                      </div>
                    </div>

                    <div class="col-lg-12 mb-1">
                      <div class="form-group">
                        <textarea>Comment</textarea>
                      </div>
                    </div>

                    <div class="col-lg-6">
                      <div class="form-btn">
                        <a href="#" class="nir-btn">Submit Review</a>
                      </div>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>

        <!-- sidebar starts -->
        <div class="col-lg-4 col-md-12">
          <div class="sidebar-sticky">
            <div class="list-sidebar">
              <div
                class="author-news mb-4 box-shadow border-all p-5 text-center rounded"
              >
                <div class="author-news-content">
                  <div class="author-thumb mb-1">
                    <img src="images/team/img2.jpg" alt="author" />
                  </div>

                  <div class="author-content">
                    <h3 class="title mb-1">
                      <a href="#">Relson Dulux</a>
                    </h3>

                    <p class="mb-2">
                      Hello, We're content writer who is fascinated by content
                      fashion, celebrity and lifestyle. We helps clients bring
                      the right content to the right people.
                    </p>

                    <div class="header-social">
                      <ul class="d-flex justify-content-center gap-1">
                        <li>
                          <a href="#">
                            <i class="fab fa-facebook-f"></i>
                          </a>
                        </li>

                        <li>
                          <a href="#">
                            <i class="fab fa-google-plus-g"></i>
                          </a>
                        </li>

                        <li>
                          <a href="#">
                            <i class="fab fa-twitter"></i>
                          </a>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>

              <div class="sidebar-item mb-4">
                <h4 class="">All Categories</h4>

                <ul class="sidebar-category">
                  <li>
                    <a href="#">All</a>
                  </li>

                  <li>
                    <a href="#">Featured</a>
                  </li>

                  <li>
                    <a href="#">Sliders</a>
                  </li>

                  <li class="active">
                    <a href="#">Manage Listings</a>
                  </li>

                  <li>
                    <a href="#">Address and Map</a>
                  </li>

                  <li>
                    <a href="#">Reservation Requests</a>
                  </li>

                  <li>
                    <a href="#">Your Reservation</a>
                  </li>

                  <li>
                    <a href="#">Search Results</a>
                  </li>
                </ul>
              </div>

              <div class="popular-post sidebar-item mb-4">
                <div class="sidebar-tabs">
                  <div class="post-tabs">
                    <ul
                      class="nav nav-tabs nav-pills nav-fill"
                      id="postsTab1"
                      role="tablist"
                    >
                      <li class="nav-item d-inline-block" role="presentation">
                        <button
                          role="tab"
                          type="button"
                          id="popular-tab"
                          data-bs-toggle="tab"
                          aria-selected="false"
                          class="nav-link active black"
                          data-bs-target="#popular"
                        >
                          Popular
                        </button>
                      </li>

                      <li class="nav-item d-inline-block" role="presentation">
                        <button
                          role="tab"
                          type="button"
                          id="recent-tab"
                          class="nav-link black"
                          aria-selected="true"
                          data-bs-toggle="tab"
                          data-bs-target="#recent"
                        >
                          Recent
                        </button>
                      </li>
                    </ul>

                    <div class="tab-content" id="postsTabContent1">
                      <div
                        id="popular"
                        role="tabpanel"
                        aria-labelledby="popular-tab"
                        class="tab-pane fade active show"
                      >
                        <article class="post mb-2 border-b pb-2">
                          <div
                            class="s-content d-flex align-items-center justify-space-between"
                          >
                            <div class="sidebar-image w-25 me-3 rounded">
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

                        <article class="post border-b pb-2 mb-2">
                          <div
                            class="s-content d-flex align-items-center justify-space-between"
                          >
                            <div class="sidebar-image w-25 me-3 rounded">
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

                        <article class="post mb-2 border-b pb-2">
                          <div
                            class="s-content d-flex align-items-center justify-space-between"
                          >
                            <div class="sidebar-image w-25 me-3 rounded">
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

                        <article class="post">
                          <div
                            class="s-content d-flex align-items-center justify-space-between"
                          >
                            <div class="sidebar-image w-25 me-3 rounded">
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

                      <!-- Recent posts -->
                      <div
                        id="recent"
                        role="tabpanel"
                        class="tab-pane fade"
                        aria-labelledby="recent-tab"
                      >
                        <article class="post mb-2 border-b pb-2">
                          <div
                            class="s-content d-flex align-items-center justify-space-between"
                          >
                            <div class="sidebar-image w-25 me-3 rounded">
                              <router-link to="/detail-1">
                                <img
                                  src="images/trending/trending5.jpg"
                                  alt=""
                                />
                              </router-link>
                            </div>

                            <div class="content-list w-75">
                              <h5 class="mb-1">
                                <router-link to="/detail-1">
                                  10 Ways To Immediately Start Selling Furniture
                                </router-link>
                              </h5>

                              <div class="date">08 Mar 2021</div>
                            </div>
                          </div>
                        </article>

                        <article class="post border-b pb-2 mb-2">
                          <div
                            class="s-content d-flex align-items-center justify-space-between"
                          >
                            <div class="sidebar-image w-25 me-3 rounded">
                              <router-link to="/detail-1">
                                <img
                                  src="images/trending/trending6.jpg"
                                  alt=""
                                />
                              </router-link>
                            </div>

                            <div class="content-list w-75">
                              <h5 class="mb-1">
                                <router-link to="/detail-1">
                                  Photography Photo modify and Beautiful Walker
                                </router-link>
                              </h5>

                              <div class="date">18 Jan 2021</div>
                            </div>
                          </div>
                        </article>

                        <article class="post mb-2 border-b pb-2">
                          <div
                            class="s-content d-flex align-items-center justify-space-between"
                          >
                            <div class="sidebar-image w-25 me-3 rounded">
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

                        <article class="post">
                          <div
                            class="s-content d-flex align-items-center justify-space-between"
                          >
                            <div class="sidebar-image w-25 me-3 rounded">
                              <router-link to="/detail-1">
                                <img
                                  src="images/trending/trending3.jpg"
                                  alt=""
                                />
                              </router-link>
                            </div>

                            <div class="content-list w-75">
                              <h5 class="mb-1">
                                <router-link to="/detail-1">
                                  1Certified Graphic Design with Free Project
                                  Course
                                </router-link>
                              </h5>

                              <div class="date">12 Feb 2021</div>
                            </div>
                          </div>
                        </article>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="sidebar-item mb-4">
                <h4 class="">Tags</h4>

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
  </section>

  <section class="trending recent-articles pb-6 pt-0">
    <div class="container">
      <div class="section-title mb-6 w-75 mx-auto text-center">
        <h4 class="mb-1 theme1">Our Blogs Offers</h4>

        <h2 class="mb-1">
          Recent
          <span class="theme">Articles &amp; Posts</span>
        </h2>

        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore.
        </p>
      </div>

      <div class="recent-articles-inner">
        <div class="row">
          <div class="row item-slider slick-initialized slick-slider">
            <div class="splide" id="blog-carousel" aria-label="Recent Articles">
              <div class="splide__track">
                <ul class="splide__list">
                  <li
                    class="splide__slide"
                    v-for="blog in blogPostsLIst"
                    :key="blog.id"
                  >
                    <div
                      class="w-100 slick-slide slick-cloned"
                      tabindex="-1"
                      aria-hidden="true"
                      style="width: 442px"
                    >
                      <div
                        class="trend-item box-shadow bg-white mb-4 rounded overflow-hidden"
                      >
                        <div class="trend-image">
                          <img :src="blog.image" alt="image" />
                        </div>

                        <div class="trend-content-main p-4">
                          <div class="trend-content">
                            <h5 class="theme mb-1">
                              {{ blog.category }}
                            </h5>

                            <h4>
                              <router-link to="/detail-1" tabindex="-1">
                                {{ blog.title }}
                              </router-link>
                            </h4>

                            <p class="mb-3">
                              {{ blog.description }}
                            </p>

                            <div
                              class="entry-meta d-flex align-items-center justify-content-between"
                            >
                              <div class="entry-author">
                                <img
                                  alt="Image"
                                  class="rounded-circle me-1"
                                  :src="blog.author.image"
                                />

                                <span>{{ blog.author.name }}</span>
                              </div>

                              <div
                                class="entry-button d-flex align-items-center"
                              >
                                <a href="#" class="nir-btn" tabindex="-1">
                                  Read More
                                </a>
                              </div>
                            </div>
                          </div>
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
  </section>

  <OurPartners2 style="padding-top: 0" />

  <Footer />
</template>
