<script setup lang="ts">
import Appbar from './components/Appbar.vue'
import Banner from './components/Banner.vue'
import AboutUs from './components/AboutUs.vue'
import TopDestinations from './components/TopDestinations.vue'
import AboutUs2 from './components/AboutUs2.vue'
import BestTourPackage from './components/BestTourPackage.vue'
import LastMinuteDeals from './components/LastMinuteDeals.vue'
import DiscountAction from './components/DiscountAction.vue'
import OfferPackages from './components/OfferPackages.vue'
import OurTeam from './components/OurTeam.vue'
import Testimonial from './components/Testimonial.vue'
import RecentArticles from './components/RecentArticles.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <Appbar />

  <Banner />
  <div class="text-center mt-4">
    <router-link
      to="/travel-ia-tunisia"
      class="btn btn-lg btn-teal rounded-pill"
    >
      <i class="fa fa-robot me-2"></i>
      Essayez Travel.IA Tunisie
    </router-link>
  </div>

  <AboutUs />

  <TopDestinations />

  <AboutUs2 />

  <BestTourPackage />

  <LastMinuteDeals />

  <DiscountAction />

  <OfferPackages />

  <OurTeam />

  <Testimonial />

  <RecentArticles />

  <Footer />
</template>
