<script setup lang="ts">
import { ref, onMounted } from 'vue'

import Appbar from '../components/Appbar.vue'
import Banner2 from '../components/Banner2.vue'
import DiscountAction from '../components/DiscountAction.vue'
import Footer from '../components/Footer.vue'

import DestinationImage17 from 'assets/images/destination/destination17.jpg'
import DestinationImage514 from 'assets/images/destination/destination14.jpg'
import DestinationImage15 from 'assets/images/destination/destination15.jpg'
import DestinationImage5 from 'assets/images/destination/destination5.jpg'
import DestinationImage16 from 'assets/images/destination/destination16.jpg'
import DestinationImage4 from 'assets/images/destination/destination4.jpg'
import DestinationImage10 from 'assets/images/destination/destination10.jpg'
import DestinationImage11 from 'assets/images/destination/destination11.jpg'
import DestinationImage7 from 'assets/images/destination/destination7.jpg'

const topDestinationImages = ref([
  {
    id: 1,
    country: 'Italy',
    location: 'Caspian Valley',
    image: DestinationImage17,
    tour_available: 18
  },
  {
    id: 2,
    country: 'Japan',
    location: 'Tokyo',
    image: DestinationImage514,
    tour_available: 21
  },
  {
    id: 3,
    country: 'Russia',
    location: 'Moscow',
    image: DestinationImage15,
    tour_available: 15
  },
  {
    id: 4,
    country: 'Thailand',
    location: 'Bangkok',
    image: DestinationImage5,
    tour_available: 24
  },
  {
    id: 5,
    country: 'America',
    location: 'Florida',
    image: DestinationImage16,
    tour_available: 32
  },
  {
    id: 6,
    country: 'Indonesia',
    location: 'Bali',
    image: DestinationImage4,
    tour_available: 14
  },
  {
    id: 7,
    country: 'Italy',
    location: 'Caspian Valley',
    image: DestinationImage10,
    tour_available: 18
  },
  {
    id: 8,
    country: 'Japan',
    location: 'Tokyo',
    image: DestinationImage11,
    tour_available: 21
  },
  {
    id: 9,
    country: 'Russia',
    location: 'Moscow',
    image: DestinationImage7,
    tour_available: 15
  }
])

import axios from 'axios'
const bookings = ref<any[]>([])
const error = ref('')

onMounted(async () => {
  await fetchBookings()
})

const fetchBookings = async () => {
  try {
    const token = localStorage.getItem('auth_token')
    if (!token) return
    const res = await axios.get('http://localhost:8000/api/bookings', {
      headers: { Authorization: `Bearer ${token}` }
    })
    bookings.value = res.data.bookings || []
  } catch (e: any) {
    error.value = e.response?.data?.error || e.message
  }
}

const getDeparture = (flight: any) =>
  flight.itineraries?.[0]?.segments?.[0]?.departure?.iataCode || ''
const getArrival = (flight: any) => {
  const segments = flight.itineraries?.[0]?.segments
  return segments?.[segments.length - 1]?.arrival?.iataCode || ''
}
const formatDate = (dateStr: string) =>
  dateStr ? new Date(dateStr).toLocaleString() : ''

// Suppression d'une réservation
const deleteBooking = async (id: number) => {
  if (!confirm('Supprimer cette réservation ?')) return
  try {
    const token = localStorage.getItem('auth_token')
    await axios.delete(`http://localhost:8000/api/bookings/${id}`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    bookings.value = bookings.value.filter((b) => b.id !== id)
  } catch (e: any) {
    alert(e.response?.data?.error || 'Erreur lors de la suppression')
  }
}

function isExpired(dateStr: string): boolean {
  const today = new Date()
  const date = new Date(dateStr)
  return date < today
}

const iaResultList = ref<any[]>([])
</script>

<template>
  <Appbar />

  <Banner2 headline="Destination List" page-title="Destination Lists" />

  <section class="trending pb-0 pt-6">
    <div class="container">
      <div class="section-title mb-6 w-50 mx-auto text-center">
        <h4 class="mb-1 theme1">Mes vols réservés</h4>
        <h2 class="mb-1">
          <span class="theme">Vos réservations</span>
        </h2>
        <p v-if="!bookings.length">
          Vous n'avez pas encore réservé de vol. Découvrez nos destinations !
        </p>
      </div>

      <!-- Affichage des vols réservés -->
      <div v-if="bookings.length" class="row align-items-center">
        <div
          class="col-lg-6 col-md-8 mb-4"
          v-for="booking in bookings"
          :key="booking.id"
        >
          <div class="card shadow-sm p-3">
            <div class="d-flex justify-content-between align-items-center mb-2">
              <div>
                <span class="fw-bold text-primary">
                  {{ getDeparture(booking.flight_data) }}
                  <i class="fa fa-arrow-right mx-2"></i>
                  {{ getArrival(booking.flight_data) }}
                </span>
                <span class="ms-3 text-muted small">
                  Réservé le {{ formatDate(booking.created_at) }}
                </span>
              </div>
              <span class="fw-bold" style="font-size: 1.1em">
                {{ booking.flight_data.price?.grandTotal }}
                {{ booking.flight_data.price?.currency }}
              </span>
              <button
                class="btn btn-danger btn-sm ms-3"
                @click="deleteBooking(booking.id)"
              >
                Supprimer
              </button>
            </div>
            <div>
              <div
                v-for="(segment, idx) in booking.flight_data.itineraries?.[0]
                  ?.segments"
                :key="idx"
                class="small"
              >
                <i class="fa fa-plane"></i>
                {{ segment.departure.iataCode }} ({{
                  formatDate(segment.departure.at)
                }}) → {{ segment.arrival.iataCode }} ({{
                  formatDate(segment.arrival.at)
                }})
                <span class="text-muted ms-2">
                  {{ segment.carrierCode }} {{ segment.number }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Liste statique si pas de réservation -->
      <div v-if="!bookings.length" class="row align-items-center">
        <div
          class="col-lg-4 col-md-6 col-sm-6 mb-4"
          v-for="destination in topDestinationImages"
          :key="destination.id"
        >
          <div class="trend-item1">
            <div class="trend-image position-relative rounded">
              <img :src="destination.image" alt="image" />

              <div
                class="trend-content d-flex align-items-center justify-content-between position-absolute bottom-0 p-4 w-100 z-index"
              >
                <div class="trend-content-title">
                  <h5 class="mb-0">
                    <router-link to="/destination-detail" class="theme1">
                      {{ destination.country }}
                    </router-link>
                  </h5>

                  <h3 class="mb-0 white">
                    {{ destination.location }}
                  </h3>
                </div>

                <span class="white bg-theme p-1 px-2 rounded">
                  {{ destination.tour_available }} Tours
                </span>
              </div>

              <div class="color-overlay"></div>
            </div>
          </div>
        </div>
      </div>

      <ol>
        <li v-for="(hotel, i) in iaResultList" :key="i">
          <strong>{{ hotel.nom }}</strong> à {{ hotel.ville }} (Note:
          {{ hotel.note }}/10, Prix: {{ hotel.prix }} TND)<br />
          Intérêts: {{ hotel.interets }}<br />
          <a :href="hotel.lien" target="_blank">Voir l'hôtel</a>
          <!-- Notification si expiré -->
          <div
            v-if="hotel.date_expiration && isExpired(hotel.date_expiration)"
            class="alert alert-warning mt-2"
          >
            ⚠️ Cette réservation est expirée.
          </div>
        </li>
      </ol>
    </div>
  </section>

  <DiscountAction />

  <Footer />
</template>

<style scoped>
.alert-warning {
  background: #fff3cd;
  color: #856404;
  border: 1px solid #ffeeba;
  border-radius: 6px;
  padding: 8px 12px;
  margin-top: 6px;
  font-size: 0.98em;
}
</style>
