<script setup lang="ts">
import { ref } from 'vue'
import axios from '@/axios'
import { useRouter } from 'vue-router'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'

const name = ref('')
const email = ref('')
const password = ref('')
const password_confirmation = ref('')
const role = ref('user')
const loading = ref(false)
const router = useRouter()

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

// ...existing code...
const submit = async () => {
  loading.value = true
  try {
    const token = localStorage.getItem('auth_token')
    await axios.post(
      '/api/users',
      {
        name: name.value,
        email: email.value,
        password: password.value,
        role: role.value
      },
      {
        headers: { Authorization: `Bearer ${token}` }
      }
    )
    showToast('Utilisateur créé avec succès')
    router.push('/users')
  } catch (e: any) {
    showToast(
      e?.response?.data?.message ||
        (e?.response?.data?.errors &&
          Object.values(e.response.data.errors).join('\n')) ||
        'Erreur lors de la création',
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
  <div class="user-create glass">
    <div class="top-bar">
      <h2>Ajouter un utilisateur</h2>
    </div>
    <form @submit.prevent="submit" autocomplete="off">
      <div class="form-group">
        <label>Nom</label>
        <input v-model="name" required placeholder="Nom complet" />
      </div>
      <div class="form-group">
        <label>Email</label>
        <input
          v-model="email"
          type="email"
          required
          placeholder="Adresse email"
        />
      </div>
      <div class="form-group">
        <label>Mot de passe</label>
        <input
          v-model="password"
          type="password"
          required
          placeholder="Mot de passe"
          minlength="6"
        />
      </div>
      <div class="form-group">
        <label>Confirmation du mot de passe</label>
        <input
          v-model="password_confirmation"
          type="password"
          required
          placeholder="Confirmer le mot de passe"
          minlength="6"
        />
      </div>
      <div class="form-group">
        <label>Rôle</label>
        <select v-model="role">
          <option value="user">Utilisateur</option>
          <option value="admin">Admin</option>
        </select>
      </div>
      <button type="submit" :disabled="loading">
        <i class="fas fa-user-plus"></i>
        <span v-if="!loading">Ajouter</span>
        <span v-else>Ajout...</span>
      </button>
    </form>
  </div>
</template>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

.user-create {
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
input,
select {
  padding: 9px 12px;
  border-radius: 7px;
  border: 1.5px solid #e0f2f1;
  font-size: 1.07rem;
  background: #f8fafc;
  outline: none;
  transition: border 0.2s;
}
input:focus,
select:focus {
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
</style>
