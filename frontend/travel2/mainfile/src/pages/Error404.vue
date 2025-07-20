<script setup lang="ts">
import Appbar from 'pages/components/Appbar.vue'
import Footer from 'pages/components/Footer.vue'
</script>

<template>
  <Appbar />

  <section class="error overflow-hidden pb-10">
    <div class="container">
      <div class="error-content text-center">
        <h2 class="mb-2">Oops! Page not found</h2>

        <img src="images/404-1.svg" alt="" class="mb-4 w-75 mx-auto" />

        <h3 class="m-0">
          we are sorry, but the page you requested was not found
        </h3>

        <div class="error-btn mt-4">
          <router-link to="/" class="nir-btn me-2">GO TO HOMEPAGE</router-link>

          <router-link to="/contact" class="nir-btn">
            GO TO CONTACT PAGE
          </router-link>
        </div>
      </div>
    </div>
  </section>

  <Footer />
</template>
