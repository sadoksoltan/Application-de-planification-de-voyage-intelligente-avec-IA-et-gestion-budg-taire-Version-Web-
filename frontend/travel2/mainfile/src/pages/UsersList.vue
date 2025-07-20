<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from '@/axios'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'
interface User {
  id: number
  name: string
  email: string
  role: string
}
const showToast = (message: string, isSuccess = true) => {
  Toastify({
    text: message,
    duration: 3000,
    gravity: 'top',
    position: 'center',
    close: true,
    backgroundColor: isSuccess ? '#4CAF50' : '#f44336',
    style: { borderRadius: '20px' }
  }).showToast()
}
const users = ref<User[]>([])
const loading = ref(true)
const editingId = ref<number | null>(null)
const editName = ref('')
const editEmail = ref('')

const fetchUsers = async () => {
  loading.value = true
  try {
    const token = localStorage.getItem('auth_token')
    const { data } = await axios.get('/api/users', {
      headers: { Authorization: `Bearer ${token}` }
    })
    users.value = data
  } catch (e) {
    alert('Erreur lors du chargement des utilisateurs')
  } finally {
    loading.value = false
  }
}

const startEdit = (user: User) => {
  editingId.value = user.id
  editName.value = user.name
  editEmail.value = user.email
}

const cancelEdit = () => {
  editingId.value = null
  editName.value = ''
  editEmail.value = ''
}

const saveEdit = async (user: User) => {
  try {
    const token = localStorage.getItem('auth_token')
    await axios.put(
      `/api/users/${user.id}`,
      {
        name: editName.value,
        email: editEmail.value
      },
      {
        headers: { Authorization: `Bearer ${token}` }
      }
    )
    user.name = editName.value
    user.email = editEmail.value
    showToast('Utilisateur modifié avec succès')
    cancelEdit()
  } catch (e) {
    showToast('Erreur lors de la modification', false)
  }
}

const deleteUser = async (id: number) => {
  if (!confirm('Supprimer cet utilisateur ?')) return
  try {
    const token = localStorage.getItem('auth_token')
    await axios.delete(`/api/users/${id}`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    users.value = users.value.filter((u) => u.id !== id)
    showToast('Utilisateur supprimé avec succès')
  } catch (e) {
    showToast('Erreur lors de la suppression', false)
  }
}

onMounted(fetchUsers)
</script>

<template>
  <router-link to="/dashboard" class="dashboard-btn">
    <i class="fas fa-tachometer-alt"></i> Dashboard
  </router-link>
  <div class="users-list glass">
    <h2>Utilisateurs</h2>

    <div v-if="loading" class="loading">Chargement...</div>
    <table v-else>
      <thead>
        <tr>
          <th>Nom</th>
          <th>Email</th>
          <th>Rôle</th>
          <th style="width: 120px"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="u in users" :key="u.id">
          <td>
            <template v-if="editingId === u.id">
              <input v-model="editName" class="edit-input" />
            </template>
            <template v-else>
              {{ u.name }}
            </template>
          </td>
          <td>
            <template v-if="editingId === u.id">
              <input v-model="editEmail" class="edit-input" />
            </template>
            <template v-else>
              {{ u.email }}
            </template>
          </td>
          <td>{{ u.role }}</td>
          <td>
            <div class="actions">
              <template v-if="editingId === u.id">
                <button
                  class="icon-btn save"
                  @click="saveEdit(u)"
                  title="Enregistrer"
                >
                  <i class="fas fa-check"></i>
                </button>
                <button
                  class="icon-btn cancel"
                  @click="cancelEdit"
                  title="Annuler"
                >
                  <i class="fas fa-times"></i>
                </button>
              </template>
              <template v-else>
                <button
                  class="icon-btn edit"
                  @click="startEdit(u)"
                  title="Modifier"
                >
                  <i class="fas fa-pen"></i>
                </button>
                <button
                  class="icon-btn delete"
                  @click="deleteUser(u.id)"
                  title="Supprimer"
                >
                  <i class="fas fa-trash"></i>
                </button>
              </template>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

.users-list {
  padding: 32px;
  border-radius: 18px;
  background: #fff;
  box-shadow: 0 2px 16px rgba(16, 167, 167, 0.09);
  margin: 40px auto;
  max-width: 700px;
}
.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 18px;
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
h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #10a7a7;
  letter-spacing: 1px;
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
.edit-input {
  width: 95%;
  padding: 6px 8px;
  border: 1px solid #e0f2f1;
  border-radius: 6px;
  font-size: 1rem;
  background: #f8fafc;
  outline: none;
  transition: border 0.2s;
}
.edit-input:focus {
  border: 1.5px solid #10a7a7;
}
.actions {
  display: flex;
  gap: 8px;
}
.icon-btn {
  background: none;
  border: none;
  color: #6366f1;
  font-size: 1.1rem;
  cursor: pointer;
  padding: 4px 7px;
  border-radius: 6px;
  transition: background 0.15s, color 0.15s;
}
.icon-btn.edit:hover {
  background: #e0f2f1;
  color: #10a7a7;
}
.icon-btn.save {
  color: #10a7a7;
}
.icon-btn.save:hover {
  background: #e0fbe0;
}
.icon-btn.cancel {
  color: #f472b6;
}
.icon-btn.cancel:hover {
  background: #fbe0f0;
}
.icon-btn.delete {
  color: #f472b6;
}
.icon-btn.delete:hover {
  background: #fbe0f0;
}
</style>
