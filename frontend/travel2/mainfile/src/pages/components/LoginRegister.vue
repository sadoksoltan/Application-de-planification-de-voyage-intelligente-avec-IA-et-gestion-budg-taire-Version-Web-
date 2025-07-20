<script setup lang="ts">
import Trending5Image from 'images/trending/trending5.jpg'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from '@/axios'
import 'bootstrap'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'

const loginEmail = ref('')
const loginPassword = ref('')

const registerName = ref('')
const registerEmail = ref('')
const registerPassword = ref('')
const registerPasswordConfirm = ref('')

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

    // On récupère le nom et le rôle de l'utilisateur depuis la réponse
    const { token, user } = response.data
    // user.name et user.role doivent être présents dans la réponse API

    localStorage.setItem('auth_token', token)
    localStorage.setItem('name', user.name)
    localStorage.setItem('role', user.role)
    localStorage.setItem('email', user.email)
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
    isAuthenticated.value = true

    showToast('Login successful! Welcome back.')
    closeModal()
    router.push('/booking')
  } catch (error: any) {
    console.error('Login failed:', error.response?.data || error)
    showToast('Login failed. Please check your credentials.', false)
  }
}

const handleRegister = async () => {
  try {
    if (registerPassword.value !== registerPasswordConfirm.value) {
      showToast('Passwords do not match!', false)
      return
    }

    await axios.get('/sanctum/csrf-cookie')
    await axios.post('/api/register', {
      name: registerName.value,
      email: registerEmail.value,
      password: registerPassword.value,
      password_confirmation: registerPasswordConfirm.value
    })

    showToast('Registration successful! Welcome to our platform.')
    closeModal()
    router.push('/login')
  } catch (error: any) {
    console.error('Register failed:', error.response?.data || error)
    showToast('Registration failed. Please try again.', false)
  }
}

const handleLogout = async () => {
  try {
    const token = localStorage.getItem('auth_token')
    if (!token) {
      console.error('No authentication token found!')
      return
    }

    await axios.post(
      '/api/logout',
      {},
      {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    )

    showToast('You have been logged out successfully.')
    localStorage.removeItem('auth_token')
    localStorage.removeItem('name')
    localStorage.removeItem('role')
    localStorage.removeItem('email')
    isAuthenticated.value = false
    closeModal()
    router.push('/login')
  } catch (error: any) {
    console.error('Logout failed:', error.response?.data || error)
    if (error.response?.data?.message === 'Unauthenticated.') {
      showToast('You are already logged out.')
      localStorage.removeItem('auth_token')
      localStorage.removeItem('name')
      localStorage.removeItem('role')
      localStorage.removeItem('email')
      isAuthenticated.value = false
      router.push('/login')
    } else {
      showToast('Logout failed. Please try again.', false)
    }
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
    document.body.style.position = ''
    document.body.style.top = ''
  }, 300)
}
</script>

<template>
  <div
    tabindex="-1"
    id="exampleModal"
    class="modal fade"
    aria-hidden="true"
    aria-labelledby="exampleModalLabel"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-body">
          <div class="post-tabs">
            <!-- Onglets conditionnels -->
            <ul
              id="postsTab"
              role="tablist"
              class="nav nav-tabs nav-pills nav-fill"
            >
              <li v-if="!isAuthenticated" class="nav-item" role="presentation">
                <button
                  role="tab"
                  type="button"
                  id="login-tab"
                  data-bs-toggle="tab"
                  aria-controls="login"
                  aria-selected="true"
                  class="nav-link active"
                  data-bs-target="#login"
                >
                  Login
                </button>
              </li>

              <li v-if="!isAuthenticated" class="nav-item" role="presentation">
                <button
                  role="tab"
                  type="button"
                  id="register-tab"
                  class="nav-link"
                  aria-selected="false"
                  data-bs-toggle="tab"
                  aria-controls="register"
                  data-bs-target="#register"
                >
                  Register
                </button>
              </li>

              <!-- Si authentifié : Logout -->
              <li v-else class="nav-item d-flex align-items-center">
                <span class="me-3">Bienvenue, utilisateur !</span>
                <button @click="handleLogout" class="btn btn-danger">
                  Logout
                </button>
              </li>
            </ul>

            <div
              v-if="!isAuthenticated"
              class="tab-content blog-full"
              id="postsTabContent"
            >
              <div
                aria-labelledby="login-tab"
                class="tab-pane fade active show"
                id="login"
                role="tabpanel"
              >
                <div class="row">
                  <div class="col-lg-6">
                    <div class="blog-image rounded">
                      <a
                        href="#"
                        :style="`background-image: url('${Trending5Image}')`"
                      ></a>
                    </div>
                  </div>

                  <div class="col-lg-6">
                    <h4 class="text-center border-b pb-2">Login</h4>

                    <div
                      class="log-reg-button d-flex align-items-center justify-content-between"
                    >
                      <a
                        href="http://127.0.0.1:8000/auth/google"
                        class="btn btn-google"
                      >
                        <i class="fab fa-google"></i>
                        Login with Google
                      </a>

                      <a
                        href="http://127.0.0.1:8000/auth/facebook"
                        class="btn btn-fb"
                      >
                        <i class="fab fa-facebook"></i>
                        Login with Facebook
                      </a>
                    </div>

                    <hr
                      class="log-reg-hr position-relative my-4 overflow-visible"
                    />

                    <form @submit.prevent="handleLogin">
                      <div class="form-group mb-2">
                        <input
                          v-model="loginEmail"
                          type="text"
                          class="form-control"
                          placeholder="User Name or Email Address"
                        />
                      </div>

                      <div class="form-group mb-2">
                        <input
                          v-model="loginPassword"
                          type="password"
                          class="form-control"
                          placeholder="Password"
                        />
                      </div>

                      <div class="form-group mb-2">
                        <input
                          type="checkbox"
                          id="loginCheck"
                          class="custom-control-input"
                        />
                        <label
                          class="custom-control-label mb-0 ms-1"
                          for="loginCheck"
                        >
                          Remember me
                        </label>
                        <a class="float-end" href="/forgot-password"
                          >Lost your password?</a
                        >
                      </div>

                      <div class="comment-btn mb-2 pb-2 text-center border-b">
                        <input
                          type="submit"
                          value="Login"
                          class="nir-btn w-100"
                        />
                      </div>

                      <p class="text-center">
                        Don't have an account?
                        <a href="/register" class="theme">Register</a>
                      </p>
                    </form>
                  </div>
                </div>
              </div>
              <div
                id="register"
                role="tabpanel"
                class="tab-pane fade"
                aria-labelledby="register-tab"
              >
                <div class="row">
                  <div class="col-lg-6">
                    <div class="blog-image rounded">
                      <a
                        href="#"
                        :style="`background-image: url('${Trending5Image}')`"
                      ></a>
                    </div>
                  </div>

                  <div class="col-lg-6">
                    <h4 class="text-center border-b pb-2">Register</h4>

                    <div
                      class="log-reg-button d-flex align-items-center justify-content-between"
                    >
                      <button type="submit" class="btn btn-fb">
                        <i class="fab fa-facebook"></i>
                        Login with Facebook
                      </button>
                      <button type="submit" class="btn btn-google">
                        <i class="fab fa-google"></i>
                        Login with Google
                      </button>
                    </div>

                    <hr
                      class="log-reg-hr position-relative my-4 overflow-visible"
                    />

                    <form @submit.prevent="handleRegister">
                      <div class="form-group mb-2">
                        <input
                          v-model="registerName"
                          type="text"
                          class="form-control"
                          placeholder="User Name"
                        />
                      </div>

                      <div class="form-group mb-2">
                        <input
                          v-model="registerEmail"
                          type="text"
                          class="form-control"
                          placeholder="Email Address"
                        />
                      </div>

                      <div class="form-group mb-2">
                        <input
                          v-model="registerPassword"
                          type="password"
                          class="form-control"
                          placeholder="Password"
                        />
                      </div>

                      <div class="form-group mb-2">
                        <input
                          v-model="registerPasswordConfirm"
                          type="password"
                          class="form-control"
                          placeholder="Re-enter Password"
                        />
                      </div>

                      <div class="form-group mb-2 d-flex">
                        <input
                          type="checkbox"
                          id="registerCheck"
                          class="custom-control-input"
                        />
                        <label
                          for="registerCheck"
                          class="custom-control-label mb-0 ms-1 lh-1"
                        >
                          I have read and accept the Terms and Privacy Policy?
                        </label>
                      </div>

                      <div class="comment-btn mb-2 pb-2 text-center border-b">
                        <input
                          type="submit"
                          class="nir-btn w-100"
                          value="Register"
                        />
                      </div>

                      <p class="text-center">
                        Already have an account?
                        <a href="/login" class="theme">Login</a>
                      </p>
                    </form>
                  </div>
                </div>
              </div>
              <!-- END REGISTER -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.nav-item button {
  color: black;
}
.log-reg-button .btn-fb,
.log-reg-button .btn-google {
  padding: 14px 18px;
  text-align: center;
  color: #fff;
  outline: none;
  border-radius: 10px;
  font-size: 14px;
  background: #506dab;
}
.log-reg-button .btn-google {
  background: #dd4b39;
}
.modal-content {
  max-height: 90vh;
  overflow-y: auto;
}
.modal-body {
  min-height: 550px;
}
.form-group {
  margin-bottom: 1rem;
}
input.form-control {
  width: 100%;
}
@media (max-width: 768px) {
  .modal-dialog {
    width: 90%;
  }
}
</style>
