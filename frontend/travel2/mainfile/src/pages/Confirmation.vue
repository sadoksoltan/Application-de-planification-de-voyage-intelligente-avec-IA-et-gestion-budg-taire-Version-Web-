<script setup lang="ts">
import Appbar from './components/Appbar.vue'
import Banner2 from './components/Banner2.vue'
import DiscountAction from './components/DiscountAction.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <Appbar />

  <Banner2 page-title="Confirmation" />

  <section class="trending pt-6 pb-0 bg-lgrey">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-xs-12 mb-4">
          <div class="payment-book">
            <div class="booking-box">
              <div
                class="booking-box-title d-md-flex align-items-center bg-title p-4 mb-4 rounded text-md-start text-center"
              >
                <i
                  class="fa fa-check px-4 py-3 bg-white rounded title fs-5"
                ></i>

                <div class="title-content ms-md-3">
                  <h3 class="mb-1 white">
                    Thank You. Your booking order is confirmed now.
                  </h3>

                  <p class="mb-0 white">
                    A confirmation email has been sent to your provided email
                    address.
                  </p>
                </div>
              </div>

              <div class="travellers-info mb-4">
                <table>
                  <thead>
                    <tr>
                      <th>Order Number</th>
                      <th>Date</th>
                      <th>Total</th>
                      <th>Payment Method</th>
                    </tr>
                  </thead>

                  <tbody>
                    <tr>
                      <td class="theme2">1012</td>
                      <td class="theme2">11/02/2022</td>
                      <td class="theme2">$550.00</td>
                      <td class="theme2">Bank Transfer</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <div class="travellers-info mb-4">
                <h4>Traveler Information</h4>
                <table>
                  <tbody>
                    <tr>
                      <td>Booking Number</td>
                      <td>5784-BD245</td>
                    </tr>

                    <tr>
                      <td>First Name</td>
                      <td>Jessica</td>
                    </tr>

                    <tr>
                      <td>Last Name</td>
                      <td>Brown</td>
                    </tr>

                    <tr>
                      <td>Email Address</td>
                      <td>info#jessica.com</td>
                    </tr>

                    <tr>
                      <td>Street Address and number</td>
                      <td>353 Third floor Avenue</td>
                    </tr>

                    <tr>
                      <td>Town/City</td>
                      <td>Paris</td>
                    </tr>

                    <tr>
                      <td>ZIP Code</td>
                      <td>75800-875</td>
                    </tr>

                    <tr>
                      <td>Country</td>
                      <td>France</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <div class="booking-border mb-4">
                <h4 class="border-b pb-2 mb-2">Payment</h4>

                <p class="mb-0">
                  This is the third time I've used Travelo Website and telling
                  you the truth their services are always reliable and it ony
                  takes few minutes to plan and finalize.
                </p>

                <a href="#">Payment is made by Credit Card via Paypal</a>
              </div>

              <div class="booking-border mb-4">
                <h4 class="border-b pb-2 mb-2">View Booking Details</h4>

                <p class="mb-0">
                  This is the third time I've used Travelo Website and telling
                  you the truth their services are always reliable and it ony
                  takes few minutes to plan and finalize.
                </p>

                <a href="#">https://www.travel.com/booking-details</a>
              </div>

              <div class="booking-border d-flex">
                <a href="#" class="nir-btn me-2">
                  <i class="fa fa-print"></i>
                  Print
                </a>

                <a href="#" class="nir-btn-black">
                  <i class="fa fa-envelope-open-text"></i>
                  Send To
                </a>
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-xs-12 mb-4 ps-4">
          <div class="sidebar-sticky">
            <div class="list-sidebar">
              <div
                class="sidebar-item bordernone bg-white rounded box-shadow overflow-hidden p-3 mb-4"
              >
                <h4>Need Booking Help?</h4>

                <div class="sidebar-module-inner">
                  <p class="mb-2">
                    Paid was hill sir high 24/7. For him precaution any
                    advantages dissimilar.
                  </p>

                  <ul class="help-list">
                    <li class="border-b pb-1 mb-1">
                      <span class="font-weight-bold">Hotline</span>: +475 15 123
                      21
                    </li>

                    <li class="border-b pb-1 mb-1">
                      <span class="font-weight-bold">Email</span>:
                      support@Yatriiworld.com
                    </li>

                    <li>
                      <span class="font-weight-bold">Livechat</span>:
                      Yatriiworld (Skype)
                    </li>
                  </ul>
                </div>
              </div>

              <div
                class="sidebar-item bg-white rounded box-shadow overflow-hidden p-3 mb-4"
              >
                <h4>Why booking with us?</h4>
                <div class="sidebar-module-inner">
                  <ul class="featured-list-sm">
                    <li class="border-b pb-2 mb-2">
                      <h6 class="mb-0">No Booking Charges</h6>

                      We don't charge you an extra fee for booking a hotel room
                      with us.
                    </li>

                    <li class="border-b pb-2 mb-2">
                      <h6 class="mb-0">No Cancellation Sees</h6>

                      We don't charge you a cancellation or modification fee in
                      case plans change.
                    </li>

                    <li class="border-b pb-2 mb-2">
                      <h6 class="mb-0">Instant Confirmation</h6>

                      Instant booking confirmation whether booking online or via
                      the telephone.
                    </li>

                    <li>
                      <h6 class="mb-0">Flexible Booking</h6>
                      You can book up to a whole year in advance or right up
                      until the moment of your stay.
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <DiscountAction />

  <Footer />
</template>
