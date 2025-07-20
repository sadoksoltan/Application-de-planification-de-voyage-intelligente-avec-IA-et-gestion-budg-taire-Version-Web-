<script setup lang="ts">
import { onMounted, ref } from 'vue'
import Splide, { type Splide as TSplide } from '@splidejs/splide'
import '@splidejs/splide/css'

import Appbar from 'pages/components/Appbar.vue'
import Banner2 from 'pages/components/Banner2.vue'
import Footer from 'pages/components/Footer.vue'
import axios from '@/axios'

import BlogImage2 from 'images/blog/blog2.jpg'
import BlogImage3 from 'images/blog/blog3.jpg'
import BlogImage5 from 'images/blog/blog5.jpg'
import BlogImage7 from 'images/blog/blog7.jpg'
import BlogImage8 from 'images/blog/blog8.jpg'
import BlogImage9 from 'images/blog/blog9.jpg'
import BlogImage10 from 'images/blog/blog10.jpg'
import BlogImage11 from 'images/blog/blog11.jpg'
import ReviewerImage1 from 'images/reviewer/1.jpg'
import ReviewerImage2 from 'images/reviewer/2.jpg'
import ReviewerImage3 from 'images/reviewer/3.jpg'
import TrendingImage10 from 'images/trending/trending10.jpg'
import TrendingImage12 from 'images/trending/trending12.jpg'
import TrendingImage13 from 'images/trending/trending13.jpg'

const API_BASE_URL = 'http://localhost:8000'
interface ApiPost {
  id: number
  title: string
  description: string
  category: string
  image: string | null
  author: string
  published_date: string
}

const blogList = ref([
  {
    id: 1,
    title: 'Les 10 plages les plus paradisiaques de Tunisie',
    description:
      'Découvrez les plus belles plages pour vos vacances d’été : Sidi Bou Said, Mahdia, Djerba et plus encore.',
    category: 'Travel',
    image: BlogImage7,
    author: 'Sadok Soltane',
    published_date: 'May 20, 2025'
  },
  {
    id: 2,
    title: 'Mariage sur la plage : top des destinations romantiques',
    description:
      'Organisez un mariage inoubliable en bord de mer avec ces lieux de rêve entre Hammamet et Bizerte.',
    category: 'Wedding',
    image: BlogImage8,
    author: 'Nesrine Ch.',
    published_date: 'April 18, 2025'
  },
  {
    id: 3,
    title: 'Top 8 hébergements insolites au Canada',
    description:
      'Cabane dans les arbres, igloo de luxe ou chalet sur lac ? Voici nos coups de cœur.',
    category: 'Travel',
    image: BlogImage2,
    author: 'Alex Turner',
    published_date: 'March 30, 2025'
  },
  {
    id: 4,
    title: 'Les gadgets à emporter pour un road trip réussi',
    description:
      'Du chargeur solaire à la glacière connectée, voici notre sélection pour les aventuriers.',
    category: 'Electronic',
    image: BlogImage3,
    author: 'Lina H.',
    published_date: 'May 10, 2025'
  },
  {
    id: 5,
    title: 'Bien-être en voyage : astuces pour rester zen',
    description:
      'Yoga matinal, spa naturels et nourriture saine pour vos vacances en toute sérénité.',
    category: 'Health',
    image: BlogImage9,
    author: 'Dr. Manel T.',
    published_date: 'May 3, 2025'
  },
  {
    id: 6,
    title: 'Voyager avec style : les tendances 2025',
    description:
      'Looks inspirants, sacs pratiques et vêtements éco-responsables pour globe-trotters.',
    category: 'Fashion',
    image: BlogImage10,
    author: 'Rania F.',
    published_date: 'April 5, 2025'
  },
  {
    id: 7,
    title: 'Cuisine du monde : 7 plats à goûter absolument',
    description:
      'De la street food thaï à la paella espagnole, partez en voyage culinaire sans bouger.',
    category: 'Food',
    image: BlogImage11,
    author: 'Yassine B.',
    published_date: 'March 28, 2025'
  },
  {
    id: 8,
    title: 'Écotourisme : les plus beaux jardins et parcs',
    description:
      'Explorez les espaces verts du monde entier en mode durable et responsable.',
    category: 'Public',
    image: BlogImage3,
    author: 'Sarah M.',
    published_date: 'April 11, 2025'
  },
  {
    id: 9,
    title: 'Tech & voyage : 5 apps pour planifier votre prochain trip',
    description:
      'Applications de vol, météo, itinéraire… ne partez plus jamais sans elles.',
    category: 'Tech',
    image: BlogImage5,
    author: 'Omar Z.',
    published_date: 'May 1, 2025'
  }
])

// Articles dynamiques depuis l'API admin
const apiPosts = ref<ApiPost[]>([])
const loading = ref(true)

const fetchPosts = async () => {
  loading.value = true
  try {
    const { data } = await axios.get('/api/posts') // <-- ici !
    apiPosts.value = data
  } catch (e) {
    apiPosts.value = []
  } finally {
    loading.value = false
  }
}

const blogPostsLIst = ref([
  {
    id: 1,
    title:
      'Comment deux développeurs de Deutsche Bank travaillent à distance avec succès',
    category: 'Technology',
    description:
      'Découvrez comment une bonne organisation et des outils numériques permettent de rester productif à distance.',
    image: TrendingImage10,
    author: {
      name: 'Sollmond Nell',
      image: ReviewerImage2
    }
  },
  {
    id: 2,
    title: 'Une coureuse autiste inspire des milliers de femmes dans le monde',
    category: 'Inspiration',
    description:
      "L’histoire émouvante d'une athlète qui dépasse ses limites et inspire toute une génération.",
    image: TrendingImage12,
    author: {
      name: 'David Scott',
      image: ReviewerImage1
    }
  },
  {
    id: 3,
    title: 'Développez votre business en ligne avec l’affiliation',
    category: 'Public',
    description:
      'Guide pratique pour utiliser l’affiliation afin de générer des revenus passifs en voyageant.',
    image: TrendingImage13,
    author: {
      name: 'John Bolden',
      image: ReviewerImage3
    }
  },
  {
    id: 4,
    title: 'Les outils indispensables pour les développeurs nomades',
    category: 'Technology',
    description:
      'Travailler en remote depuis Bali ? Voici notre sélection de plateformes pour rester efficace n’importe où.',
    image: TrendingImage10,
    author: {
      name: 'Sollmond Nell',
      image: ReviewerImage2
    }
  }
])

let splide: TSplide

onMounted(() => {
  fetchPosts()
  splide = new Splide('#blog-carousel', {
    arrows: false,
    autoplay: true,
    drag: true,
    gap: '2rem',
    perPage: 3,
    pagination: false,
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

const prev = () => splide.go('<')
const next = () => splide.go('>')
</script>

<template>
  <Appbar />

  <Banner2 page-title="Blog List Leftsidebar" headline="Blog List" />

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
                    <div
                      class="change-list f-active me-2 rounded overflow-hidden"
                    >
                      <router-link to="/post-list">
                        <i class="fa fa-bars"></i>
                      </router-link>
                    </div>
                    <div class="change-grid me-2 rounded overflow-hidden">
                      <router-link to="post-grid-1">
                        <i class="fa fa-th bg-grey"></i>
                      </router-link>
                    </div>
                    <div
                      class="sortby d-flex input-box align-items-center justify-content-between ml-2"
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

              <!-- Articles dynamiques (admin) -->
              <div
                class="blog-full d-flex mb-4 border-b bg-white box-shadow p-4 rounded border-all"
                v-for="blog in apiPosts"
                :key="'api-' + blog.id"
              >
                <div class="row w-100">
                  <div class="col-lg-5 col-md-4 blog-height">
                    <div class="blog-image rounded">
                      <router-link
                        :to="`/post/${blog.id}`"
                        :style="{
                          backgroundImage: blog.image
                            ? `url('${
                                blog.image.startsWith('http')
                                  ? blog.image
                                  : API_BASE_URL + '/storage/' + blog.image
                              }')`
                            : 'url(images/blog/blog2.jpg)'
                        }"
                      ></router-link>
                    </div>
                  </div>
                  <div class="col-lg-7 col-md-8">
                    <div class="blog-content">
                      <h5 class="theme mb-1">
                        {{ blog.category }}
                      </h5>
                      <h3 class="mb-2">
                        <router-link :to="`/post/${blog.id}`">
                          {{ blog.title }}
                        </router-link>
                      </h3>
                      <p class="date-cats mb-2">
                        <a href="#" class="me-2">
                          <i class="fa fa-file"></i>
                          {{ blog.category }}
                        </a>
                        <a href="#" class="me-2">
                          <i class="fa fa-calendar-alt"></i>
                          {{ blog.published_date }}
                        </a>
                        <a href="#">
                          <i class="fa fa-user"></i>
                          By {{ blog.author }}
                        </a>
                      </p>
                      <p class="mb-0">
                        {{ blog.description }}
                      </p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Articles statiques -->
              <div
                class="blog-full d-flex mb-4 border-b bg-white box-shadow p-4 rounded border-all"
                v-for="blog in blogList"
                :key="'static-' + blog.id"
              >
                <div class="row w-100">
                  <div class="col-lg-5 col-md-4 blog-height">
                    <div class="blog-image rounded">
                      <router-link
                        to="/detail-1"
                        :style="{
                          backgroundImage: `url(${blog.image})`
                        }"
                      ></router-link>
                    </div>
                  </div>
                  <div class="col-lg-7 col-md-8">
                    <div class="blog-content">
                      <h5 class="theme mb-1">
                        {{ blog.category }}
                      </h5>
                      <h3 class="mb-2">
                        <router-link to="/detail-1">
                          {{ blog.title }}
                        </router-link>
                      </h3>
                      <p class="date-cats mb-2">
                        <a href="#" class="me-2">
                          <i class="fa fa-file"></i>
                          Categories
                        </a>
                        <a href="#" class="me-2">
                          <i class="fa fa-calendar-alt"></i>
                          {{ blog.published_date }}
                        </a>
                        <a href="#">
                          <i class="fa fa-user"></i>
                          By {{ blog.author }}
                        </a>
                      </p>
                      <p class="mb-0">
                        {{ blog.description }}
                      </p>
                    </div>
                  </div>
                </div>
              </div>
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

        <!-- Sidebar identique à avant -->
        <div class="col-lg-4 ps-lg-4">
          <!-- ...sidebar code identique... -->
        </div>
      </div>
    </div>
  </section>

  <section class="top-post pt-0 pb-4">
    <div class="container">
      <div class="row align-items-center justify-content-between mb-6">
        <div class="col-lg-7">
          <div class="section-title text-center text-lg-start">
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
        </div>
        <div class="col-lg-5"></div>
      </div>

      <div class="row item-slider slick-initialized slick-slider">
        <button
          class="slick-prev slick-arrow d-none d-lg-block"
          aria-label="Previous"
          type="button"
          @click="prev"
        >
          Previous
        </button>

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
                          <div class="entry-button d-flex align-items-center">
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

        <button
          class="slick-next slick-arrow d-none d-lg-block"
          aria-label="Next"
          type="button"
          @click="next"
        >
          Next
        </button>
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
</style>
