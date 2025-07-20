<script setup lang="ts">
import { ref, onMounted } from 'vue'

import Appbar from 'pages/components/Appbar.vue'
import Banner2 from 'pages/components/Banner2.vue'
import Footer from 'pages/components/Footer.vue'

import TrendingImage10 from 'images/trending/trending10.jpg'
import TrendingImage12 from 'images/trending/trending12.jpg'
import TrendingImage13 from 'images/trending/trending13.jpg'
import ReviewerImage1 from 'images/reviewer/1.jpg'
import ReviewerImage2 from 'images/reviewer/2.jpg'
import ReviewerImage3 from 'images/reviewer/3.jpg'

// AJOUT : import axios et image fallback
import axios from '@/axios'
import BlogImage2 from 'images/blog/blog2.jpg'

// AJOUT : interface pour les articles API
interface ApiPost {
  id: number
  title: string
  description: string
  category: string
  image: string | null
  author: string
  published_date: string
}

const API_BASE_URL = 'http://localhost:8000'

// AJOUT : articles dynamiques
const apiPosts = ref<ApiPost[]>([])
const loading = ref(true)

const fetchPosts = async () => {
  loading.value = true
  try {
    const { data } = await axios.get('/api/posts')
    apiPosts.value = data
  } catch (e) {
    apiPosts.value = []
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchPosts()
})

const blogList = ref([
  {
    id: 1,
    title: 'How a developer duo at Deutsche Bank keep remote alive.',
    description:
      'Explore new horizons, embrace different cultures, and create unforgettable memories.',
    category: 'Technology',
    image: TrendingImage10,
    author: {
      name: 'Sollmond Nell',
      image: ReviewerImage2
    }
  },
  {
    id: 2,
    title: "Inspire Runner with Autism Graces of Women's Running",
    description:
      'Explore new horizons, embrace different cultures, and create unforgettable memories.',
    category: 'Inspiration',
    image: TrendingImage12,
    author: {
      name: 'David Scott',
      image: ReviewerImage1
    }
  },
  {
    id: 3,
    title: "Inspire Runner with Autism Graces of Women's Running",
    description: 'Services To Grow Your Business Sell Affiliate Products',
    category: 'Public',
    image: TrendingImage13,
    author: {
      name: 'John Bolden',
      image: ReviewerImage3
    }
  },
  {
    id: 4,
    title: 'How a developer duo at Deutsche Bank keep remote alive.',
    description:
      'Explore new horizons, embrace different cultures, and create unforgettable memories.',
    category: 'Technology',
    image: TrendingImage10,
    author: {
      name: 'Sollmond Nell',
      image: ReviewerImage2
    }
  },
  {
    id: 5,
    title: "Inspire Runner with Autism Graces of Women's Running",
    description:
      'Explore new horizons, embrace different cultures, and create unforgettable memories.',
    category: 'Inspiration',
    image: TrendingImage12,
    author: {
      name: 'David Scott',
      image: ReviewerImage1
    }
  },
  {
    id: 6,
    title: "Inspire Runner with Autism Graces of Women's Running",
    description: 'Services To Grow Your Business Sell Affiliate Products',
    category: 'Public',
    image: TrendingImage13,
    author: {
      name: 'John Bolden',
      image: ReviewerImage3
    }
  },
  {
    id: 7,
    title: 'How a developer duo at Deutsche Bank keep remote alive.',
    description:
      'Explore new horizons, embrace different cultures, and create unforgettable memories.',
    category: 'Technology',
    image: TrendingImage10,
    author: {
      name: 'Sollmond Nell',
      image: ReviewerImage2
    }
  },
  {
    id: 8,
    title: "Inspire Runner with Autism Graces of Women's Running",
    description:
      'Explore new horizons, embrace different cultures, and create unforgettable memories.',
    category: 'Inspiration',
    image: TrendingImage12,
    author: {
      name: 'David Scott',
      image: ReviewerImage1
    }
  }
])
</script>

<template>
  <Appbar />

  <Banner2 page-title="Blog Grid Leftsidebar" headline="Blog Grid" />

  <section class="blog">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 pe-lg-4">
          <div class="listing-inner">
            <div class="row">
              <div class="col-lg-12">
                <div
                  class="list-results d-flex align-items-center justify-content-between"
                >
                  <div class="list-results-sort">
                    <p class="m-0">
                      <span v-if="!loading">
                        Showing 1-{{ blogList.length + apiPosts.length }} of
                        {{ blogList.length + apiPosts.length }} results
                      </span>
                      <span v-else>Chargement...</span>
                    </p>
                  </div>

                  <div
                    class="click-menu d-flex align-items-center justify-content-between"
                  >
                    <div class="change-list me-2 rounded overflow-hidden">
                      <router-link to="/post-list-1">
                        <i class="fa fa-bars bg-grey"></i>
                      </router-link>
                    </div>

                    <div
                      class="change-grid f-active me-2 rounded overflow-hidden"
                    >
                      <router-link to="/post-grid-1">
                        <i class="fa fa-th"></i>
                      </router-link>
                    </div>

                    <div
                      class="sortby input-box d-flex align-items-center justify-content-between ml-2"
                    >
                      <select class="niceSelect">
                        <option value="1">Sort By</option>
                        <option value="2">Average rating</option>
                        <option value="3">Price: low to high</option>
                        <option value="4">Price: high to low</option>
                      </select>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Articles dynamiques (API) -->
              <div
                class="col-lg-6"
                v-for="blog in apiPosts"
                :key="'api-' + blog.id"
              >
                <div
                  class="trend-item box-shadow bg-white mb-4 rounded overflow-hidden"
                >
                  <div class="trend-image">
                    <router-link :to="`/post/${blog.id}`">
                      <img
                        :src="
                          blog.image
                            ? blog.image.startsWith('http')
                              ? blog.image
                              : API_BASE_URL + '/storage/' + blog.image
                            : BlogImage2
                        "
                        alt="image"
                        class="w-100"
                      />
                    </router-link>
                  </div>
                  <div class="trend-content-main p-4 pb-2">
                    <div class="trend-content">
                      <h5 class="theme mb-1">{{ blog.category }}</h5>
                      <h4>
                        <router-link :to="`/post/${blog.id}`">
                          {{ blog.title }}
                        </router-link>
                      </h4>
                      <p class="mb-3">{{ blog.description }}</p>
                      <div
                        class="entry-meta d-flex align-items-center justify-content-between"
                      >
                        <div class="entry-author mb-2">
                          <i class="fa fa-user me-1"></i>
                          <span>{{ blog.author }}</span>
                        </div>
                        <div class="entry-date mb-2">
                          <i class="fa fa-calendar-alt me-1"></i>
                          <span>{{ blog.published_date }}</span>
                        </div>
                      </div>
                      <div class="eentry-button d-flex align-items-center mb-2">
                        <router-link :to="`/post/${blog.id}`" class="nir-btn"
                          >Read More</router-link
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <!-- Fin articles dynamiques -->

              <!-- Articles statiques -->
              <div class="col-lg-6" v-for="blog in blogList" :key="blog.id">
                <div
                  class="trend-item box-shadow bg-white mb-4 rounded overflow-hidden"
                >
                  <div class="trend-image">
                    <img :src="blog.image" alt="image" class="w-100" />
                  </div>
                  <div class="trend-content-main p-4 pb-2">
                    <div class="trend-content">
                      <h5 class="theme mb-1">
                        {{ blog.category }}
                      </h5>
                      <h4>
                        <router-link to="/detail-1">
                          {{ blog.title }}
                        </router-link>
                      </h4>
                      <p class="mb-3">
                        {{ blog.description }}
                      </p>
                      <div
                        class="entry-meta d-flex align-items-center justify-content-between"
                      >
                        <div class="entry-author mb-2">
                          <img
                            :src="blog.author.image"
                            alt=""
                            class="rounded-circle me-1"
                          />
                          <span>{{ blog.author.name }}</span>
                        </div>
                        <div
                          class="eentry-button d-flex align-items-center mb-2"
                        >
                          <a href="#" class="nir-btn">Read More</a>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <!-- Fin articles statiques -->
            </div>

            <div class="pagination-main text-center">
              <ul class="pagination">
                <li>
                  <a href="#">
                    <i class="fa fa-angle-double-left" aria-hidden="true"></i>
                  </a>
                </li>

                <li class="active">
                  <a href="#">1</a>
                </li>

                <li>
                  <a href="#">2</a>
                </li>

                <li>
                  <a href="#">3</a>
                </li>

                <li>
                  <a href="#">4</a>
                </li>

                <li>
                  <a href="#">
                    <i class="fa fa-angle-double-right" aria-hidden="true"></i>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="col-lg-4 ps-lg-4">
          <div class="sidebar-sticky">
            <div class="list-sidebar">
              <div class="sidebar-item">
                <h4 class="">Search Here</h4>

                <div
                  class="newsletter-form rounded overflow-hidden position-relative"
                >
                  <form @submit.prevent="() => {}">
                    <input
                      type="text"
                      placeholder="Search your keyword here.."
                    />

                    <input
                      type="submit"
                      class="nir-btn bordernone rounded-0 position-absolute end-0"
                      value="Search"
                    />
                  </form>
                </div>
              </div>

              <div
                class="author-news mb-4 box-shadow p-5 text-center rounded overflow-hidden border-all"
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
                            <i class="fab fa-facebook-f rounded"></i>
                          </a>
                        </li>

                        <li>
                          <a href="#">
                            <i class="fab fa-google-plus-g rounded"></i>
                          </a>
                        </li>

                        <li>
                          <a href="#"><i class="fab fa-twitter rounded"></i></a>
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

                <ul class="sidebar-tags d-flex gap-1 flex-wrap">
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

  <section class="featured-video pb-4 pt-0">
    <div class="container">
      <div class="section-title mb-6 text-center w-75 mx-auto">
        <h4 class="mb-1 theme1">Our Articles &amp; Blogs</h4>

        <h2 class="mb-1">
          Some Related
          <span class="theme">Posts</span>
        </h2>

        <p>
          Explore new horizons, embrace different cultures, and create
          unforgettable memories.
        </p>
      </div>

      <div class="featured-video-main">
        <div class="row">
          <div class="col-lg-6 mb-4">
            <div class="trend-item box-shadow bg-white rounded overflow-hidden">
              <div class="trend-image position-relative">
                <img
                  src="images/trending/trending14.jpg"
                  alt="image"
                  class="w-100"
                />

                <div
                  class="video-button text-center position-absolute top-50 w-100 mx-auto z-index3 start-50 translate-middle"
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

              <div class="trend-content-main">
                <div class="trend-content-main p-4 pb-2">
                  <div class="trend-content">
                    <h5 class="theme mb-1 d-inline-block">Inspiration</h5>

                    <h4>
                      <router-link to="/detail-1">
                        Our Main Inspire Runner with Autism Graces of Women's
                        Running
                      </router-link>
                    </h4>

                    <p class="mb-3">
                      Explore new horizons, embrace different cultures, and
                      create unforgettable memories.
                    </p>

                    <div
                      class="entry-meta d-flex align-items-center justify-content-between"
                    >
                      <div class="entry-author mb-2">
                        <img
                          src="images/reviewer/1.jpg"
                          alt=""
                          class="rounded-circle me-1"
                        />

                        <span>David Scott</span>
                      </div>

                      <div class="eentry-button d-flex align-items-center mb-2">
                        <a href="#" class="nir-btn">Read More</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="col-lg-6">
            <div class="row">
              <div class="col-lg-6 col-md-6 mb-4">
                <div
                  class="trend-item box-shadow bg-white rounded overflow-hidden"
                >
                  <div class="trend-image">
                    <img src="images/trending/trending10.jpg" alt="image" />
                  </div>

                  <div class="trend-content-main">
                    <div class="trend-content p-4">
                      <h5 class="theme mb-1">Design</h5>

                      <h4 class="mb-0">
                        <router-link to="detail-1">
                          Get Ready To Up Your Creative Game
                        </router-link>
                      </h4>
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-lg-6 col-md-6 mb-4">
                <div
                  class="trend-item box-shadow bg-white rounded overflow-hidden"
                >
                  <div class="trend-image">
                    <img src="images/trending/trending11.jpg" alt="image" />
                  </div>

                  <div class="trend-content-main">
                    <div class="trend-content p-4">
                      <h5 class="theme mb-1">Health</h5>

                      <h4 class="mb-0">
                        <router-link to="/detail-1">
                          Tradition design won't save us in the COVID
                        </router-link>
                      </h4>
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-lg-6 col-md-6 mb-4">
                <div
                  class="trend-item box-shadow bg-white rounded overflow-hidden"
                >
                  <div class="trend-image">
                    <img src="images/trending/trending13.jpg" alt="image" />
                  </div>

                  <div class="trend-content-main">
                    <div class="trend-content p-4">
                      <h5 class="theme mb-1">Foods</h5>

                      <h4 class="mb-0">
                        <router-link to="/detail-1">
                          The 1 Food that helps remote teams
                        </router-link>
                      </h4>
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-lg-6 col-md-6 mb-4">
                <div
                  class="trend-item box-shadow bg-white rounded overflow-hidden"
                >
                  <div class="trend-image">
                    <img src="images/trending/trending12.jpg" alt="image" />
                  </div>

                  <div class="trend-content-main">
                    <div class="trend-content p-4">
                      <h5 class="theme mb-1">Products</h5>

                      <h4 class="mb-0">
                        <router-link to="/detail-1">
                          New: Freehand Templates, built for all
                        </router-link>
                      </h4>
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

  <Footer />
</template>

<style scoped>
select {
  appearance: none;
  -moz-appearance: none;
  -webkit-appearance: none;
}

.input-box {
  position: relative;
}

.input-box::after {
  position: absolute;
  top: 55%;
  right: 1px;
  pointer-events: none;
  content: url('../../assets/chevron-down.svg');
  transform: translate(-50%, -50%);
}

.niceSelect:focus {
  border-color: #999;
}
.trend-image img {
  object-fit: cover;
  height: 250px;
}
</style>
