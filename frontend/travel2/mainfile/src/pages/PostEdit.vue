<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from '@/axios'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'

const route = useRoute()
const router = useRouter()
const id = route.params.id

const title = ref('')
const category = ref('')
const author = ref('')
const published_date = ref('')
const image = ref<string | null>(null)
const description = ref('')
const loading = ref(false)

onMounted(async () => {
  loading.value = true
  try {
    const token = localStorage.getItem('auth_token')
    const { data } = await axios.get(`/api/admin/posts/${id}`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    title.value = data.title
    category.value = data.category
    author.value = data.author
    published_date.value = data.published_date
    image.value = data.image
    description.value = data.description
  } catch (e) {
    Toastify({
      text: 'Erreur chargement',
      backgroundColor: '#f44336'
    }).showToast()
  } finally {
    loading.value = false
  }
})

const submit = async () => {
  loading.value = true
  try {
    const token = localStorage.getItem('auth_token')
    await axios.put(
      `/api/admin/posts/${id}`,
      {
        title: title.value,
        category: category.value,
        author: author.value,
        published_date: published_date.value,
        image: image.value,
        description: description.value
      },
      {
        headers: { Authorization: `Bearer ${token}` }
      }
    )
    Toastify({
      text: 'Article modifié',
      backgroundColor: '#10a7a7'
    }).showToast()
    router.push('/admin/posts')
  } catch (e) {
    Toastify({
      text: 'Erreur modification',
      backgroundColor: '#f44336'
    }).showToast()
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="admin-posts glass">
    <router-link to="/admin/posts" class="back-btn">
      <i class="fas fa-arrow-left"></i> Retour à la liste
    </router-link>
    <h2>Modifier l'article</h2>
    <form @submit.prevent="submit" class="edit-form">
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
        <label>Image (URL ou chemin)</label>
        <input v-model="image" />
      </div>
      <div class="form-group">
        <label>Description</label>
        <textarea v-model="description" rows="4"></textarea>
      </div>
      <button class="save-btn" :disabled="loading">
        <i class="fas fa-save"></i> Enregistrer
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
  font-size: 1.5rem;
  color: #10a7a7;
  text-align: center;
}
.edit-form {
  margin-top: 18px;
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
.save-btn {
  display: flex;
  align-items: center;
  gap: 7px;
  background: linear-gradient(90deg, #10a7a7 30%, #2dd4bf 70%);
  color: #fff;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  padding: 10px 22px;
  font-size: 1.05rem;
  box-shadow: 0 2px 8px rgba(16, 167, 167, 0.1);
  transition: background 0.18s, transform 0.15s;
  margin-top: 12px;
  cursor: pointer;
}
.save-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
.save-btn:hover {
  background: linear-gradient(90deg, #2dd4bf 30%, #10a7a7 100%);
  color: #fff;
  transform: scale(1.04);
}
.back-btn {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  background: none;
  color: #10a7a7;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  padding: 0;
  font-size: 1rem;
  text-decoration: none;
  margin-bottom: 18px;
  transition: color 0.18s;
}
.back-btn:hover {
  color: #2dd4bf;
  text-decoration: underline;
}
</style>
