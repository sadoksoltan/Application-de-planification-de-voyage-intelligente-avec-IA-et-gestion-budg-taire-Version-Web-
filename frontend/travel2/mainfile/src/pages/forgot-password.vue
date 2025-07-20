<script setup lang="ts">
import { ref } from 'vue'
import axios from '@/axios'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'

const email = ref('')
const isLoading = ref(false)

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

const submit = async () => {
  try {
    isLoading.value = true

    // Ensure CSRF protection
    await axios.get('/sanctum/csrf-cookie', { withCredentials: true })

    const response = await axios.post(
      '/api/forgot-password',
      {
        email: email.value
      },
      {
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        }
      }
    )

    showToast(
      response.data.message || 'Password reset email sent successfully!'
    )
    email.value = '' // Clear form on success
  } catch (error: any) {
    console.error('Password reset error:', error)

    let errorMessage = 'Failed to send password reset link'
    if (error.response) {
      errorMessage =
        error.response.data?.message ||
        error.response.data?.error ||
        error.response.statusText
    } else if (error.request) {
      errorMessage = 'No response from server'
    }

    showToast(errorMessage, false)
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="container mt-5">
    <h3 class="text-center mb-4">Forgot Password</h3>
    <form @submit.prevent="submit" class="mx-auto" style="max-width: 400px">
      <div class="form-group mb-3">
        <label for="email">Email address</label>
        <input
          v-model="email"
          type="email"
          class="form-control"
          id="email"
          required
          :disabled="isLoading"
        />
      </div>
      <button type="submit" class="btn btn-primary w-100" :disabled="isLoading">
        <span v-if="isLoading" class="spinner-border spinner-border-sm"></span>
        {{ isLoading ? 'Sending...' : 'Send Reset Link' }}
      </button>
    </form>
  </div>
</template>
