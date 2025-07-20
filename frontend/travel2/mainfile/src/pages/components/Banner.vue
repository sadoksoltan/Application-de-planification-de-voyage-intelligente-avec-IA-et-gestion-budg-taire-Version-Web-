<script setup lang="ts">
import { onMounted, ref } from 'vue'
import axios from 'axios'
import Splide from '@splidejs/splide'
import '@splidejs/splide/css'

import TestimonaiImage from 'images/testimonial.png'
import CampingImage from 'images/icons/004-camping-tent.png'
import HikingImage from 'images/icons/003-hiking.png'
import SunBedImage from 'images/icons/005-sunbed.png'
import SurfImage from 'images/icons/006-surf.png'
import SafariImage from 'images/icons/002-safari.png'
import CylingImage from 'images/icons/008-cycling.png'
import CityScapeImage from 'images/icons/001-cityscape.png'
import { useRouter } from 'vue-router'
const hotelQuery = ref('')
const hotelArrivalDate = ref('')
const hotelDepartureDate = ref('')
const hotelAdults = ref(1)
const hotels = ref<any[]>([])
const hotelLoading = ref(false)
const hotelError = ref('')
const router = useRouter()
const bannerList = ref([
  { id: 1, image: CampingImage, text: 'Camping' },
  { id: 2, image: HikingImage, text: 'Hiking' },
  { id: 3, image: SunBedImage, text: 'Beach Tours' },
  { id: 4, image: SurfImage, text: 'Surfing' },
  { id: 5, image: SafariImage, text: 'Safari' },
  { id: 6, image: CylingImage, text: 'Cycling' },
  { id: 7, image: CityScapeImage, text: 'Trekings' }
])

const iaCity = ref('')
const iaStartDate = ref('')
const iaEndDate = ref('')
const iaBudget = ref(1500)
const iaInterests = ref<string[]>([])
const iaLoading = ref(false)
const iaResult = ref('')
const iaError = ref('')
const resetTravelIA = () => {
  iaCity.value = ''
  iaStartDate.value = ''
  iaEndDate.value = ''
  iaBudget.value = 1500
  iaInterests.value = []
  iaResult.value = ''
  iaError.value = ''
}
const iaBannerList = [
  { id: 1, image: CampingImage, text: 'Camping' },
  { id: 2, image: HikingImage, text: 'Hiking' },
  { id: 3, image: SunBedImage, text: 'Beach Tours' },
  { id: 4, image: SurfImage, text: 'Surfing' },
  { id: 5, image: SafariImage, text: 'Safari' },
  { id: 6, image: CylingImage, text: 'Cycling' },
  { id: 7, image: CityScapeImage, text: 'Trekings' }
]

const toggleIaInterest = (interest: string) => {
  if (iaInterests.value.includes(interest)) {
    iaInterests.value = iaInterests.value.filter((i) => i !== interest)
  } else {
    iaInterests.value.push(interest)
  }
}

const searchTravelIA = async () => {
  iaLoading.value = true
  iaError.value = ''
  iaResult.value = ''
  try {
    const res = await axios.post('http://localhost:8000/api/ai/museums', {
      city: iaCity.value,
      start_date: iaStartDate.value,
      end_date: iaEndDate.value,
      budget: iaBudget.value,
      interests: iaInterests.value
    })
    iaResult.value =
      res.data.answer ||
      res.data.recommendations ||
      'Aucune suggestion trouvée.'
  } catch (e: any) {
    iaError.value =
      e.response?.data?.error || 'Erreur lors de la génération du plan'
  } finally {
    iaLoading.value = false
  }
}
const adults = ref(1)
const budget = ref(1500)
const interests = ref<string[]>([])
const selectedType = ref<'hotels' | 'flights' | 'travel-ia'>('flights')
const origin = ref('')
const destination = ref('')
const departureDate = ref('')
const travelType = ref('')
const tourDuration = ref('')
const loading = ref(false)
const flights = ref<any[]>([])
const error = ref('')
const dictionaries = ref<any>({})
const printResult = () => {
  window && window.print && window.print()
}
const toggleInterest = (interest: string) => {
  if (interests.value.includes(interest)) {
    interests.value = interests.value.filter((i) => i !== interest)
  } else {
    interests.value.push(interest)
  }
}
const searchHotels = async () => {
  hotelLoading.value = true
  hotelError.value = ''
  hotels.value = []
  const city = hotelQuery.value.split(',')[0].trim()
  try {
    const res = await axios.get('http://localhost:8000/api/hotels/search', {
      params: {
        query: city,
        arrival_date: hotelArrivalDate.value,
        departure_date: hotelDepartureDate.value,
        adults: hotelAdults.value
      }
    })
    hotels.value = res.data.data?.hotels || []
  } catch (e: any) {
    hotelError.value = e.response?.data?.error || 'Erreur lors de la recherche'
  } finally {
    hotelLoading.value = false
  }
}
const searchFlights = async () => {
  loading.value = true
  error.value = ''
  flights.value = []
  try {
    const res = await axios.get('http://localhost:8000/api/flights/search', {
      params: {
        origin: origin.value,
        destination: destination.value,
        departure_date: departureDate.value,
        adults: adults.value,
        budget: budget.value,
        travel_type: travelType.value,
        tour_duration: tourDuration.value,
        interests: interests.value
      }
    })
    // Filtrer ici côté front
    const allFlights = res.data.data || []
    flights.value = allFlights.filter(
      (f: { price?: { grandTotal?: string } }) =>
        Number(f.price?.grandTotal) <= budget.value
    )
    dictionaries.value = res.data.dictionaries || {}
  } catch (e: any) {
    error.value = e.response?.data?.error || 'Erreur lors de la recherche'
  } finally {
    loading.value = false
  }
}

const getDeparture = (flight: any) =>
  flight.itineraries[0]?.segments[0]?.departure.iataCode || ''
const getArrival = (flight: any) => {
  const segments = flight.itineraries[0]?.segments
  return segments?.[segments.length - 1]?.arrival.iataCode || ''
}
const formatDate = (dateStr: string) => new Date(dateStr).toLocaleString()
const bookFlight = async (flight: any) => {
  try {
    const token = localStorage.getItem('auth_token')
    if (!token || token === 'undefined') {
      alert('Vous devez être connecté pour réserver.')
      router.push('/login')
      return
    }
    await axios.post(
      'http://localhost:8000/api/bookings',
      { flight },
      {
        headers: { Authorization: `Bearer ${token}` }
      }
    )
    alert('Vol réservé avec succès !')
    router.push('/destination-list')
  } catch (e: any) {
    if (e.response?.status === 401) {
      alert('Session expirée, veuillez vous reconnecter.')
      router.push('/login')
    } else {
      alert(e.response?.data?.error || 'Erreur lors de la réservation')
    }
  }
}

const getCityName = (iata: string) => {
  if (!dictionaries.value.locations || !dictionaries.value.locations[iata])
    return iata
  const loc = dictionaries.value.locations[iata]
  return loc.cityName ? `${loc.cityName}, ${loc.countryCode}` : iata
}
const getCarrierName = (code: string) => {
  return dictionaries.value.carriers?.[code] || code
}
const getCarrierLogo = (code: string) => {
  return `https://content.airhex.com/content/logos/airlines_${code}_350_100_r.png`
}

onMounted(() => {
  new Splide('#banner-carousel', {
    arrows: false,
    autoplay: true,
    drag: true,
    interval: 5000,
    gap: '2rem',
    pagination: false,
    perPage: 6,
    speed: 1500,
    type: 'loop',
    breakpoints: {
      576: { perPage: 2 },
      768: { perPage: 3 },
      992: { perPage: 4 },
      1200: { perPage: 5 }
    }
  }).mount()
})
</script>

<template>
  <section
    class="banner pt-10 pb-0 overflow-hidden"
    :style="`background-image: url('${TestimonaiImage}')`"
  >
    <div class="container">
      <div class="banner-in">
        <div class="row align-items-center">
          <div class="col-lg-6 mb-4">
            <div class="banner-content text-lg-start text-center">
              <h4 class="theme mb-0">Explore the World</h4>
              <h1>Begin Crafting Your Perfect Journey Today</h1>
              <p class="mb-4">
                Discover new horizons and unforgettable experiences. Let us help
                you plan a personalized trip that turns your travel dreams into
                reality, effortlessly and confidently.
              </p>

              <div class="book-form">
                <div
                  class="row d-flex align-items-center justify-content-between"
                >
                  <!-- Boutons Hotels Flights Travel.IA -->
                  <div class="col-lg-12 mb-3">
                    <div
                      class="d-flex justify-content-center gap-4 booking-type"
                    >
                      <div
                        :class="[
                          'type-option',
                          selectedType === 'hotels' ? 'active' : ''
                        ]"
                        @click="selectedType = 'hotels'"
                      >
                        <i class="fa fa-bed me-1"></i> Hotels
                      </div>
                      <div
                        :class="[
                          'type-option',
                          selectedType === 'flights' ? 'active' : ''
                        ]"
                        @click="selectedType = 'flights'"
                      >
                        <i class="fa fa-plane me-1"></i> Flights
                      </div>
                      <div
                        :class="[
                          'type-option',
                          selectedType === 'travel-ia' ? 'active' : ''
                        ]"
                        @click="selectedType = 'travel-ia'"
                      >
                        <i class="fa fa-robot me-1"></i> Travel.IA
                      </div>
                    </div>
                  </div>

                  <div v-if="selectedType === 'hotels'" class="col-lg-12 mb-3">
                    <input
                      v-model="hotelQuery"
                      type="text"
                      placeholder="Enter hotel name or city"
                      class="form-control"
                    />
                    <input
                      v-model="hotelArrivalDate"
                      type="date"
                      class="form-control mt-2"
                      placeholder="Arrival date"
                    />
                    <input
                      v-model="hotelDepartureDate"
                      type="date"
                      class="form-control mt-2"
                      placeholder="Departure date"
                    />
                    <label class="mb-1 mt-2">Adults</label>
                    <div class="d-flex align-items-center gap-2">
                      <button
                        @click="hotelAdults > 1 && hotelAdults--"
                        class="counter-btn"
                      >
                        −
                      </button>
                      <span class="counter-value">{{ hotelAdults }}</span>
                      <button @click="hotelAdults++" class="counter-btn">
                        +
                      </button>
                    </div>
                    <button
                      @click="searchHotels"
                      class="nir-btn w-100 mt-3"
                      :disabled="hotelLoading"
                    >
                      <i class="fa fa-search mr-2"></i>
                      <span v-if="!hotelLoading">Search Hotels</span>
                      <span v-else>Searching...</span>
                    </button>
                    <div v-if="hotelError" class="alert alert-danger mt-3">
                      {{ hotelError }}
                    </div>
                    <!-- ...existing code... -->
                    <div v-if="hotels.length" class="hotels-list mt-4">
                      <div
                        v-for="(hotel, idx) in hotels"
                        :key="hotel.hotel_id || idx"
                        class="hotel-card row mb-4 p-0 rounded-4 overflow-hidden shadow bg-white"
                        style="
                          border: 1px solid #e0e0e0;
                          transition: all 0.3s ease;
                        "
                      >
                        <!-- Image avec badge TOP -->
                        <div class="col-md-4 p-0 position-relative">
                          <div class="h-100 w-100" style="min-height: 200px">
                            <img
                              v-if="hotel.property?.photoUrls?.[0]"
                              :src="hotel.property.photoUrls[0]"
                              alt="hotel"
                              class="img-fluid h-100 w-100"
                              style="object-fit: cover"
                            />
                            <div
                              v-else
                              class="bg-light h-100 d-flex align-items-center justify-content-center"
                            >
                              <i class="fa fa-hotel fa-3x text-muted"></i>
                            </div>
                          </div>
                          <div
                            v-if="idx < 3"
                            class="position-absolute top-0 start-0 bg-primary text-white px-2 py-1 m-2 rounded"
                          >
                            <small class="fw-bold">TOP {{ idx + 1 }}</small>
                          </div>
                        </div>

                        <!-- Infos -->
                        <div class="col-md-8 p-4">
                          <div class="d-flex flex-column h-100">
                            <!-- En-tête avec nom et prix -->
                            <div
                              class="d-flex justify-content-between align-items-start mb-2"
                            >
                              <div>
                                <h3 class="h5 fw-bold mb-1 text-dark">
                                  {{
                                    hotel.property?.name ||
                                    hotel.accessibilityLabel?.split('\n')[0] ||
                                    'Hotel'
                                  }}
                                </h3>
                                <div class="d-flex align-items-center gap-2">
                                  <!-- Étoiles -->
                                  <div
                                    v-if="hotel.property?.class"
                                    class="text-warning"
                                  >
                                    <span
                                      v-for="n in Math.min(
                                        5,
                                        hotel.property.class
                                      )"
                                      :key="n"
                                      >★</span
                                    >
                                    <small class="text-muted ms-1"
                                      >{{ hotel.property.class }} stars</small
                                    >
                                  </div>
                                </div>
                              </div>

                              <!-- Prix -->
                              <div
                                v-if="
                                  hotel.property?.priceBreakdown?.grossPrice
                                "
                                class="text-end"
                              >
                                <div class="fs-4 fw-bold text-primary">
                                  ${{
                                    hotel.property.priceBreakdown.grossPrice.value.toFixed(
                                      2
                                    )
                                  }}
                                  <span class="fs-6 text-muted">{{
                                    hotel.property.priceBreakdown.grossPrice
                                      .currency
                                  }}</span>
                                </div>
                                <small class="text-success fw-semibold"
                                  >Includes taxes & fees</small
                                >
                              </div>
                            </div>

                            <!-- Adresse et note -->
                            <div class="mb-3">
                              <div class="text-muted mb-2">
                                <i
                                  class="fas fa-map-marker-alt text-primary me-1"
                                ></i>
                                {{
                                  hotel.property?.address ||
                                  'Address not available'
                                }}
                              </div>
                              <div
                                v-if="hotel.property?.reviewScore"
                                class="d-flex align-items-center gap-2"
                              >
                                <div
                                  class="bg-primary text-white px-2 py-1 rounded fw-bold small d-flex align-items-center"
                                >
                                  <span class="me-1">★</span>
                                  {{ hotel.property.reviewScore }}/10
                                </div>
                                <span class="text-muted small">
                                  {{ hotel.property.reviewCount }} reviews •
                                  <span class="text-success fw-semibold"
                                    >Excellent</span
                                  >
                                </span>
                              </div>
                            </div>

                            <!-- Description -->
                            <div class="mb-3 small text-muted">
                              {{
                                hotel.accessibilityLabel?.split('\n')[1] ||
                                hotel.property?.description ||
                                'No description available'
                              }}
                            </div>

                            <!-- Bouton et conditions -->
                            <div
                              class="mt-auto d-flex justify-content-between align-items-end"
                            >
                              <div>
                                <small class="text-muted d-block"
                                  >Free cancellation</small
                                >
                                <small class="text-success fw-semibold"
                                  >No prepayment needed</small
                                >
                              </div>
                              <a
                                :href="hotel.property?.url || '#'"
                                target="_blank"
                                class="btn btn-primary px-4 py-2 fw-bold rounded-pill"
                                :class="{ disabled: !hotel.property?.url }"
                              >
                                View Deal
                                <i class="fas fa-arrow-right ms-2"></i>
                              </a>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <!-- ...existing code... -->
                  </div>

                  <!-- Champs Flights -->
                  <template v-if="selectedType === 'flights'">
                    <div class="col-lg-6 mb-2">
                      <input
                        v-model="origin"
                        type="text"
                        class="form-control"
                        placeholder="Ville de départ (ex: Casablanca)"
                      />
                    </div>
                    <div class="col-lg-6 mb-2">
                      <input
                        v-model="destination"
                        type="text"
                        class="form-control"
                        placeholder="Destination (ville)"
                      />
                    </div>
                    <div class="col-lg-6 mb-2">
                      <input
                        v-model="departureDate"
                        type="date"
                        class="form-control"
                      />
                    </div>
                    <div class="col-lg-6 mb-2">
                      <select v-model="travelType" class="niceSelect">
                        <option value="">Travel Type</option>
                        <option>City Tour</option>
                        <option>Family Tour</option>
                      </select>
                    </div>
                    <div class="col-lg-6 mb-2">
                      <select v-model="tourDuration" class="niceSelect">
                        <option value="">Tour Duration</option>
                        <option>5 days</option>
                        <option>7 Days</option>
                        <option>30 days</option>
                      </select>
                    </div>
                    <div class="col-lg-12 mb-3">
                      <label class="mb-1">Adults</label>
                      <div
                        class="d-flex align-items-center justify-content-center gap-2"
                      >
                        <button
                          @click="adults > 1 && adults--"
                          class="counter-btn"
                        >
                          −
                        </button>
                        <span class="counter-value">{{ adults }}</span>
                        <button @click="adults++" class="counter-btn">+</button>
                      </div>
                    </div>
                    <div class="col-lg-12 mb-3">
                      <label class="mb-1">Budget: ${{ budget }}</label>
                      <input
                        type="range"
                        v-model="budget"
                        min="100"
                        max="5000"
                        step="50"
                        class="form-range"
                      />
                    </div>
                    <div class="col-lg-12 mb-4">
                      <label class="mb-1">Choose Interests:</label>
                      <div
                        class="d-flex flex-wrap gap-2 justify-content-center"
                      >
                        <button
                          v-for="interest in bannerList"
                          :key="interest.id"
                          :class="[
                            'interest-btn',
                            interests.includes(interest.text) ? 'active' : ''
                          ]"
                          @click="toggleInterest(interest.text)"
                        >
                          <img
                            :src="interest.image"
                            class="interest-icon me-1"
                          />
                          {{ interest.text }}
                        </button>
                      </div>
                    </div>
                  </template>

                  <!-- Travel.IA message et formulaire -->
                  <div
                    v-if="selectedType === 'travel-ia'"
                    class="col-lg-12 mb-3"
                  >
                    <div
                      class="travelia-card-custom p-4 mb-3 shadow-sm rounded-4"
                    >
                      <div class="d-flex align-items-center mb-3">
                        <i class="fa fa-robot fa-2x text-info me-3"></i>
                        <div>
                          <h5 class="mb-1 fw-bold text-info">
                            Planifiez avec Travel.IA
                          </h5>
                          <small class="text-muted"
                            >Laissez l’IA vous proposer un itinéraire sur
                            mesure</small
                          >
                        </div>
                      </div>
                      <div class="row g-3">
                        <!-- Centres d'intérêt à droite sur desktop, en haut sur mobile -->
                        <div class="col-md-4 order-md-2 mb-3 mb-md-0">
                          <label class="mb-1 small">Centres d'intérêt :</label>
                          <div class="d-flex flex-md-column flex-wrap gap-2">
                            <button
                              v-for="interest in iaBannerList"
                              :key="interest.id"
                              :class="[
                                'interest-btn-custom',
                                iaInterests.includes(interest.text)
                                  ? 'active'
                                  : ''
                              ]"
                              @click="toggleIaInterest(interest.text)"
                              type="button"
                            >
                              <img
                                :src="interest.image"
                                class="interest-icon me-1"
                              />
                              {{ interest.text }}
                            </button>
                          </div>
                        </div>
                        <!-- Formulaire -->
                        <div class="col-md-8 order-md-1">
                          <div class="row g-2">
                            <div class="col-12">
                              <div class="input-date-custom mb-2">
                                <input
                                  v-model="iaCity"
                                  type="text"
                                  class="form-control"
                                  placeholder="Ville ou pays"
                                />
                                <span class="date-icon"
                                  ><i class="fa fa-map-marker-alt"></i
                                ></span>
                              </div>
                            </div>
                            <div class="col-12 col-md-6 mb-2">
                              <div class="input-date-custom">
                                <input
                                  v-model="iaStartDate"
                                  type="date"
                                  class="form-control input-lg"
                                  placeholder="Date début"
                                />
                                <span class="date-icon"
                                  ><i class="fa fa-calendar"></i
                                ></span>
                              </div>
                            </div>
                            <div class="col-12 col-md-6 mb-2">
                              <div class="input-date-custom">
                                <input
                                  v-model="iaEndDate"
                                  type="date"
                                  class="form-control input-lg"
                                  placeholder="Date fin"
                                />
                                <span class="date-icon"
                                  ><i class="fa fa-calendar"></i
                                ></span>
                              </div>
                            </div>
                            <div class="col-12 col-md-6">
                              <label class="mb-1 small"
                                >Budget: ${{ iaBudget }}</label
                              >
                              <input
                                type="range"
                                v-model="iaBudget"
                                min="100"
                                max="5000"
                                step="50"
                                class="form-range"
                              />
                              <div class="d-flex justify-content-between">
                                <small class="text-muted">Éco</small>
                                <small class="text-muted">Luxe</small>
                              </div>
                            </div>
                            <div class="col-12 mt-2">
                              <button
                                v-if="!iaResult"
                                @click="searchTravelIA"
                                class="nir-btn w-100 btn-info text-white fw-bold"
                                :disabled="iaLoading"
                              >
                                <i class="fa fa-magic me-2"></i>
                                <span v-if="!iaLoading"
                                  >Générer mon plan IA</span
                                >
                                <span v-else>Génération...</span>
                              </button>
                              <button
                                v-else
                                @click="resetTravelIA"
                                class="nir-btn w-100 btn-outline-secondary fw-bold"
                                type="button"
                                :disabled="iaLoading"
                                style="max-width: 180px"
                              >
                                <i class="fa fa-undo me-1"></i> Réinitialiser
                              </button>
                            </div>
                            <div v-if="iaError" class="col-12">
                              <div class="alert alert-danger mt-3">
                                <i class="fa fa-exclamation-triangle me-2"></i>
                                {{ iaError }}
                              </div>
                            </div>
                            <div v-if="iaResult" class="col-12">
                              <div class="ia-result-special mt-3">
                                <div class="ia-result-header">
                                  <i class="fa fa-lightbulb"></i>
                                  <span>Votre itinéraire IA personnalisé</span>
                                  <button
                                    class="btn-print"
                                    @click="printResult"
                                  >
                                    <i class="fa fa-print"></i>
                                  </button>
                                </div>
                                <div class="ia-result-content">
                                  <pre>{{ iaResult }}</pre>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Bouton Recherche -->
                  <!-- Bouton Recherche pour Flights uniquement -->
                  <div class="col-lg-12" v-if="selectedType === 'flights'">
                    <button
                      @click="searchFlights"
                      class="nir-btn w-100"
                      :disabled="loading"
                    >
                      <i class="fa fa-search mr-2"></i>
                      <span v-if="!loading">Search Now</span>
                      <span v-else>Searching...</span>
                    </button>
                  </div>
                </div>
                <!-- Résultats vols améliorés -->
                <div v-if="error" class="alert alert-danger mt-3">
                  {{ error }}
                </div>
                <div v-if="flights.length" class="flights-list mt-4">
                  <div
                    v-for="(flight, idx) in flights"
                    :key="flight.id"
                    class="flight-card mb-3 p-3 rounded shadow-sm bg-white position-relative"
                    :style="{ border: idx === 0 ? '2px solid #00bfa5' : '' }"
                  >
                    <span
                      v-if="idx === 0"
                      class="badge bg-success position-absolute"
                      style="top: 50px; right: 10px; font-size: 1em"
                      >Best Price</span
                    >
                    <div
                      class="d-flex justify-content-between align-items-center mb-2"
                    >
                      <span class="text-primary fw-bold">
                        <i class="fa fa-plane"></i>
                        {{ getCityName(getDeparture(flight)) }}
                        <span class="text-muted"
                          >({{ getDeparture(flight) }})</span
                        >
                        <i class="fa fa-arrow-right mx-2"></i>
                        {{ getCityName(getArrival(flight)) }}
                        <span class="text-muted"
                          >({{ getArrival(flight) }})</span
                        >
                      </span>
                      <span class="fw-bold" style="font-size: 1.2em">
                        {{ flight.price?.grandTotal }}
                        {{ flight.price?.currency }}
                      </span>
                    </div>
                    <div class="mb-2">
                      <div
                        v-for="(segment, idx2) in flight.itineraries[0]
                          ?.segments"
                        :key="idx2"
                        class="small d-flex align-items-center"
                      >
                        <img
                          v-if="getCarrierLogo(segment.carrierCode)"
                          :src="getCarrierLogo(segment.carrierCode)"
                          alt="logo"
                          style="
                            width: 32px;
                            height: 32px;
                            object-fit: contain;
                            margin-right: 8px;
                          "
                        />
                        <span>
                          {{ getCarrierName(segment.carrierCode) }}
                          <span class="text-muted"
                            >({{ segment.carrierCode }}
                            {{ segment.number }})</span
                          >
                          <br />
                          {{ getCityName(segment.departure.iataCode) }} ({{
                            segment.departure.iataCode
                          }})
                          <span class="text-muted">{{
                            formatDate(segment.departure.at)
                          }}</span>
                          →
                          {{ getCityName(segment.arrival.iataCode) }} ({{
                            segment.arrival.iataCode
                          }})
                          <span class="text-muted">{{
                            formatDate(segment.arrival.at)
                          }}</span>
                        </span>
                      </div>
                    </div>
                    <button
                      class="btn btn-warning btn-sm float-end"
                      @click="bookFlight(flight)"
                    >
                      Booking Now
                    </button>
                  </div>
                </div>
                <!-- Fin résultats vols améliorés -->
              </div>
            </div>
          </div>

          <!-- Image -->
          <div class="col-lg-6 mb-4">
            <img src="images/travel.png" alt="Travel Image" />
          </div>
        </div>

        <!-- Carousel -->
        <div class="category-main-inner border-t pt-1">
          <div id="banner-carousel" class="splide">
            <div class="splide__track">
              <ul class="splide__list">
                <li
                  class="splide__slide"
                  v-for="banner in bannerList"
                  :key="banner.id"
                >
                  <div class="my-4">
                    <div
                      class="category-item box-shadow p-3 py-4 text-center bg-white rounded overflow-hidden"
                    >
                      <div class="trending-topic-content text-center">
                        <img :src="banner.image" class="mb-1 d-inline-block" />
                        <h4 class="mb-0">
                          <router-link to="/tour-grid">{{
                            banner.text
                          }}</router-link>
                        </h4>
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
  </section>
</template>

<style scoped>
.counter-btn {
  width: 35px;
  height: 35px;
  border: 1px solid #ddd;
  background-color: white;
  font-size: 20px;
  border-radius: 50%;
  transition: background 0.2s;
}
.counter-btn:hover {
  background-color: #00bfa5;
  color: white;
}
.counter-value {
  font-size: 18px;
  min-width: 30px;
  text-align: center;
}
.interest-btn {
  display: flex;
  align-items: center;
  gap: 5px;
  border: 1px solid #ccc;
  padding: 8px 12px;
  border-radius: 30px;
  background-color: white;
  cursor: pointer;
  transition: 0.3s;
}
.interest-btn.active {
  background-color: #00bfa5;
  color: white;
  border-color: #00bfa5;
}
.interest-icon {
  width: 20px;
  height: 20px;
}
.booking-type .type-option {
  padding: 10px 16px;
  border: 1px solid #ddd;
  border-radius: 30px;
  cursor: pointer;
  background-color: white;
  transition: 0.3s;
}
.booking-type .type-option.active {
  background-color: #00bfa5;
  color: white;
  border-color: #00bfa5;
}
.flights-list {
  margin-top: 24px;
}
.flight-card {
  border: 1px solid #e0e0e0;
  transition: box-shadow 0.2s;
  position: relative;
}
.flight-card:hover {
  box-shadow: 0 4px 16px rgba(0, 191, 165, 0.15);
}
.badge.bg-success {
  background-color: #00bfa5 !important;
}
.hotel-card {
  transition: box-shadow 0.2s, border 0.2s;
  border: 1px solid #e0e0e0;
  background: #fff;
}
.hotel-card:hover {
  box-shadow: 0 4px 16px rgba(0, 191, 165, 0.15);
  border-color: #00bfa5;
}
.badge.bg-success {
  background-color: #00bfa5 !important;
}
.btn-warning {
  background: #ffd600;
  color: #222;
  border: none;
  border-radius: 24px;
  font-weight: bold;
  transition: background 0.2s;
}
.btn-warning:hover {
  background: #ffb300;
  color: #fff;
}
.hotel-card:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}
.hotel-card {
  transition: all 0.3s ease;
  border: 1px solid #e0e0e0;
}
.hotel-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  border-color: var(--bs-primary);
}

.hotel-card .btn-primary {
  background-color: var(--bs-primary);
  border: none;
  transition: all 0.3s ease;
}
.hotel-card .btn-primary:hover {
  background-color: #ffd600;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(13, 110, 253, 0.3);
}

.text-warning {
  color: #ffc107 !important;
}

@media (max-width: 767.98px) {
  .hotel-card {
    flex-direction: column;
  }
  .hotel-card > div[class^='col-'] {
    width: 100%;
    max-width: 100%;
  }
}
.travelia-card-custom {
  background: #f8fcff;
  border: 2px solid #00bfa5 !important;
  box-shadow: 0 2px 12px rgba(0, 191, 165, 0.07);
}
.input-date-custom {
  position: relative;
  display: flex;
  align-items: center;
}
.input-date-custom input[type='date'],
.input-date-custom input[type='text'] {
  border-radius: 16px;
  padding-right: 38px;
  height: 48px;
  font-size: 1.1em;
  border: 1.5px solid #00bfa5;
  background: #fff;
  color: #222;
  transition: border 0.2s;
}
.input-date-custom input[type='date']:focus,
.input-date-custom input[type='text']:focus {
  border-color: #009688;
  outline: none;
}
.input-date-custom .date-icon {
  position: absolute;
  right: 14px;
  color: #00bfa5;
  font-size: 1.2em;
  pointer-events: none;
}
.interest-btn-custom {
  width: 100%;
  justify-content: flex-start;
  font-weight: 500;
  font-size: 1em;
  margin-bottom: 6px;
  border-radius: 24px;
  border: 1.5px solid #00bfa5;
  background: #fff;
  color: #00bfa5;
  transition: background 0.2s, color 0.2s;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
}
.interest-btn-custom.active {
  background: #00bfa5;
  color: #fff;
}
.travelia-card-custom {
  background: #f8fcff;
  border: 2px solid #00bfa5 !important;
  box-shadow: 0 2px 12px rgba(0, 191, 165, 0.07);
}
.input-date-custom {
  position: relative;
  display: flex;
  align-items: center;
}
.input-date-custom input[type='date'],
.input-date-custom input[type='text'] {
  border-radius: 16px;
  padding-right: 38px;
  height: 48px;
  font-size: 1.1em;
  border: 1.5px solid #00bfa5;
  background: #fff;
  color: #222;
  transition: border 0.2s;
}
.input-date-custom input[type='date']:focus,
.input-date-custom input[type='text']:focus {
  border-color: #009688;
  outline: none;
}
.input-date-custom .date-icon {
  position: absolute;
  right: 14px;
  color: #00bfa5;
  font-size: 1.2em;
  pointer-events: none;
}
.interest-btn-custom {
  width: 100%;
  justify-content: flex-start;
  font-weight: 500;
  font-size: 1em;
  margin-bottom: 6px;
  border-radius: 24px;
  border: 1.5px solid #00bfa5;
  background: #fff;
  color: #00bfa5;
  transition: background 0.2s, color 0.2s;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
}
.interest-btn-custom.active {
  background: #00bfa5;
  color: #fff;
}
.ia-result-special {
  background: linear-gradient(120deg, #e0f7fa 0%, #fff 100%);
  border-radius: 18px;
  box-shadow: 0 4px 24px rgba(0, 191, 165, 0.08);
  padding: 24px 18px;
  border: 1.5px solid #00bfa5;
  animation: fadeIn 0.7s;
}
.ia-result-header {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: bold;
  color: #009688;
  font-size: 1.2em;
  margin-bottom: 10px;
}
.ia-result-header .fa-lightbulb {
  color: #ffd600;
  font-size: 1.5em;
}
.ia-result-header .btn-print {
  margin-left: auto;
  background: none;
  border: none;
  color: #00bfa5;
  font-size: 1.2em;
  cursor: pointer;
  transition: color 0.2s;
}
.ia-result-header .btn-print:hover {
  color: #009688;
}
.ia-result-content {
  font-family: 'Fira Mono', 'Consolas', monospace;
  color: #222;
  font-size: 1.05em;
  white-space: pre-line;
  background: #f8fcff;
  border-radius: 10px;
  padding: 12px;
  margin-top: 4px;
  border-left: 4px solid #00bfa5;
}
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.input-date-custom input[type='date'].input-lg {
  height: 56px;
  font-size: 1.15em;
}
</style>
