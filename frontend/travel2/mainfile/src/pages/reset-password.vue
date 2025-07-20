<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from '@/axios'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'

const route = useRoute()
const router = useRouter()

const newPassword = ref('')
const newPasswordConfirmation = ref('')
const token = ref('')
const isLoading = ref(false)

onMounted(() => {
  const paramToken = route.params.token
  const queryToken = route.query.token

  if (typeof paramToken === 'string') {
    token.value = paramToken
  } else if (typeof queryToken === 'string') {
    token.value = queryToken
  } else if (Array.isArray(queryToken)) {
    token.value = queryToken[0] || ''
  } else {
    token.value = ''
  }

  if (!token.value) {
    showToast('Invalid or incomplete password reset link', false)
    router.push('/forgot')
  }
})

const showToast = (message: string, isSuccess = true) => {
  Toastify({
    text: message,
    duration: 3000,
    gravity: 'top',
    position: 'center',
    close: true,
    backgroundColor: isSuccess ? '#4CAF50' : '#f44336',
    style: {
      borderRadius: '20px',
      fontWeight: '500'
    }
  }).showToast()
}

const validateForm = (): boolean => {
  if (!newPassword.value || !newPasswordConfirmation.value) {
    showToast('Please fill in all fields', false)
    return false
  }

  if (newPassword.value.length < 5) {
    showToast('Password must be at least 5 characters', false)
    return false
  }

  if (newPassword.value !== newPasswordConfirmation.value) {
    showToast('Passwords do not match', false)
    return false
  }

  return true
}

const submit = async () => {
  if (!validateForm()) return

  try {
    isLoading.value = true

    const response = await axios.post('/api/forgot', {
      token: token.value,
      new_password: newPassword.value,
      new_password_confirmation: newPasswordConfirmation.value
    })

    showToast(
      response.data.message ||
        'Password reset successful! Redirecting to login...'
    )

    setTimeout(() => router.push('/login'), 2000)
  } catch (error: any) {
    const errorMessage = error.response?.data?.errors
      ? Object.values(error.response.data.errors).flat().join(', ')
      : error.response?.data?.message || 'An error occurred'
    showToast(errorMessage, false)
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="container mt-5">
    <div
      class="card mx-auto"
      style="
        max-width: 500px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      "
    >
      <div class="card-body p-4">
        <h3 class="text-center mb-4" style="color: #2c3e50; font-weight: 600">
          Reset Your Password
        </h3>

        <form @submit.prevent="submit">
          <div class="mb-3">
            <label for="newPassword" class="form-label">New Password</label>
            <input
              v-model="newPassword"
              type="password"
              class="form-control"
              id="newPassword"
              required
              minlength="5"
              placeholder="At least 5 characters"
            />
            <div class="form-text">Minimum 5 characters</div>
          </div>

          <div class="mb-4">
            <label for="newPasswordConfirmation" class="form-label"
              >Confirm Password</label
            >
            <input
              v-model="newPasswordConfirmation"
              type="password"
              class="form-control"
              id="newPasswordConfirmation"
              required
              minlength="5"
            />
          </div>

          <button
            type="submit"
            class="btn w-100 py-2"
            :class="{ 'btn-primary': !isLoading, 'btn-secondary': isLoading }"
            :disabled="isLoading"
            style="font-weight: 500; letter-spacing: 0.5px"
          >
            <span
              v-if="isLoading"
              class="spinner-border spinner-border-sm me-2"
            ></span>
            {{ isLoading ? 'Processing...' : 'Reset Password' }}
          </button>
        </form>

        <div class="text-center mt-3">
          <router-link
            to="/login"
            style="color: #506dab; text-decoration: none"
          >
            Back to Login
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  border: none;
}

.form-control:read-only {
  cursor: not-allowed;
}

.btn-primary {
  background-color: #3b82f6;
  border-color: #3b82f6;
}

.btn-primary:hover {
  background-color: #2563eb;
  border-color: #2563eb;
}
</style>
