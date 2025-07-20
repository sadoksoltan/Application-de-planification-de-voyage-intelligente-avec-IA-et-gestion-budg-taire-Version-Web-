<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from '@/axios'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'

interface Tour {
  id: number
  title: string
  location: string
  reviews: number
  price: number
  image: string | null
}

const tours = ref<Tour[]>([])
const loading = ref(true)

// Utilise l'URL complète du backend pour les images (important si front et back sur ports différents)
const API_BASE_URL = 'http://localhost:8000'

const fetchTours = async () => {
  loading.value = true
  try {
    const token = localStorage.getItem('auth_token')
    const { data } = await axios.get('/api/admin/tours', {
      headers: { Authorization: `Bearer ${token}` }
    })
    tours.value = data
  } catch (e) {
    Toastify({
      text: 'Erreur chargement tours',
      backgroundColor: '#f44336'
    }).showToast()
  } finally {
    loading.value = false
  }
}
const deleteTour = async (id: number) => {
  if (!confirm('Supprimer ce tour ?')) return
  try {
    const token = localStorage.getItem('auth_token')
    await axios.delete(`/api/admin/tours/${id}`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    tours.value = tours.value.filter((t) => t.id !== id)
    Toastify({ text: 'Tour supprimé', backgroundColor: '#10a7a7' }).showToast()
  } catch (e) {
    Toastify({
      text: 'Erreur suppression',
      backgroundColor: '#f44336'
    }).showToast()
  }
}
onMounted(fetchTours)
</script>

<template>
  <router-link to="/dashboard" class="dashboard-btn">
    <i class="fas fa-tachometer-alt"></i> Dashboard
  </router-link>
  <div class="admin-tours glass">
    <div class="top-bar">
      <h2>Gestion des Tours</h2>
      <router-link to="/admin/tours/create" class="add-btn">
        <i class="fas fa-plus"></i> Ajouter un tour
      </router-link>
    </div>
    <div v-if="loading" class="loading">Chargement...</div>
    <table v-else>
      <thead>
        <tr>
          <th style="width: 110px">Image</th>
          <th>Titre</th>
          <th>Lieu</th>
          <th>Prix</th>
          <th>Reviews</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="tour in tours" :key="tour.id">
          <td>
            <img
              v-if="tour.image"
              :src="
                tour.image.startsWith('http')
                  ? tour.image
                  : `${API_BASE_URL}/storage/${tour.image}`
              "
              alt=""
              class="tour-img"
            />
            <span v-else class="no-img">-</span>
          </td>
          <td>{{ tour.title }}</td>
          <td>{{ tour.location }}</td>
          <td>{{ tour.price }} €</td>
          <td>{{ tour.reviews }}</td>
          <td>
            <router-link :to="`/admin/tours/${tour.id}`" class="edit-btn">
              <i class="fas fa-edit"></i>
            </router-link>
            <button @click="deleteTour(tour.id)" class="delete-btn">
              <i class="fas fa-trash"></i>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.admin-tours {
  padding: 32px;
  border-radius: 18px;
  background: #fff;
  box-shadow: 0 2px 16px rgba(16, 167, 167, 0.09);
  margin: 40px auto;
  max-width: 900px;
}
.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 18px;
}
.add-btn {
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
.add-btn:hover {
  background: linear-gradient(90deg, #2dd4bf 30%, #10a7a7 100%);
  color: #fff;
  transform: scale(1.04);
}
.loading {
  text-align: center;
  color: #10a7a7;
  font-size: 1.1rem;
  padding: 30px 0;
}
table {
  width: 100%;
  border-collapse: collapse;
  background: transparent;
}
th,
td {
  padding: 12px 8px;
  border-bottom: 1px solid #e0f2f1;
  text-align: left;
  font-size: 1.04rem;
}
th {
  color: #6366f1;
  font-weight: 600;
  background: #f8fafc;
}
.tour-img {
  width: 100px;
  height: 65px;
  object-fit: cover;
  border-radius: 6px;
  border: 1px solid #e0f2f1;
  background: #f3f3f3;
}
.no-img {
  color: #aaa;
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
