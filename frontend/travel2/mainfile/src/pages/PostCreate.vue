<script setup lang="ts">
import { ref } from 'vue'
import axios from '@/axios'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'
import { useRouter } from 'vue-router'

const title = ref('')
const category = ref('')
const author = ref('')
const published_date = ref('')
const image = ref<File | null>(null)
const description = ref('')

const loading = ref(false)
const router = useRouter()

const handleImage = (e: Event) => {
  const files = (e.target as HTMLInputElement).files
  if (files && files.length > 0) {
    image.value = files[0]
  } else {
    image.value = null
  }
}

const submit = async () => {
  loading.value = true
  try {
    const token = localStorage.getItem('auth_token')
    const formData = new FormData()
    formData.append('title', title.value)
    formData.append('category', category.value)
    formData.append('author', author.value)
    formData.append('published_date', published_date.value)
    formData.append('description', description.value)
    if (image.value) {
      formData.append('image', image.value)
    }
    await axios.post('/api/admin/posts/create', formData, {
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'multipart/form-data'
      }
    })
    Toastify({ text: 'Article ajouté', backgroundColor: '#10a7a7' }).showToast()
    router.push('/admin/posts')
  } catch (e) {
    Toastify({ text: 'Erreur ajout', backgroundColor: '#f44336' }).showToast()
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <router-link to="/dashboard" class="dashboard-btn">
    <i class="fas fa-tachometer-alt"></i> Dashboard
  </router-link>
  <div class="admin-posts glass">
    <h2>Ajouter un article</h2>
    <form @submit.prevent="submit">
      <div class="form-group">
        <label>Titre</label>
        <input v-model="title" required />
      </div>
      <div class="form-group">
        <label>Catégorie</label>
        <input v-model="category" />
      </div>
      <div class="form-group">
        <label>Auteur</label>
        <input v-model="author" />
      </div>
      <div class="form-group">
        <label>Date de publication</label>
        <input v-model="published_date" type="date" />
      </div>
      <div class="form-group">
        <label>Image (upload)</label>
        <input type="file" accept="image/*" @change="handleImage" />
      </div>
      <div class="form-group">
        <label>Description</label>
        <textarea v-model="description" rows="4"></textarea>
      </div>
      <button class="add-btn" :disabled="loading">
        <i class="fas fa-plus"></i> Ajouter
      </button>
    </form>
  </div>
</template>

<style scoped>
.admin-posts {
  padding: 32px;
  border-radius: 18px;
  background: #fff;
  box-shadow: 0 2px 16px rgba(16, 167, 167, 0.09);
  margin: 40px auto;
  max-width: 600px;
}
h2 {
  margin-bottom: 18px;
}
.form-group {
  margin-bottom: 16px;
}
label {
  font-weight: 600;
  color: #6366f1;
  margin-bottom: 4px;
  display: block;
}
input,
textarea {
  width: 100%;
  padding: 8px 10px;
  border: 1px solid #e0f2f1;
  border-radius: 6px;
  font-size: 1rem;
  background: #f8fafc;
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
  padding: 10px 22px;
  font-size: 1.05rem;
  text-decoration: none;
  box-shadow: 0 2px 8px rgba(16, 167, 167, 0.1);
  transition: background 0.18s, transform 0.15s;
  margin-top: 12px;
}
.add-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
.add-btn:hover {
  background: linear-gradient(90deg, #2dd4bf 30%, #10a7a7 100%);
  color: #fff;
  transform: scale(1.04);
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
