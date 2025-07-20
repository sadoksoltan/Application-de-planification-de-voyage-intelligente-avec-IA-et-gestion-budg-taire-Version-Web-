<script setup lang="ts">
import Appbar from 'pages/components/Appbar.vue'
import Footer from 'pages/components/Footer.vue'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from '@/axios'
import 'bootstrap'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'

const loginEmail = ref('')
const loginPassword = ref('')

const router = useRouter()
const isAuthenticated = ref(false)

onMounted(() => {
  checkAuthStatus()
})

const checkAuthStatus = () => {
  isAuthenticated.value = !!localStorage.getItem('auth_token')
}

const showToast = (message: string, isSuccess: boolean = true) => {
  Toastify({
    text: message,
    duration: 3000,
    close: true,
    gravity: 'top',
    position: 'center',
    backgroundColor: isSuccess ? '#4CAF50' : '#f44336',
    stopOnFocus: true,
    style: {
      borderRadius: '20px'
    }
  }).showToast()
}

const handleLogin = async () => {
  try {
    await axios.get('/sanctum/csrf-cookie')

    const response = await axios.post('/api/login', {
      email: loginEmail.value,
      password: loginPassword.value
    })

    console.log('Login success:', response.data)
    showToast('Login successful! Welcome back.')

    const token = response.data.token
    localStorage.setItem('auth_token', token)
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
    isAuthenticated.value = true

    closeModal()
    router.push('/booking')
  } catch (error: any) {
    console.error('Login failed:', error.response?.data || error)
    showToast(
      error.response?.data?.message ||
        'Login failed. Please check your credentials.',
      false
    )
  }
}

const closeModal = () => {
  const modalEl = document.getElementById('exampleModal')
  const bootstrap = (window as any).bootstrap
  if (modalEl && bootstrap?.Modal) {
    const modalInstance = bootstrap.Modal.getInstance(modalEl)
    modalInstance?.hide()
  }

  setTimeout(() => {
    document.querySelectorAll('.modal-backdrop').forEach((el) => el.remove())
    document.body.classList.remove('modal-open')
    document.body.style.overflow = 'auto'
    document.body.style.paddingRight = ''
  }, 100)
}
</script>

<template>
  <Appbar />

  <section class="login-register pt-6 pb-6">
    <div class="container">
      <div class="log-main blog-full log-reg w-75 mx-auto">
        <div class="row">
          <div class="col-lg-12">
            <h3 class="text-center border-b pb-2">Login</h3>

            <form
              method="post"
              name="contactform"
              id="contactform3"
              @submit.prevent="handleLogin"
            >
              <div class="form-group mb-2">
                <input
                  type="text"
                  id="email"
                  name="email"
                  v-model="loginEmail"
                  class="form-control"
                  placeholder="Email Address"
                />
              </div>

              <div class="form-group mb-2">
                <input
                  type="password"
                  id="password"
                  name="password"
                  v-model="loginPassword"
                  class="form-control"
                  placeholder="Password"
                />
              </div>

              <div class="form-group mb-2">
                <input
                  type="checkbox"
                  id="exampleCheck3"
                  class="custom-control-input me-1"
                />
                <label class="custom-control-label mb-0" for="exampleCheck3">
                  Remember me
                </label>
                <a class="float-end" href="/forgot-password"
                  >Lost your password?</a
                >
              </div>

              <div class="comment-btn mb-2 pb-2 text-center border-b">
                <input
                  id="submit1"
                  type="submit"
                  value="Login"
                  class="nir-btn"
                />
              </div>

              <p class="text-center">
                Don't have an account?
                <a href="/register" class="theme">Register</a>
              </p>
            </form>

            <hr class="log-reg-hr position-relative my-4 overflow-visible" />

            <div
              class="log-reg-button d-sm-flex align-items-center justify-content-between"
            >
              <a
                href="http://127.0.0.1:8000/auth/facebook"
                class="btn btn-fb w-50 me-1"
              >
                <i class="fab fa-facebook"></i>
                Login with Facebook
              </a>

              <a
                href="http://127.0.0.1:8000/auth/google"
                class="btn btn-google w-50 ms-1"
              >
                <i class="fab fa-google"></i>
                Login with Google
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <Footer />
</template>
