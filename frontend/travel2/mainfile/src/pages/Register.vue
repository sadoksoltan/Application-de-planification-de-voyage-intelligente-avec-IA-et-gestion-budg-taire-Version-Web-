<script setup lang="ts">
import Appbar from 'pages/components/Appbar.vue'
import Footer from 'pages/components/Footer.vue'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from '@/axios'
import 'bootstrap'
import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'

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

const handleRegister = async () => {
  try {
    if (registerPassword.value !== registerPasswordConfirm.value) {
      showToast('Passwords do not match!', false)
      return
    }

    await axios.get('/sanctum/csrf-cookie')

    const response = await axios.post('/api/register', {
      name: registerName.value,
      email: registerEmail.value,
      password: registerPassword.value,
      password_confirmation: registerPasswordConfirm.value
    })

    console.log('Register success:', response.data)
    showToast('Registration successful! Welcome to our platform.')
    closeModal()
    router.push('/login')
  } catch (error: any) {
    console.error('Register failed:', error.response?.data || error)
    showToast(
      error.response?.data?.message || 'Registration failed. Please try again.',
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
            <h3 class="text-center border-b pb-2">Register</h3>

            <form
              novalidate
              method="post"
              id="contactform2"
              name="contactform2"
              @submit.prevent="handleRegister"
            >
              <div class="form-group mb-2">
                <input
                  id="name"
                  type="text"
                  name="name"
                  v-model="registerName"
                  class="form-control"
                  placeholder="User Name"
                />
              </div>

              <div class="form-group mb-2">
                <input
                  type="text"
                  id="email"
                  name="email"
                  v-model="registerEmail"
                  class="form-control"
                  placeholder="Email Address"
                />
              </div>

              <div class="form-group mb-2">
                <input
                  id="password"
                  type="password"
                  name="password"
                  v-model="registerPassword"
                  class="form-control"
                  placeholder="Password"
                />
              </div>

              <div class="form-group mb-2">
                <input
                  id="password_confirmation"
                  type="password"
                  name="password_confirmation"
                  v-model="registerPasswordConfirm"
                  class="form-control"
                  placeholder="Re-enter Password"
                />
              </div>

              <div class="form-group mb-2 d-flex">
                <input
                  type="checkbox"
                  id="exampleCheck"
                  class="custom-control-input me-1"
                />
                <label
                  class="custom-control-label mb-0 ms-1 lh-1"
                  for="exampleCheck"
                >
                  I have read and accept the Terms and Privacy Policy?
                </label>
              </div>

              <div class="comment-btn mb-2 pb-2 text-center border-b">
                <input
                  id="submit3"
                  type="submit"
                  class="nir-btn"
                  value="Register"
                />
              </div>

              <p class="text-center">
                Already have an account?
                <a href="/login" class="theme">Login</a>
              </p>
            </form>

            <hr class="log-reg-hr position-relative my-4 overflow-visible" />

            <div
              class="log-reg-button d-sm-flex align-items-center justify-content-between"
            >
              <button type="button" class="btn btn-fb w-50 me-1">
                <i class="fab fa-facebook"></i>
                Login with Facebook
              </button>

              <button type="button" class="btn btn-google w-50 ms-1">
                <i class="fab fa-google"></i>
                Login with Google
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <Footer />
</template>
