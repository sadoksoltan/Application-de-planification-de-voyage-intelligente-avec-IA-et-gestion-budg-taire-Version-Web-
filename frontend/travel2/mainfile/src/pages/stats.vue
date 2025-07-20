<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import axios from '@/axios'
import { Bar, Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
)

interface LatestUser {
  name: string
  email: string
  created_at: string
}
interface LatestBooking {
  id: number
  user_id: number
  created_at: string
}

const stats = ref<{
  users_count: number
  bookings_count: number
  trips_count: number
  contact_messages_count: number
  tour_count: number
  post_count: number
  latest_users: LatestUser[]
  latest_bookings: LatestBooking[]
}>({
  users_count: 0,
  bookings_count: 0,
  trips_count: 0,
  contact_messages_count: 0,
  tour_count: 0,
  post_count: 0,
  latest_users: [],
  latest_bookings: []
})

const loading = ref(true)

onMounted(async () => {
  try {
    const token = localStorage.getItem('auth_token')
    const { data } = await axios.get('/api/stats', {
      headers: { Authorization: `Bearer ${token}` }
    })
    stats.value = data
  } catch (e) {
    alert('Impossible de charger les statistiques.')
  } finally {
    loading.value = false
  }
})

// Bar chart
const barData = computed(() => ({
  labels: ['Utilisateurs', 'Réservations', 'Tours', 'Articles'],
  datasets: [
    {
      label: 'Totaux',
      backgroundColor: ['#10a7a7', '#6366f1', '#f59e42', '#f44336'],
      data: [
        stats.value.users_count,
        stats.value.bookings_count,
        stats.value.tour_count,
        stats.value.post_count // <-- ici
      ]
    }
  ]
}))

const barOptions = {
  responsive: true,
  plugins: {
    legend: { display: false },
    title: { display: true, text: 'Utilisateurs, Réservations & Tours' }
  }
}

// Line chart
const lineLabels = computed(() =>
  stats.value.latest_bookings.map((b, i) => `#${b.id}`)
)
const lineData = computed(() => ({
  labels: lineLabels.value,
  datasets: [
    {
      label: 'Réservations récentes',
      borderColor: '#10a7a7',
      backgroundColor: 'rgba(16,167,167,0.2)',
      data: stats.value.latest_bookings.map(() => 1),
      tension: 0.4
    }
  ]
}))

const lineOptions = {
  responsive: true,
  plugins: {
    legend: { display: false },
    title: { display: true, text: 'Dernières réservations' }
  }
}
</script>

<template>
  <div class="stats-hero">
    <div class="stats-hero-bg"></div>
    <div class="stats-nav-bar-inside">
      <router-link to="/" class="stats-btn">
        <i class="fas fa-home"></i> Accueil
      </router-link>
      <router-link to="/dashboard" class="stats-btn">
        <i class="fas fa-tachometer-alt"></i> Dashboard
      </router-link>
    </div>
    <div class="stats-hero-content">
      <h1><span class="gradient-text">Statistiques du site</span></h1>
    </div>
  </div>
  <div class="stats-container glass">
    <div v-if="loading" class="loading">Chargement...</div>
    <div v-else>
      <div class="stats-cards">
        <div class="stat-card">
          <i class="fas fa-users"></i>
          <div>
            <div class="stat-value">{{ stats.users_count }}</div>
            <div class="stat-label">Utilisateurs</div>
          </div>
        </div>
        <div class="stat-card">
          <i class="fas fa-calendar-check"></i>
          <div>
            <div class="stat-value">{{ stats.bookings_count }}</div>
            <div class="stat-label">Réservations</div>
          </div>
        </div>
        <div class="stat-card">
          <i class="fas fa-map-marked-alt"></i>
          <div>
            <div class="stat-value">{{ stats.trips_count }}</div>
            <div class="stat-label">Voyages</div>
          </div>
        </div>
        <div class="stat-card">
          <i class="fas fa-route"></i>
          <div>
            <div class="stat-value">{{ stats.tour_count }}</div>
            <div class="stat-label">Tours</div>
          </div>
        </div>
        <div class="stat-card">
          <i class="fas fa-envelope"></i>
          <div>
            <div class="stat-value">{{ stats.contact_messages_count }}</div>
            <div class="stat-label">Messages contact</div>
          </div>
        </div>
        <div class="stat-card">
          <i class="fas fa-newspaper"></i>
          <div>
            <div class="stat-value">{{ stats.post_count }}</div>
            <div class="stat-label">Articles</div>
          </div>
        </div>
      </div>

      <div class="stats-lists">
        <div class="stats-list">
          <h3>Derniers utilisateurs</h3>
          <ul>
            <li v-for="u in stats.latest_users" :key="u.email">
              <i class="fas fa-user"></i>
              {{ u.name }} <span class="email">({{ u.email }})</span>
              <span class="date">{{
                new Date(u.created_at).toLocaleDateString()
              }}</span>
            </li>
          </ul>
        </div>
        <div class="stats-list">
          <h3>Dernières réservations</h3>
          <ul>
            <li v-for="b in stats.latest_bookings" :key="b.id">
              <i class="fas fa-calendar-check"></i>
              Réservation #{{ b.id }} par utilisateur #{{ b.user_id }}
              <span class="date">{{
                new Date(b.created_at).toLocaleDateString()
              }}</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- <div class="chart-card">
        <Line :data="bookingsLineData" :options="lineOptions" />
      </div> -->

      <div class="charts-section">
        <div class="chart-card">
          <Bar :data="barData" :options="barOptions" />
        </div>
        <div class="chart-card">
          <Line :data="lineData" :options="lineOptions" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

/* Styles conservés identiques */
.stats-hero {
  position: relative;
  width: 100vw;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  min-height: 200px;
  background: linear-gradient(120deg, #6366f1 0%, #10a7a7 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.stats-hero-bg {
  position: absolute;
  width: 100%;
  height: 100%;
  background: url('https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=1200&q=80')
    center/cover no-repeat;
  opacity: 0.16;
  z-index: 1;
}
.stats-hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  color: #fff;
  padding: 36px 0 18px 0;
}
.gradient-text {
  background: linear-gradient(90deg, #fff 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: 2.2rem;
  font-weight: 900;
  letter-spacing: 2px;
  text-shadow: 0 2px 12px rgba(56, 189, 248, 0.18);
}
.stats-container {
  max-width: 10000px;
  margin: -60px auto 40px auto;
  padding: 36px 28px 28px 28px;
  background: rgba(255, 255, 255, 0.92);
  border-radius: 18px;
  box-shadow: 0 6px 32px rgba(16, 167, 167, 0.13),
    0 1.5px 8px rgba(0, 0, 0, 0.04);
  position: relative;
  border: 1.5px solid #e0f2f1;
  backdrop-filter: blur(6px);
}
.loading {
  text-align: center;
  font-size: 1.2rem;
  color: #10a7a7;
  padding: 40px 0;
}
.stats-cards {
  display: flex;
  gap: 32px;
  justify-content: space-between;
  margin-bottom: 32px;
  flex-wrap: wrap;
}
.stat-card {
  flex: 1 1 160px;
  min-width: 160px;
  background: linear-gradient(120deg, #10a7a7 0%, #2dd4bf 100%);
  color: #fff;
  border-radius: 14px;
  padding: 22px 18px;
  display: flex;
  align-items: center;
  gap: 18px;
  font-size: 1.2rem;
  box-shadow: 0 2px 12px rgba(16, 167, 167, 0.1);
  margin-bottom: 10px;
}
.stat-card i {
  font-size: 2.2rem;
  opacity: 0.85;
}
.stat-value {
  font-size: 2rem;
  font-weight: 800;
  line-height: 1;
}
.stat-label {
  font-size: 1.05rem;
  font-weight: 500;
  opacity: 0.9;
}
.stats-lists {
  display: flex;
  gap: 32px;
  margin-top: 24px;
  flex-wrap: wrap;
}
.stats-list {
  flex: 1 1 320px;
  min-width: 260px;
  background: #f8fafc;
  border-radius: 12px;
  padding: 18px 18px 10px 18px;
  box-shadow: 0 2px 8px rgba(16, 167, 167, 0.07);
}
.stats-list h3 {
  color: #10a7a7;
  font-size: 1.1rem;
  margin-bottom: 10px;
  font-weight: 700;
}
.stats-list ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.stats-list li {
  margin-bottom: 10px;
  font-size: 1.05rem;
  display: flex;
  align-items: center;
  gap: 8px;
}
.stats-list .email {
  color: #6366f1;
  font-size: 0.98rem;
  margin-left: 4px;
}
.stats-list .date {
  margin-left: auto;
  color: #aaa;
  font-size: 0.93rem;
}
.charts-section {
  display: flex;
  gap: 32px;
  margin-bottom: 32px;
  flex-wrap: wrap;
  justify-content: center;
}
.chart-card {
  background: #fff;
  border-radius: 14px;
  box-shadow: 0 2px 12px rgba(16, 167, 167, 0.07);
  padding: 18px 18px 8px 18px;
  min-width: 320px;
  max-width: 420px;
  flex: 1 1 320px;
}
.stats-nav-bar {
  width: 100vw;
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 18px 32px 0 32px;
  box-sizing: border-box;
  z-index: 10;
}
.stats-nav-bar-inside {
  position: absolute;
  top: 18px;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding: 0 32px;
  z-index: 2;
  pointer-events: none;
}
.stats-nav-bar-inside .stats-btn {
  pointer-events: auto;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  background: linear-gradient(90deg, #10a7a7 30%, #2dd4bf 70%);
  color: #fff;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  padding: 10px 22px;
  font-size: 1.05rem;
  text-decoration: none;
  box-shadow: 0 2px 8px rgba(16, 167, 167, 0.1);
  transition: background 0.18s, transform 0.15s;
}
.stats-nav-bar-inside .stats-btn:hover {
  background: linear-gradient(90deg, #2dd4bf 30%, #10a7a7 100%);
  color: #fff;
  transform: scale(1.04);
  text-decoration: none;
}
.stats-nav-bar-inside .stats-btn i {
  font-size: 1.2em;
  margin-right: 6px;
}
.stats-hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  color: #fff;
  padding: 36px 0 18px 0;
}
@media (max-width: 900px) {
  .stat-card,
  .stats-list,
  .chart-card {
    min-width: unset;
    margin-bottom: 18px;
  }
}
</style>
