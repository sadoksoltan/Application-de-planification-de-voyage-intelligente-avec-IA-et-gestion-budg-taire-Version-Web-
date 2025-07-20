<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

import Appbar from 'pages/components/Appbar.vue'
import Banner2 from 'pages/components/Banner2.vue'
import Footer from 'pages/components/Footer.vue'
const firstName = ref('')
const lastName = ref('')
const email = ref('')
const phone = ref('')
const message = ref('')

const validationError = ref('')
const isFormSuccess = ref(false)
async function checkValidation() {
  isFormSuccess.value = false
  validationError.value = ''

  const emailRegExp = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/

  if (firstName.value === '') {
    validationError.value = 'First name is required.'
    return
  }

  if (lastName.value === '') {
    validationError.value = 'Last name is required.'
    return
  }

  if (email.value === '') {
    validationError.value = 'Email is required'
    return
  }

  if (!emailRegExp.test(email.value)) {
    validationError.value = 'Invalid email address.'
    return
  }

  if (phone.value === '') {
    validationError.value = 'Phone number is required.'
    return
  }

  if (message.value === '') {
    validationError.value = 'Comment is required.'
    return
  }

  try {
    await axios.post('http://localhost:8000/api/contact', {
      first_name: firstName.value,
      last_name: lastName.value,
      email: email.value,
      phone: phone.value,
      message: message.value
    })

    isFormSuccess.value = true

    firstName.value = ''
    lastName.value = ''
    email.value = ''
    phone.value = ''
    message.value = ''
  } catch (error: any) {
    if (error.response?.data?.message) {
      validationError.value = error.response.data.message
    } else {
      validationError.value = 'Something went wrong. Please try again.'
    }
  }
}
</script>

<template>
  <Appbar />
  <Banner2 page-title="Contact Us" />

  <section class="contact-main pt-6 pb-60">
    <div class="container">
      <div class="contact-info-main mt-0">
        <div class="row">
          <div class="col-lg-10 col-offset-lg-1 mx-auto">
            <div class="contact-info bg-white">
              <div class="contact-info-title text-center mb-4 px-5">
                <h3 class="mb-1">INFORMATION ABOUT US</h3>
                <p class="mb-0">
                  Sagittis posuere id nam quis vestibulum vestibulum a facilisi
                  at elit hendrerit scelerisque sodales nam dis orci.
                </p>
              </div>

              <div class="contact-info-content row mb-1">
                <div class="col-lg-4 col-md-6 mb-4">
                  <div
                    class="info-item bg-lgrey px-4 py-5 border-all text-center rounded"
                  >
                    <div class="info-icon mb-2">
                      <i class="fa fa-map-marker-alt theme"></i>
                    </div>
                    <div class="info-content">
                      <h3>Office Location</h3>
                      <p class="m-0">Monastir, Tunisia</p>
                    </div>
                  </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                  <div
                    class="info-item bg-lgrey px-4 py-5 border-all text-center rounded"
                  >
                    <div class="info-icon mb-2">
                      <i class="fa fa-phone theme"></i>
                    </div>
                    <div class="info-content">
                      <h3>Phone Number</h3>
                      <p class="m-0">+216 xx xxx xxx</p>
                      <p class="m-0">+216 xx xxx xxx</p>
                    </div>
                  </div>
                </div>

                <div class="col-lg-4 col-md-12 mb-4">
                  <div
                    class="info-item bg-lgrey px-4 py-5 border-all text-center rounded"
                  >
                    <div class="info-icon mb-2">
                      <i class="fa fa-envelope theme"></i>
                    </div>
                    <div class="info-content ps-4">
                      <h3>Email Address</h3>
                      <p class="m-0">info@xxxx.com</p>
                      <p class="m-0">help@xxxx.com</p>
                    </div>
                  </div>
                </div>
              </div>

              <div id="contact-form1" class="contact-form">
                <div class="row">
                  <div class="col-lg-6">
                    <div class="map rounded overflow-hiddenb rounded mb-md-4">
                      <div style="width: 100%">
                        <iframe
                          height="500"
                          src="https://maps.google.com/maps?width=100%25&height=600&hl=en&q=Monastir,%20Tunisia&t=&z=14&ie=UTF8&iwloc=B&output=embed"
                        ></iframe>
                      </div>
                    </div>
                  </div>

                  <div class="col-lg-6">
                    <div class="theme mb-1" v-if="validationError">
                      {{ validationError }}
                    </div>

                    <div v-if="isFormSuccess">
                      <h4 class="mb-0">Email Sent Successfully.</h4>
                      <p>
                        Thank you<strong></strong>, your message has been
                        submitted to us.
                      </p>
                    </div>

                    <form
                      novalidate
                      method="post"
                      id="contactform2"
                      name="contactform2"
                      @submit.prevent="checkValidation"
                    >
                      <div class="form-group mb-2">
                        <input
                          id="fullname"
                          type="text"
                          name="first_name"
                          class="form-control"
                          placeholder="First Name"
                          v-model="firstName"
                        />
                      </div>

                      <div class="form-group mb-2">
                        <input
                          id="llastname"
                          type="text"
                          name="last_name"
                          class="form-control"
                          placeholder="Last Name"
                          v-model="lastName"
                        />
                      </div>

                      <div class="form-group mb-2">
                        <input
                          id="email"
                          type="email"
                          name="email"
                          placeholder="Email"
                          class="form-control"
                          v-model="email"
                        />
                      </div>

                      <div class="form-group mb-2">
                        <input
                          type="text"
                          name="phone"
                          id="phnumber"
                          placeholder="Phone"
                          class="form-control"
                          v-model="phone"
                        />
                      </div>

                      <div class="textarea mb-2">
                        <textarea
                          name="message"
                          placeholder="Enter a message"
                          class="form-control"
                          v-model="message"
                        ></textarea>
                      </div>

                      <div class="comment-btn text-center">
                        <input
                          id="submit2"
                          type="submit"
                          class="nir-btn"
                          value="Send Message"
                        />
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <Footer />
</template>
