<script setup lang="ts">
import { ref, onMounted } from 'vue'
import VueCal from 'vue-cal'
import 'vue-cal/dist/vuecal.css'
import axios from '@/axios'

const events = ref<any[]>([])
const loading = ref(true)
const error = ref('')

const fetchBookings = async () => {
  loading.value = true
  try {
    const token = localStorage.getItem('auth_token')
    const { data } = await axios.get('/api/admin/bookings', {
      headers: { Authorization: `Bearer ${token}` }
    })
    console.log(data.bookings)
    events.value = (data.bookings || []).map((b: any) => ({
      start: b.created_at.slice(0, 10),
      end: b.created_at.slice(0, 10),
      title: b.user?.name
        ? `#${b.id} - ${b.user.name}`
        : `#${b.id} - Réservation`
    }))
  } catch (e: any) {
    error.value = e?.response?.data?.message || 'Erreur lors du chargement.'
  } finally {
    loading.value = false
  }
}

onMounted(fetchBookings)
</script>

<template>
  <router-link to="/dashboard" class="dashboard-btn">
    <i class="fas fa-tachometer-alt"></i> Dashboard
  </router-link>
  <div style="max-width: 900px; margin: 40px auto">
    <h1 style="color: #10a7a7; margin-bottom: 24px">
      Calendrier des réservations
    </h1>
    <div v-if="loading" style="text-align: center">Chargement...</div>
    <div v-if="error" style="color: #b91c1c; text-align: center">
      {{ error }}
    </div>
    <vue-cal
      v-else
      :events="events"
      style="height: 700px"
      :time="false"
      default-view="month"
      locale="fr"
    />
  </div>
</template>
<style scoped>
.all-reservations-container {
  max-width: 1100px;
  margin: 40px auto;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 24px #10a7a71a;
  padding: 32px 24px;
}
h1 {
  color: #10a7a7;
  margin-bottom: 24px;
  font-size: 2rem;
  display: flex;
  align-items: center;
  gap: 12px;
}
.reservations-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 18px;
}
.reservations-table th,
.reservations-table td {
  border: 1px solid #e0f2f1;
  padding: 10px 8px;
  text-align: left;
}
.reservations-table th {
  background: #e0f7fa;
  color: #10a7a7;
}
.loading,
.empty,
.error-msg {
  text-align: center;
  margin: 24px 0;
  color: #10a7a7;
  font-weight: 600;
}
.error-msg {
  color: #b91c1c;
}
.dashboard-btn {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  background: linear-gradient(90deg, #10a7a7 30%, #2dd4bf 70%);
  color: #fff;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  padding: 8px 18px;
  font-size: 1.05rem;
  text-decoration: none;
  box-shadow: 0 2px 8px rgba(16, 167, 167, 0.1);
  transition: background 0.18s, transform 0.15s;
}
.dashboard-btn:hover {
  background: linear-gradient(90deg, #2dd4bf 30%, #10a7a7 100%);
  color: #fff;
  transform: scale(1.04);
  text-decoration: none;
}
</style>
