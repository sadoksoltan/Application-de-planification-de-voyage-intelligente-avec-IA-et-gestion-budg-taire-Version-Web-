<script setup lang="ts">
import { ref } from 'vue'
import axios from '@/axios'
import { useRouter } from 'vue-router'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'

const title = ref('')
const location = ref('')
const price = ref('')
const reviews = ref(0)
const image = ref<File | null>(null)
const loading = ref(false)
const router = useRouter()

const showToast = (msg: string, ok = true) => {
  Toastify({
    text: msg,
    duration: 3000,
    gravity: 'top',
    position: 'center',
    close: true,
    backgroundColor: ok ? '#10a7a7' : '#f44336',
    style: { borderRadius: '20px' }
  }).showToast()
}

const handleFile = (e: Event) => {
  const files = (e.target as HTMLInputElement).files
  if (files && files.length) image.value = files[0]
}

const submit = async () => {
  loading.value = true
  try {
    const token = localStorage.getItem('auth_token')
    const form = new FormData()
    form.append('title', title.value)
    form.append('location', location.value)
    form.append('price', price.value)
    form.append('reviews', reviews.value.toString())
    if (image.value) form.append('image', image.value)
    await axios.post('/api/admin/tours', form, {
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'multipart/form-data'
      }
    })
    showToast('Tour ajouté avec succès')
    router.push('/admin/tours')
  } catch (e: any) {
    showToast(
      e?.response?.data?.message ||
        (e?.response?.data?.errors &&
          Object.values(e.response.data.errors).join('\n')) ||
        "Erreur lors de l'ajout",
      false
    )
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <router-link to="/dashboard" class="dashboard-btn">
    <i class="fas fa-tachometer-alt"></i> Dashboard
  </router-link>
  <div class="admin-tour-create glass">
    <div class="top-bar">
      <h2>Ajouter un tour</h2>
      <router-link to="/admin/tours" class="back-btn">
        <i class="fas fa-arrow-left"></i> Retour à la liste
      </router-link>
    </div>
    <form @submit.prevent="submit" autocomplete="off">
      <div class="form-group">
        <label>Titre</label>
        <input v-model="title" required placeholder="Titre du tour" />
      </div>
      <div class="form-group">
        <label>Lieu</label>
        <input v-model="location" required placeholder="Lieu" />
      </div>
      <div class="form-group">
        <label>Prix (€)</label>
        <input
          v-model="price"
          type="number"
          min="0"
          required
          placeholder="Prix"
        />
      </div>
      <div class="form-group">
        <label>Nombre de reviews</label>
        <input
          v-model="reviews"
          type="number"
          min="0"
          required
          placeholder="Reviews"
        />
      </div>
      <div class="form-group">
        <label>Image</label>
        <input type="file" accept="image/*" @change="handleFile" />
      </div>
      <button type="submit" :disabled="loading">
        <i class="fas fa-plus"></i>
        <span v-if="!loading">Ajouter</span>
        <span v-else>Ajout...</span>
      </button>
    </form>
  </div>
</template>

<style scoped>
.admin-tour-create {
  padding: 38px 32px 32px 32px;
  border-radius: 18px;
  background: #fff;
  box-shadow: 0 2px 16px rgba(16, 167, 167, 0.09);
  margin: 40px auto;
  max-width: 420px;
}
.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 18px;
}
.back-btn {
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
.back-btn:hover {
  background: linear-gradient(90deg, #2dd4bf 30%, #10a7a7 100%);
  color: #fff;
  transform: scale(1.04);
}
h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #10a7a7;
  letter-spacing: 1px;
}
form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}
.form-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
label {
  font-weight: 600;
  color: #6366f1;
  font-size: 1.04rem;
}
input[type='text'],
input[type='number'],
input[type='file'] {
  padding: 9px 12px;
  border-radius: 7px;
  border: 1.5px solid #e0f2f1;
  font-size: 1.07rem;
  background: #f8fafc;
  outline: none;
  transition: border 0.2s;
}
input:focus {
  border: 1.5px solid #10a7a7;
}
button[type='submit'] {
  margin-top: 10px;
  background: linear-gradient(90deg, #10a7a7 30%, #2dd4bf 70%);
  color: #fff;
  font-weight: 700;
  border: none;
  border-radius: 8px;
  padding: 12px 0;
  font-size: 1.08rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  box-shadow: 0 2px 8px rgba(16, 167, 167, 0.1);
  transition: background 0.18s, transform 0.15s;
  cursor: pointer;
}
button[type='submit']:hover:not(:disabled) {
  background: linear-gradient(90deg, #2dd4bf 30%, #10a7a7 100%);
  transform: scale(1.03);
}
button[disabled] {
  opacity: 0.7;
  cursor: not-allowed;
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
