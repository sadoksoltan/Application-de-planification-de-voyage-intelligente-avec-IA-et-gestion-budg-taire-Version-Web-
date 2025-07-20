<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import Appbar from './components/Appbar.vue'
import Banner2 from './components/Banner2.vue'
import DiscountAction from './components/DiscountAction.vue'
import Footer from './components/Footer.vue'
import Destination17Image from 'assets/images/destination/destination17.jpg'
import axios from 'axios'

const isConfirmed = ref(false)

// Formulaire lié dynamiquement
const form = ref({
  title: '',
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  gender: '',
  dob: '',
  country: '',
  city: '',
  address1: '',
  address2: ''
})

// Remplir dynamiquement avec les infos utilisateur du localStorage
onMounted(() => {
  const token = localStorage.getItem('auth_token')
  if (token) {
    axios
      .get('http://localhost:8000/api/bookings', {
        headers: { Authorization: `Bearer ${token}` }
      })
      .then((res) => {
        userBookings.value = res.data.bookings || []
      })
      .catch((err) => {
        console.error(err)
      })
  }

  form.value.firstName = localStorage.getItem('name') || ''
  form.value.email = localStorage.getItem('email') || ''
  // Ajoute d'autres champs si tu les stockes aussi (ex: phone, gender...)
})

// Vérifie que le formulaire est complet
const isFormComplete = computed(
  () =>
    form.value.firstName &&
    form.value.lastName &&
    form.value.email &&
    form.value.phone &&
    form.value.gender &&
    form.value.dob &&
    form.value.country &&
    form.value.city &&
    form.value.address1 &&
    form.value.title
)

// Quand on clique sur CONFIRM BOOKING
const confirmBooking = () => {
  if (isFormComplete.value) {
    isConfirmed.value = true
    setTimeout(() => {
      window.print()
    }, 300)
  }
}

const userBookings = ref<any[]>([])
const totalAmount = computed(() => {
  return userBookings.value.reduce((sum, b) => {
    const price = parseFloat(b.flight_data?.price?.grandTotal || 0)
    return sum + (isNaN(price) ? 0 : price)
  }, 0)
})
const currency = computed(() => {
  return userBookings.value[0]?.flight_data?.price?.currency || 'USD'
})
</script>

<template>
  <Appbar />

  <Banner2 page-title="Booking" />

  <section class="trending pt-6 pb-0 bg-lgrey">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 mb-4">
          <div class="payment-book">
            <div class="booking-box">
              <div class="customer-information mb-4">
                <h3 class="border-b pb-2 mb-2">Traveller Information</h3>

                <form class="mb-2">
                  <h5>Let us know who you are</h5>

                  <div class="row">
                    <div class="col-md-2">
                      <div class="form-group mb-2">
                        <label>Title</label>

                        <div class="input-box">
                          <select class="niceSelect" v-model="form.title">
                            <option value="0">Select</option>
                            <option value="1">Mr.</option>
                            <option value="2">Mrs.</option>
                          </select>
                        </div>
                      </div>
                    </div>

                    <div class="col-md-5">
                      <div class="form-group mb-2">
                        <label>First Name</label>

                        <input
                          type="text"
                          placeholder="First Name"
                          v-model="form.firstName"
                        />
                      </div>
                    </div>

                    <div class="col-md-5">
                      <div class="form-group mb-2">
                        <label>Last Name</label>

                        <input
                          type="text"
                          placeholder="Last Name"
                          v-model="form.lastName"
                        />
                      </div>
                    </div>

                    <div class="col-md-6">
                      <div class="form-group mb-2">
                        <label>Email</label>

                        <input
                          type="email"
                          placeholder="Email Address"
                          v-model="form.email"
                        />
                      </div>
                    </div>

                    <div class="col-md-6">
                      <div class="form-group mb-2">
                        <label>Phone</label>

                        <input
                          type="text"
                          placeholder="Phone No."
                          v-model="form.phone"
                        />
                      </div>
                    </div>

                    <div class="col-md-6 col-sm-6">
                      <div class="form-group">
                        <label>Gender</label>

                        <div class="input-box">
                          <select class="niceSelect" v-model="form.gender">
                            <option value="0">Select Gender</option>
                            <option value="1">Male</option>
                            <option value="2">Female</option>
                          </select>
                        </div>
                      </div>
                    </div>

                    <div class="col-md-6 col-sm-6">
                      <div class="form-group mb-2">
                        <label>DOB</label>

                        <div>
                          <input
                            id="date-range"
                            type="date"
                            v-model="form.dob"
                          />
                        </div>
                      </div>
                    </div>

                    <div class="col-md-6 col-sm-12">
                      <div class="form-group mb-2">
                        <label>Select Country</label>

                        <div class="input-box">
                          <select class="niceSelect" v-model="form.country">
                            <option value="0">Albania</option>
                            <option value="1">Malaysia</option>
                            <option value="2">Singapore</option>
                            <option value="3">Japan</option>
                            <option value="4">Thailand</option>
                          </select>
                        </div>
                      </div>
                    </div>

                    <div class="col-md-6 col-sm-12">
                      <div class="form-group mb-2">
                        <label>Select City</label>

                        <div class="input-box">
                          <select class="niceSelect" v-model="form.city">
                            <option value="0">Istanbul</option>
                            <option value="1">London</option>
                            <option value="2">Texas</option>
                            <option value="3">Tokyo</option>
                            <option value="4">Bangkok</option>
                          </select>
                        </div>
                      </div>
                    </div>

                    <div class="col-md-6">
                      <div class="form-group mb-2">
                        <label>Address Line 1</label>

                        <input
                          type="text"
                          placeholder="Address line 1"
                          v-model="form.address1"
                        />
                      </div>
                    </div>

                    <div class="col-md-6">
                      <div class="form-group mb-2">
                        <label>Address Line 2</label>

                        <input
                          type="text"
                          placeholder="Address line 2"
                          v-model="form.address2"
                        />
                      </div>
                    </div>
                  </div>
                </form>
              </div>

              <div
                class="customer-information mb-4 d-flex align-items-center bg-grey rounded p-4"
              >
                <i
                  class="fa fa-grin-wink rounded fs-1 bg-theme white p-3 px-4"
                ></i>

                <div class="customer-info ps-4">
                  <h6 class="mb-1">Good To Know:</h6>

                  <small>Free Cancellation until 14:00 pn 11 Feb 2022</small>
                </div>
              </div>

              <div class="customer-information card-information">
                <h3 class="border-b pb-2 mb-2">How do you want to pay?</h3>

                <div class="trending-topic-main">
                  <ul
                    class="nav nav-tabs nav-pills nav-fill w-50"
                    id="postsTab1"
                    role="tablist"
                  >
                    <li class="nav-item me-2 ms-0" role="presentation">
                      <button
                        role="tab"
                        type="button"
                        id="card-tab"
                        data-bs-toggle="tab"
                        aria-controls="card"
                        aria-selected="false"
                        data-bs-target="#card"
                        class="nav-link active text-black"
                      >
                        Credit/Debit card
                      </button>
                    </li>

                    <li class="nav-item m-0" role="presentation">
                      <button
                        role="tab"
                        type="button"
                        id="paypal-tab"
                        class="nav-link text-black"
                        aria-selected="true"
                        data-bs-toggle="tab"
                        aria-controls="paypal"
                        data-bs-target="#paypal"
                      >
                        Digital Payment
                      </button>
                    </li>
                  </ul>

                  <div class="tab-content" id="postsTabContent1">
                    <div
                      id="card"
                      role="tabpanel"
                      aria-labelledby="card-tab"
                      class="tab-pane fade active show"
                    >
                      <form>
                        <h5 class="mb-2 border-b pb-2">
                          <i class="fa fa-credit-card"></i> Credit Card
                        </h5>

                        <div class="row align-items-center">
                          <div class="col-md-8">
                            <div class="card-detail">
                              <div class="row">
                                <div class="col-md-6">
                                  <div class="form-group mb-2">
                                    <label>Card Holder Number</label>

                                    <input type="text" />
                                  </div>
                                </div>

                                <div class="col-md-6">
                                  <div class="form-group mb-2">
                                    <label>Card Number</label>

                                    <input
                                      type="text"
                                      placeholder="**** **** **** ****"
                                    />
                                  </div>
                                </div>

                                <div class="col-md-6">
                                  <div class="form-group mb-2">
                                    <label>Expiry Date</label>

                                    <input
                                      type="text"
                                      placeholder=" Expiry Date"
                                    />
                                  </div>
                                </div>

                                <div class="col-md-6">
                                  <div class="form-group">
                                    <label>CVC/CVV</label>

                                    <input type="text" placeholder="CVC/CVV" />
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>

                          <div class="col-md-4">
                            <img src="images/cc.png" alt="" class="rounded" />
                          </div>
                        </div>
                      </form>
                    </div>

                    <div
                      id="paypal"
                      role="tabpanel"
                      class="tab-pane fade"
                      aria-labelledby="paypal-tab"
                    >
                      <div class="paypal-card">
                        <h5 class="mb-2 border-b pb-2">
                          <i class="fab fa-paypal"></i> Paypal
                        </h5>

                        <ul>
                          <li class="d-block">
                            To make the payment process secure and complete you
                            will be redirected to Paypal Website.
                          </li>

                          <li class="d-block">
                            <a href="#" class="theme">
                              Checkout via Paypal
                              <i class="fa fa-long-arrow-alt-right"> </i>
                            </a>
                          </li>

                          <li class="d-block">
                            The total Amount you will be charged is:
                            <span class="fw-bold theme">$ 245.50</span>
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="booking-terms border-t pt-3 mt-3">
                  <form class="d-lg-flex align-items-center">
                    <div class="form-group mb-2 w-75">
                      <input type="checkbox" />

                      By continuing, you agree to the

                      <a href="#">Terms and Conditions.</a>
                    </div>

                    <a
                      href="#"
                      class="nir-btn float-lg-end w-25"
                      :class="{ disabled: !isFormComplete }"
                      @click.prevent="confirmBooking"
                    >
                      CONFIRM BOOKING
                    </a>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-4 mb-4 ps-ld-4">
          <div class="sidebar-sticky">
            <div
              class="sidebar-item bg-white rounded box-shadow overflow-hidden p-3 mb-4"
            >
              <h4>Your Booking Details</h4>

              <div class="trend-full border-b pb-2 mb-2">
                <div class="row">
                  <div class="col-lg-4 col-md-4">
                    <div class="trend-item2 rounded">
                      <router-link
                        to="/destination-detail"
                        :style="{
                          backgroundImage: `url('${Destination17Image}')`
                        }"
                      ></router-link>

                      <div class="color-overlay"></div>
                    </div>
                  </div>

                  <div class="col-lg-8 col-md-8 ps-0">
                    <div class="trend-content position-relative">
                      <div class="rating mb-1">
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <span class="fa fa-star checked"></span>
                        <small>200 Reviews</small>
                      </div>

                      <h5 class="mb-1">
                        <router-link to="/destination-detail">
                          Adriatic Adventure-Zagreb To Athens
                        </router-link>
                      </h5>

                      <h6 class="theme mb-0">
                        <i class="icon-location-pin"></i>
                        Croatia
                      </h6>
                    </div>
                  </div>
                </div>
              </div>

              <div class="trend-check border-b pb-2">
                <div class="row">
                  <div class="col-lg-6">
                    <div class="trend-check-item bg-grey rounded p-3 mb-2">
                      <p class="mb-0">Check In</p>

                      <h6 class="mb-0">Thu 21 Feb 2022</h6>

                      <small>15:00 - 22:00</small>
                    </div>
                  </div>

                  <div class="col-lg-6">
                    <div class="trend-check-item bg-grey rounded p-3 mb-2">
                      <p class="mb-0">Check Out</p>

                      <h6 class="mb-0">Tue 24 Feb 2022</h6>

                      <small>1:00 - 10:00</small>
                    </div>
                  </div>
                </div>
              </div>

              <div class="trend-check border-b pb-2 mb-2">
                <p class="mb-0">Total Length of Stay:</p>

                <h6 class="mb-0">8 Days | 7 Nights</h6>

                <small>
                  <a href="#" class="theme text-decoration-underline">
                    Travelling on different dates?
                  </a>
                </small>
              </div>

              <div class="trend-check">
                <p class="mb-0">You Selected:</p>

                <h6 class="mb-0">
                  Superior Double Rooms
                  <span class="float-end fw-normal">1 room, 3 adults</span>
                </h6>

                <small>
                  <a href="#" class="theme text-decoration-underline">
                    Change your selection
                  </a>
                </small>
              </div>
            </div>

            <div
              class="sidebar-item bg-white rounded box-shadow overflow-hidden p-3 mb-4"
            >
              <h4>Your Price Summary</h4>
              <table>
                <tbody>
                  <tr>
                    <td>Total Amount</td>
                    <td class="theme2">
                      {{ totalAmount.toFixed(2) }} {{ currency }}
                    </td>
                  </tr>
                  <tr>
                    <td>Nombre de réservations</td>
                    <td class="theme2">{{ userBookings.length }}</td>
                  </tr>
                  <tr>
                    <td>Tax &amp; fee</td>
                    <td class="theme2">50.00 {{ currency }}</td>
                  </tr>
                  <tr>
                    <td>Booking Fee</td>
                    <td class="theme2">Free</td>
                  </tr>
                  <tr>
                    <td>Total</td>
                    <td class="theme2">
                      {{ (totalAmount + 50).toFixed(2) }} {{ currency }}
                    </td>
                  </tr>
                </tbody>
                <tfoot class="bg-title">
                  <tr>
                    <th class="font-weight-bold white">Amount</th>
                    <th class="font-weight-bold white">
                      {{ (totalAmount + 50).toFixed(2) }} {{ currency }}
                    </th>
                  </tr>
                </tfoot>
              </table>
            </div>

            <div
              class="sidebar-item bg-white rounded box-shadow overflow-hidden p-3 mb-4"
            >
              <h4>Your Payment Schedule</h4>

              <p class="mb-0">
                Before you stay you'll pay
                <span class="float-end">$40.00</span>
              </p>
            </div>

            <div
              class="sidebar-item bg-white rounded box-shadow overflow-hidden p-3"
            >
              <h4>Do you have a promo code?</h4>

              <input type="text" name="" />

              <a href="#" class="nir-btn-black mt-2">Apply</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <DiscountAction />

  <Footer />

  <div
    v-if="isConfirmed"
    class="receipt-preview mt-4 p-4 border rounded shadow only-print bg-light"
  >
    <h4 class="text-center mb-4 text-primary">Reçu de paiement</h4>

    <div class="mb-2">
      <strong>Nom :</strong> {{ form.title }} {{ form.firstName }}
      {{ form.lastName }}
    </div>
    <div class="mb-2"><strong>Email :</strong> {{ form.email }}</div>
    <div class="mb-2"><strong>Téléphone :</strong> {{ form.phone }}</div>
    <div class="mb-2"><strong>Genre :</strong> {{ form.gender }}</div>
    <div class="mb-2"><strong>Date de naissance :</strong> {{ form.dob }}</div>
    <div class="mb-2"><strong>Pays :</strong> {{ form.country }}</div>
    <div class="mb-2"><strong>Ville :</strong> {{ form.city }}</div>
    <div class="mb-3">
      <strong>Adresse :</strong> {{ form.address1 }} {{ form.address2 }}
    </div>

    <div class="mb-2">
      <strong>Nombre de réservations :</strong> {{ userBookings.length }}
    </div>
    <div class="mb-2">
      <strong>Montant total :</strong>
      {{ totalAmount.toFixed(2) }} {{ currency }}
    </div>

    <hr />

    <div class="mb-2">
      <strong>Statut :</strong> <span class="text-success fw-bold">Payé</span>
    </div>
    <div class="mb-3">
      <strong>Date :</strong> {{ new Date().toLocaleString() }}
    </div>

    <p class="text-center fw-bold text-success mt-4">
      Merci pour votre réservation !
    </p>
  </div>
</template>

<style scoped>
select {
  appearance: none;
  -moz-appearance: none;
  -webkit-appearance: none;
}

.input-box {
  position: relative;
}

.input-box::after {
  position: absolute;
  top: 55%;
  right: 1px;
  pointer-events: none;
  content: url('../assets/chevron-down.svg');
  transform: translate(-50%, -50%);
}

.niceSelect:focus {
  border-color: #999;
}

.receipt-preview {
  border: 2px dashed #00bfa5;
  background: #f8fcff;
  padding: 18px 24px;
  border-radius: 12px;
  margin-top: 24px;
  max-width: 500px;
}
.disabled {
  pointer-events: none;
  opacity: 0.6;
}

@media print {
  body * {
    visibility: hidden !important;
  }
  .only-print,
  .only-print * {
    visibility: visible !important;
  }
  .only-print {
    position: absolute;
    left: 0;
    top: 0;
    width: 100vw;
    background: #fff;
    z-index: 9999;
    box-shadow: none;
    padding: 32px 24px;
  }
}
</style>
