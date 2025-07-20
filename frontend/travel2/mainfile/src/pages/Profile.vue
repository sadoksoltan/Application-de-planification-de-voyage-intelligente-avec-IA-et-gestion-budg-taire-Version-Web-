<template>
  <router-link to="/" class="dashboard-btn">
    <i class="fas fa-home"></i> home
  </router-link>
  <div class="profile-hero">
    <div class="profile-hero-bg"></div>
    <div class="profile-hero-content">
      <img class="profile-avatar" :src="avatarUrl" alt="Avatar" />
      <h1 class="gradient-text">{{ form.name }}</h1>
      <p class="profile-email">{{ form.email }}</p>
    </div>
  </div>
  <div class="profile-container glass">
    <h2>Mon Profil</h2>
    <form @submit.prevent="handleSave">
      <div class="form-row">
        <label for="name"><i class="fas fa-user"></i> Nom</label>
        <input id="name" v-model="form.name" type="text" required />
      </div>
      <div class="form-row">
        <label for="email"><i class="fas fa-envelope"></i> Email</label>
        <input id="email" v-model="form.email" type="email" disabled />
      </div>
      <div class="form-row">
        <label for="avatar"><i class="fas fa-image"></i> Avatar</label>
        <input
          id="avatar"
          type="file"
          @change="onAvatarChange"
          accept="image/*"
        />
      </div>
      <div class="form-row">
        <label for="password"
          ><i class="fas fa-lock"></i> Nouveau mot de passe</label
        >
        <input
          id="password"
          v-model="form.password"
          type="password"
          placeholder="Laisser vide pour ne pas changer"
        />
      </div>
      <div class="form-actions">
        <button type="submit" class="save-btn">
          <i class="fas fa-save"></i> Enregistrer les modifications
        </button>
      </div>
    </form>
    <div v-if="successMsg" class="success-msg">
      <i class="fas fa-check-circle"></i> {{ successMsg }}
    </div>
    <div v-if="errorMsg" class="error-msg">
      <i class="fas fa-exclamation-triangle"></i> {{ errorMsg }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import axios from '@/axios'

const form = reactive({
  name: '',
  email: '',
  password: '',
  avatar: null as File | null
})

const avatarUrl = ref(
  'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJu-PalNLype77rVV-6AeFIeoDPm22_ruvpA&s'
)
const successMsg = ref('')
const errorMsg = ref('')

onMounted(async () => {
  // 1. Essaye de récupérer le profil depuis l'API (si token présent)
  try {
    const token = localStorage.getItem('auth_token')
    if (token) {
      const { data } = await axios.get('/api/user', {
        headers: { Authorization: `Bearer ${token}` }
      })
      form.name = data.name || 'Utilisateur'
      form.email = data.email || 'user@email.com'
      localStorage.setItem('name', form.name)
      localStorage.setItem('email', form.email)
      // Si c'est un compte Google, stocke aussi dans google_email
      if (data.provider === 'google' || data.email.endsWith('@gmail.com')) {
        localStorage.setItem('google_email', data.email)
      }
      return
    }
  } catch (e) {
    // Si erreur API, fallback sur localStorage
  }
  // 2. Fallback sur localStorage
  const googleEmail = localStorage.getItem('google_email')
  const localEmail = localStorage.getItem('email') || 'user@email.com'
  form.name = localStorage.getItem('name') || 'Utilisateur'
  form.email = googleEmail || localEmail
})

function onAvatarChange(e: Event) {
  const file = (e.target as HTMLInputElement).files?.[0]
  if (file) {
    form.avatar = file
    avatarUrl.value = URL.createObjectURL(file)
  }
}

async function handleSave() {
  try {
    localStorage.setItem('name', form.name)
    successMsg.value = 'Profil mis à jour avec succès !'
    errorMsg.value = ''
    setTimeout(() => (successMsg.value = ''), 3000)
  } catch (e) {
    errorMsg.value = 'Erreur lors de la mise à jour du profil.'
    successMsg.value = ''
  }
}
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

.profile-hero {
  position: relative;
  width: 100vw;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  min-height: 260px;
  background: linear-gradient(120deg, #10a7a7 0%, #2dd4bf 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.profile-hero-bg {
  position: absolute;
  width: 100%;
  height: 100%;
  background: url('https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=1200&q=80')
    center/cover no-repeat;
  opacity: 0.18;
  z-index: 1;
}
.profile-hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  color: #fff;
  padding: 40px 0 20px 0;
  width: 100%;
}
.profile-avatar {
  width: 110px;
  height: 110px;
  border-radius: 50%;
  border: 4px solid #fff;
  margin-bottom: 12px;
  box-shadow: 0 4px 24px rgba(16, 167, 167, 0.18);
  object-fit: cover;
  background: #fff;
}
.gradient-text {
  background: linear-gradient(90deg, #fff 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: 2.2rem;
  font-weight: 900;
  letter-spacing: 2px;
  color: #fff;
}
.profile-email {
  color: #e0f7fa;
  font-size: 1.1rem;
  margin-bottom: 0;
  font-weight: 500;
  text-shadow: 0 1px 8px rgba(16, 167, 167, 0.1);
}

.profile-container {
  max-width: 420px;
  margin: -60px auto 40px auto;
  padding: 36px 28px 28px 28px;
  background: rgba(255, 255, 255, 0.92);
  border-radius: 18px;
  box-shadow: 0 6px 32px rgba(16, 167, 167, 0.13),
    0 1.5px 8px rgba(0, 0, 0, 0.04);
  position: relative;
  border: 1.5px solid #e0f2f1;
  backdrop-filter: blur(6px);
  animation: fadeInUp 0.7s cubic-bezier(0.23, 1.02, 0.32, 1) both;
}
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: none;
  }
}
.profile-container h2 {
  color: #10a7a7;
  font-size: 1.3rem;
  margin-bottom: 24px;
  font-weight: 700;
  letter-spacing: 1px;
  text-align: center;
}
.form-row {
  margin-bottom: 18px;
  display: flex;
  flex-direction: column;
}
.form-row label {
  font-weight: 600;
  color: #10a7a7;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 7px;
}
.form-row input[type='text'],
.form-row input[type='email'],
.form-row input[type='password'] {
  padding: 10px 14px;
  border-radius: 8px;
  border: 1.5px solid #b2f5ea;
  background: #f8fafc;
  font-size: 1.08rem;
  transition: border 0.2s;
  outline: none;
}
.form-row input[type='text']:focus,
.form-row input[type='email']:focus,
.form-row input[type='password']:focus {
  border: 1.5px solid #10a7a7;
  background: #fff;
}
.form-row input[type='file'] {
  padding: 6px 0;
  font-size: 1rem;
}
.form-actions {
  text-align: center;
  margin-top: 18px;
}
.save-btn {
  background: linear-gradient(90deg, #10a7a7 30%, #2dd4bf 70%);
  color: #fff;
  border: none;
  border-radius: 10px;
  padding: 12px 32px;
  font-size: 1.1rem;
  font-weight: 700;
  box-shadow: 0 2px 12px rgba(16, 167, 167, 0.1);
  cursor: pointer;
  transition: background 0.2s, transform 0.15s;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}
.save-btn:hover {
  background: linear-gradient(90deg, #2dd4bf 30%, #10a7a7 100%);
  transform: scale(1.04);
}
.success-msg,
.error-msg {
  margin-top: 18px;
  padding: 12px 18px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1.05rem;
  display: flex;
  align-items: center;
  gap: 8px;
  justify-content: center;
}
.success-msg {
  background: #e0f7fa;
  color: #10a7a7;
}
.error-msg {
  background: #fee2e2;
  color: #b91c1c;
}
@media (max-width: 600px) {
  .profile-container {
    max-width: 98vw;
    padding: 18px 6vw;
  }
  .profile-hero-content {
    padding: 32px 0 12px 0;
  }
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
