<script setup lang="ts">
import LoginRegister from './LoginRegister.vue'
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'
import axios from '@/axios'

const isAuthenticated = ref(false)
const router = useRouter()

const showProfileMenu = ref(false)
const name = ref('') // Utilise "name" au lieu de "username"
const role = ref('')

const showToast = (message: string, isSuccess: boolean = true) => {
  Toastify({
    text: message,
    duration: 3000,
    close: true,
    gravity: 'top',
    position: 'center',
    backgroundColor: isSuccess ? '#4CAF50' : '#f44336',
    stopOnFocus: true,
    style: {
      borderRadius: '20px'
    }
  }).showToast()
}

const checkAuthStatus = () => {
  const urlParams = new URLSearchParams(window.location.search)
  const token = urlParams.get('token')
  const user = localStorage.getItem('name') // Utilise "name"
  let userRole = localStorage.getItem('role')

  // Correction: forcer la casse et supprimer les espaces
  if (userRole) {
    userRole = userRole.trim().toLowerCase()
  }

  if (token) {
    localStorage.setItem('auth_token', token)
    isAuthenticated.value = true
  } else {
    isAuthenticated.value = !!localStorage.getItem('auth_token')
  }
  if (isAuthenticated.value && user) {
    name.value = user
    role.value = userRole || ''
  }
}

const handleLogout = async () => {
  try {
    const token = localStorage.getItem('auth_token')
    if (!token) {
      console.error('No authentication token found!')
      return
    }

    await axios.post(
      '/api/logout',
      {},
      {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    )

    showToast('You have been logged out successfully.')
    localStorage.removeItem('auth_token')
    localStorage.removeItem('name')
    localStorage.removeItem('role')
    isAuthenticated.value = false
    name.value = ''
    role.value = ''
    router.push('/login')
  } catch (error: any) {
    if (error.response?.data?.message === 'Unauthenticated.') {
      showToast('You are already logged out.')
      localStorage.removeItem('auth_token')
      localStorage.removeItem('name')
      localStorage.removeItem('role')
      isAuthenticated.value = false
      name.value = ''
      role.value = ''
      router.push('/login')
    } else {
      showToast('Logout failed. Please try again.', false)
    }
  }
}

const handleProfileLogout = async () => {
  showProfileMenu.value = false
  await handleLogout()
}

function handleClickOutside(event: MouseEvent) {
  const dropdown = document.querySelector('.profile-dropdown')
  if (dropdown && !dropdown.contains(event.target as Node)) {
    showProfileMenu.value = false
  }
}

onMounted(() => {
  checkAuthStatus()
  document.addEventListener('click', handleClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})

const searchView = ref(false)
const toggleNavView = ref(false)

function handleSearch() {
  searchView.value = !searchView.value
}

function handleToggleNavView() {
  toggleNavView.value = !toggleNavView.value
}
</script>

<template>
  <LoginRegister />

  <div id="search1" :class="{ open: searchView }" @click.self="handleSearch">
    <button type="button" class="close" @click="handleSearch">X</button>
    <form @submit.prevent="() => {}">
      <input type="search" placeholder="type keyword(s) here" />
      <button type="submit" class="btn btn-primary">Search</button>
    </form>
  </div>

  <header class="main_header_area">
    <div class="header-content py-1 bg-theme">
      <div class="container d-flex align-items-center justify-content-between">
        <div class="links">
          <ul>
            <li>
              <a href="#" class="white">
                <i class="icon-calendar white"></i>
                Thursday, Avr 26, 2025
              </a>
            </li>
            <li>
              <a href="#" class="white">
                <i class="icon-location-pin white"></i>
                Monastir, Tunisia
              </a>
            </li>
            <li>
              <a href="#" class="white">
                <i class="icon-clock white"></i>
                Mon-Fri: 10 AM - 5 PM
              </a>
            </li>
          </ul>
        </div>

        <div class="links float-right">
          <ul>
            <li>
              <a href="#" class="white">
                <i class="fab fa-facebook" aria-hidden="true"></i>
              </a>
            </li>
            <li>
              <a href="#" class="white">
                <i class="fab fa-twitter" aria-hidden="true"></i>
              </a>
            </li>
            <li>
              <a href="#" class="white">
                <i class="fab fa-instagram" aria-hidden="true"></i>
              </a>
            </li>
            <li>
              <a href="#" class="white">
                <i class="fab fa-linkedin" aria-hidden="true"></i>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div class="header_menu" id="header_menu">
      <nav class="navbar navbar-expand-lg navbar-default">
        <div class="container">
          <div
            class="navbar-flex d-flex align-items-center gap-4 gap-xl-0 justify-content-between w-100 pb-3 pt-3"
          >
            <div class="navbar-header">
              <router-link to="/" class="navbar-brand">
                <img src="images/logo.png" alt="image" />
              </router-link>
            </div>

            <div>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul
                  class="nav navbar-nav d-flex flex-wrap"
                  id="responsive-menu"
                >
                  <li class="nav-item">
                    <router-link to="/">Home</router-link>
                  </li>
                  <li class="nav-item">
                    <router-link to="/about">About Us</router-link>
                  </li>
                  <li class="submenu dropdown nav-item">
                    <a
                      href="#"
                      role="button"
                      aria-haspopup="true"
                      aria-expanded="false"
                      data-toggle="dropdown"
                      class="dropdown-toggle"
                    >
                      Destinations
                      <i class="icon-arrow-down" aria-hidden="true"></i>
                    </a>
                    <ul class="dropdown-menu">
                      <li>
                        <router-link to="/destination-list"
                          >Destination List</router-link
                        >
                      </li>
                      <li>
                        <router-link to="/destination-detail"
                          >Destination Detail</router-link
                        >
                      </li>
                    </ul>
                  </li>
                  <li class="submenu dropdown nav-item">
                    <a
                      href="#"
                      role="button"
                      aria-haspopup="true"
                      aria-expanded="false"
                      data-toggle="dropdown"
                      class="dropdown-toggle"
                    >
                      Tours
                      <i class="icon-arrow-down" aria-hidden="true"></i>
                    </a>
                    <ul class="dropdown-menu">
                      <li>
                        <router-link to="/tour-list">Tour List</router-link>
                        <router-link to="/tour-grid">Tour Grid</router-link>
                        <router-link to="/tour-single">Tour Single</router-link>
                      </li>
                    </ul>
                  </li>
                  <li class="submenu dropdown nav-item">
                    <a
                      href="#"
                      role="button"
                      aria-haspopup="true"
                      aria-expanded="false"
                      class="dropdown-toggle"
                      data-toggle="dropdown"
                    >
                      Pages
                      <i class="icon-arrow-down" aria-hidden="true"></i>
                    </a>
                    <ul class="dropdown-menu">
                      <li>
                        <router-link to="/team">Our Guide</router-link>
                      </li>
                      <li>
                        <router-link to="/booking">Booking</router-link>
                      </li>
                      <li>
                        <router-link to="/confirmation"
                          >Confirmation</router-link
                        >
                      </li>
                      <li class="submenu dropdown">
                        <router-link
                          role="button"
                          to="/services"
                          aria-haspopup="true"
                          aria-expanded="false"
                          data-toggle="dropdown"
                          class="dropdown-toggle"
                        >
                          Services
                          <i class="fa fa-angle-right" aria-hidden="true"></i>
                        </router-link>
                        <ul class="dropdown-menu">
                          <li>
                            <router-link to="/services"
                              >Services Lists</router-link
                            >
                          </li>
                          <li>
                            <router-link to="/service-detail"
                              >Service Detail</router-link
                            >
                          </li>
                        </ul>
                      </li>
                      <li>
                        <router-link to="/gallery1">Gallery</router-link>
                      </li>
                      <li>
                        <router-link to="/404">Error</router-link>
                      </li>
                      <!-- <li>
                        <router-link to="/login">Login|Register</router-link>
                      </li> -->
                      <li>
                        <router-link to="/comingsoon">Coming Soon</router-link>
                      </li>
                      <li>
                        <router-link to="/testimonial">Testimonial</router-link>
                      </li>
                      <li>
                        <router-link to="/faq">FAQ</router-link>
                      </li>
                      <li>
                        <router-link to="/contact">Contact Us</router-link>
                      </li>
                    </ul>
                  </li>
                  <li class="submenu dropdown">
                    <a
                      href="#"
                      role="button"
                      aria-haspopup="true"
                      aria-expanded="false"
                      data-toggle="dropdown"
                      class="dropdown-toggle"
                    >
                      Blog
                      <i class="icon-arrow-down" aria-hidden="true"></i>
                    </a>
                    <ul class="dropdown-menu">
                      <li class="submenu dropdown">
                        <router-link to="/post-grid-1">Blog Grid</router-link>
                        <router-link to="/post-list-1">Blog List</router-link>
                      </li>
                    </ul>
                  </li>
                  <li class="search-main" @click="handleSearch">
                    <a href="#" class="mt_search">
                      <i class="fa fa-search"></i>
                    </a>
                  </li>
                </ul>
              </div>
            </div>

            <div @click="handleToggleNavView">
              <button
                class="navbar-toggler"
                type="button"
                aria-controls="navbarSupportedContent"
                aria-expanded="false"
                aria-label="Toggle navigation"
              >
                <span class="navbar-toggler-icon"></span>
              </button>
            </div>

            <div class="register-login d-flex flex-shrink-0 align-items-center">
              <template v-if="isAuthenticated">
                <div class="profile-dropdown position-relative me-3">
                  <button
                    class="nir-btn white d-flex align-items-center"
                    style="
                      background: #10a7a7;
                      color: #fff;
                      border-radius: 15px;
                      border: none;
                      font-weight: 500;
                      padding: 6px 26px;
                    "
                    @click.stop="showProfileMenu = !showProfileMenu"
                  >
                    <i class="icon-user fs-6 me-2"></i>
                    <span style="font-size: 1rem">{{ name || 'Profile' }}</span>
                    <i class="fa fa-caret-down ms-2"></i>
                  </button>
                  <div
                    v-if="showProfileMenu"
                    class="dropdown-menu show"
                    style="
                      position: absolute;
                      right: 1;
                      min-width: 175px;
                      z-index: 1000;
                    "
                  >
                    <router-link
                      class="dropdown-item"
                      to="/profile"
                      @click="showProfileMenu = false"
                    >
                      Profile
                    </router-link>
                    <router-link
                      v-if="
                        role && role.toString().trim().toLowerCase() === 'admin'
                      "
                      class="dropdown-item"
                      to="/dashboard"
                      @click="showProfileMenu = false"
                    >
                      Dashboard
                    </router-link>
                    <button class="dropdown-item" @click="handleProfileLogout">
                      Logout
                    </button>
                  </div>
                </div>
              </template>
              <template v-else>
                <a
                  href="#"
                  class="me-3"
                  data-bs-toggle="modal"
                  data-bs-target="#exampleModal"
                >
                  <i class="icon-user"></i> Login/Register
                </a>
              </template>

              <router-link
                to="/booking"
                class="nir-btn white"
                style="
                  background: #10a7a7;
                  color: #fff;
                  border-radius: 15px;
                  border: none;
                  font-weight: 600;
                  padding: 10px 30px;
                "
              >
                Book Now
              </router-link>
            </div>
          </div>

          <div class="d-lg-none pb-2" v-if="toggleNavView">
            <div class="d-flex flex-wrap gap-2 px-2">
              <div>
                <router-link to="/">Home</router-link>
              </div>
              <div>
                <router-link to="/about">About Us</router-link>
              </div>
              <div class="dropdown">
                <span
                  aria-expanded="false"
                  class="dropdown-toggle"
                  data-bs-toggle="dropdown"
                >
                  Destinations
                </span>
                <div class="dropdown-menu px-2">
                  <div>
                    <router-link to="destination-list"
                      >Destination List</router-link
                    >
                  </div>
                  <div>
                    <router-link to="destination-detail"
                      >Destination Detail</router-link
                    >
                  </div>
                </div>
              </div>
              <div class="dropdown">
                <span
                  aria-expanded="false"
                  data-bs-toggle="dropdown"
                  class="dropdown-toggle"
                >
                  Tours
                </span>
                <div class="dropdown-menu px-2">
                  <div>
                    <router-link to="tour-list">Tour List</router-link>
                  </div>
                  <div>
                    <router-link to="tour-grid">Tour Grid</router-link>
                  </div>
                  <div>
                    <router-link to="tour-single">Tour Single</router-link>
                  </div>
                </div>
              </div>
              <div class="dropdown d-none d-sm-block d-lg-none">
                <span
                  aria-expanded="false"
                  data-bs-toggle="dropdown"
                  class="dropdown-toggle"
                >
                  Pages
                </span>
                <div class="dropdown-menu px-2">
                  <div>
                    <router-link to="/team">Our Guide</router-link>
                  </div>
                  <div>
                    <router-link to="/booking">Booking</router-link>
                  </div>
                  <div>
                    <router-link to="/confirmation">Confirmation</router-link>
                  </div>
                  <div>
                    <router-link to="services">Service Lists</router-link>
                  </div>
                  <div>
                    <router-link to="/service-detail"
                      >Service Details</router-link
                    >
                  </div>
                  <div>
                    <router-link to="/gallery1">Gallery</router-link>
                  </div>
                  <div>
                    <router-link to="/404">Error</router-link>
                  </div>
                  <div>
                    <router-link to="/login">Login/Register</router-link>
                  </div>
                  <div>
                    <router-link to="/comingsoon">Coming Soon</router-link>
                  </div>
                  <div>
                    <router-link to="/testimonial">Testimonial</router-link>
                  </div>
                  <div>
                    <router-link to="/faq">FAQ</router-link>
                  </div>
                  <div>
                    <router-link to="/contact">Contact Us</router-link>
                  </div>
                </div>
              </div>
              <div class="dropdown d-none d-sm-block d-lg-none">
                <span
                  aria-expanded="false"
                  data-bs-toggle="dropdown"
                  class="dropdown-toggle"
                >
                  Blogs
                </span>
                <div class="dropdown-menu px-2">
                  <div>
                    <router-link to="post-grid-1">Blog Grid</router-link>
                  </div>
                  <div>
                    <router-link to="post-list-1">Blog List</router-link>
                  </div>
                  <div>
                    <router-link to="detail-1">Blog Single</router-link>
                  </div>
                </div>
              </div>
            </div>

            <div class="d-flex d-sm-none px-2 gap-2">
              <div class="dropdown">
                <span
                  aria-expanded="false"
                  data-bs-toggle="dropdown"
                  class="dropdown-toggle"
                >
                  Pages
                </span>
                <div class="dropdown-menu px-2">
                  <div>
                    <router-link to="/team">Our Guide</router-link>
                  </div>
                  <div>
                    <router-link to="/booking">Booking</router-link>
                  </div>
                  <div>
                    <router-link to="/confirmation">Confirmation</router-link>
                  </div>
                  <div>
                    <router-link to="services">Service Lists</router-link>
                  </div>
                  <div>
                    <router-link to="/service-detail"
                      >Service Details</router-link
                    >
                  </div>
                  <div>
                    <router-link to="/gallery1">Gallery</router-link>
                  </div>
                  <div>
                    <router-link to="/404">Error</router-link>
                  </div>
                  <div>
                    <router-link to="/login">Login/Register</router-link>
                  </div>
                  <div>
                    <router-link to="/comingsoon">Coming Soon</router-link>
                  </div>
                  <div>
                    <router-link to="/testimonial">Testimonial</router-link>
                  </div>
                  <div>
                    <router-link to="/faq">FAQ</router-link>
                  </div>
                  <div>
                    <router-link to="/contact">Contact Us</router-link>
                  </div>
                </div>
              </div>
              <div class="dropdown">
                <span
                  aria-expanded="false"
                  data-bs-toggle="dropdown"
                  class="dropdown-toggle"
                >
                  Blogs
                </span>
                <div class="dropdown-menu px-2">
                  <div>
                    <router-link to="post-grid-1">Blog Grid</router-link>
                  </div>
                  <div>
                    <router-link to="post-list-1">Blog List</router-link>
                  </div>
                  <div>
                    <router-link to="detail-1">Blog Single</router-link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </div>
  </header>
</template>
