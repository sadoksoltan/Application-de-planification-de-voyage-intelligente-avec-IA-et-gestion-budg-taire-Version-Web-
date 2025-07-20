<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from '@/axios'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'

interface Post {
  id: number
  title: string
  category: string
  author: string
  published_date: string
  image: string | null
}

const posts = ref<Post[]>([])
const loading = ref(true)

const API_BASE_URL = 'http://localhost:8000'

const fetchPosts = async () => {
  loading.value = true
  try {
    const token = localStorage.getItem('auth_token')
    const { data } = await axios.get('/api/admin/posts', {
      headers: { Authorization: `Bearer ${token}` }
    })
    posts.value = data
  } catch (e) {
    Toastify({
      text: 'Erreur chargement articles',
      backgroundColor: '#f44336'
    }).showToast()
  } finally {
    loading.value = false
  }
}
const deletePost = async (id: number) => {
  if (!confirm('Supprimer cet article ?')) return
  try {
    const token = localStorage.getItem('auth_token')
    await axios.delete(`/api/admin/posts/${id}`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    posts.value = posts.value.filter((p) => p.id !== id)
    Toastify({
      text: 'Article supprimé',
      backgroundColor: '#10a7a7'
    }).showToast()
  } catch (e) {
    Toastify({
      text: 'Erreur suppression',
      backgroundColor: '#f44336'
    }).showToast()
  }
}
onMounted(fetchPosts)
</script>

<template>
  <router-link to="/dashboard" class="dashboard-btn">
    <i class="fas fa-tachometer-alt"></i> Dashboard
  </router-link>
  <div class="admin-posts glass">
    <div class="top-bar">
      <h2>Gestion des Articles</h2>
      <router-link to="/admin/posts/create" class="add-btn">
        <i class="fas fa-plus"></i> Ajouter un article
      </router-link>
    </div>
    <div v-if="loading" class="loading">Chargement...</div>
    <table v-else>
      <thead>
        <tr>
          <th style="width: 110px">Image</th>
          <th>Titre</th>
          <th>Catégorie</th>
          <th>Auteur</th>
          <th>Date</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="post in posts" :key="post.id">
          <td>
            <img
              v-if="post.image"
              :src="
                post.image.startsWith('http')
                  ? post.image
                  : `${API_BASE_URL}/storage/${post.image}`
              "
              alt=""
              class="post-img"
            />
            <span v-else class="no-img">-</span>
          </td>
          <td>{{ post.title }}</td>
          <td>{{ post.category }}</td>
          <td>{{ post.author }}</td>
          <td>{{ post.published_date }}</td>
          <td>
            <router-link :to="`/admin/posts/${post.id}`" class="edit-btn">
              <i class="fas fa-edit"></i>
            </router-link>
            <button @click="deletePost(post.id)" class="delete-btn">
              <i class="fas fa-trash"></i>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.admin-posts {
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
.post-img {
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
