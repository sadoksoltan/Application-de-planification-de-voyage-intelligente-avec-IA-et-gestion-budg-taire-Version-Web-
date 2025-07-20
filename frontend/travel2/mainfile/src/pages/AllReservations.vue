<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from '@/axios'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'

const reservations = ref<Booking[]>([])
const loading = ref(true)
const error = ref('')
import { useRouter } from 'vue-router'
const router = useRouter()

const fetchReservations = async () => {
  loading.value = true
  try {
    const token = localStorage.getItem('auth_token')
    if (!token) throw new Error('Token manquant')
    const { data } = await axios.get('/api/admin/bookings', {
      headers: { Authorization: `Bearer ${token}` }
    })
    reservations.value = data.bookings
  } catch (e: any) {
    error.value = e?.response?.data?.message || 'Erreur lors du chargement.'
    Toastify({
      text: error.value,
      backgroundColor: '#f44336'
    }).showToast()
    if (error.value.toLowerCase().includes('unauthenticated')) {
      router.replace('/login')
    }
  } finally {
    loading.value = false
  }
}
interface Booking {
  id: number
  user?: { name: string }
  flight_data?: any
  created_at?: string
  paid?: boolean
}
const markAsPaid = async (id: number) => {
  try {
    const token = localStorage.getItem('auth_token')
    await axios.patch(
      `/api/admin/bookings/${id}/pay`,
      {},
      {
        headers: { Authorization: `Bearer ${token}` }
      }
    )
    const booking = reservations.value.find((b) => b.id === id)
    if (booking) booking.paid = true
    Toastify({
      text: 'Réservation marquée comme payée',
      backgroundColor: '#10a7a7'
    }).showToast()
  } catch (e) {
    Toastify({
      text: 'Erreur lors du paiement',
      backgroundColor: '#f44336'
    }).showToast()
  }
}
onMounted(() => {
  const role = (localStorage.getItem('role') || '').trim().toLowerCase()
  if (role !== 'admin') {
    router.replace('/')
    return
  }
  fetchReservations()
})
</script>

<template>
  <router-link to="/dashboard" class="dashboard-btn">
    <i class="fas fa-tachometer-alt"></i> Dashboard
  </router-link>
  <div class="all-reservations-container glass">
    <h1><i class="fas fa-list"></i> Toutes les réservations</h1>
    <div v-if="loading" class="loading">Chargement...</div>
    <table v-else-if="reservations.length" class="reservations-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Utilisateur</th>
          <th>Départ</th>
          <th>Arrivée</th>
          <th>Date</th>
          <th>Payé</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="r in reservations" :key="r.id">
          <td>{{ r.id }}</td>
          <td>{{ r.user?.name || '-' }}</td>
          <td>
            {{
              r.flight_data?.itineraries?.[0]?.segments?.[0]?.departure
                ?.iataCode || '-'
            }}
          </td>
          <td>
            {{
              r.flight_data?.itineraries?.[0]?.segments?.slice(-1)[0]?.arrival
                ?.iataCode || '-'
            }}
          </td>
          <td>{{ r.created_at }}</td>
          <td>
            <span v-if="r.paid" class="text-success">Oui</span>
            <span v-else class="text-danger">Non</span>
          </td>
          <td>
            <button
              v-if="!r.paid"
              @click="markAsPaid(r.id)"
              class="btn btn-sm btn-success"
            >
              Marquer comme payé
            </button>
            <!-- autres actions ici -->
          </td>
        </tr>
      </tbody>
    </table>
    <div v-if="!loading && !reservations.length && !error" class="empty">
      Aucune réservation trouvée.
    </div>
    <div v-if="error" class="error-msg">{{ error }}</div>
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
