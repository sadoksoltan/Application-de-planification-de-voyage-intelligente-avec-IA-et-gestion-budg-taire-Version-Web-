<script setup lang="ts">
import { ref } from 'vue'

import Appbar from 'pages/components/Appbar.vue'
import Banner2 from 'pages/components/Banner2.vue'
import DiscountAction from 'pages/components/DiscountAction.vue'
import Footer from 'pages/components/Footer.vue'

const accrodion1Idx = ref(1)
const accrodion2Idx = ref(1)
</script>

<template>
  <Appbar />

  <Banner2 page-title="FAQ" />

  <section class="faq-main pb-6 pt-6">
    <div class="container">
      <div class="section-title mb-6 text-center w-75 mx-auto">
        <h4 class="mb-1 theme1">Faq</h4>

        <h2 class="mb-1">
          Frequent Asked <span class="theme">Questions</span>
        </h2>

        <p>
          Explore new horizons, embrace different cultures, and create
          unforgettable memories.
        </p>
      </div>

      <div class="faq-accordian">
        <div class="row">
          <div class="col-lg-6 col-md-12 mb-4">
            <div
              class="accrodion-grp faq-accrodion faq-accrodion1"
              data-grp-name="faq-accrodion1"
            >
              <div class="accrodion" :class="{ active: accrodion1Idx === 1 }">
                <div class="accrodion-title" @click="accrodion1Idx = 1">
                  <h5>Who We Are?</h5>
                </div>

                <div
                  class="accrodion-content"
                  :class="{
                    'd-none': accrodion1Idx !== 1
                  }"
                >
                  <div class="inner">
                    <p>
                      Discover the beauty of the world around you, immerse
                      yourself in diverse cultures, and create lasting memories
                      through your travels. Embrace every moment as an
                      opportunity for growth and adventure
                    </p>
                  </div>
                </div>
              </div>

              <div class="accrodion" :class="{ active: accrodion1Idx === 2 }">
                <div class="accrodion-title" @click="accrodion1Idx = 2">
                  <h5>Wanna know our Special Features?</h5>
                </div>

                <div
                  class="accrodion-content"
                  :class="{
                    'd-none': accrodion1Idx !== 2
                  }"
                >
                  <div class="inner">
                    <p>
                      Discover the beauty of the world around you, immerse
                      yourself in diverse cultures, and create lasting memories
                      through your travels. Embrace every moment as an
                      opportunity for growth and adventure
                    </p>
                  </div>
                </div>
              </div>

              <div class="accrodion" :class="{ active: accrodion1Idx === 3 }">
                <div class="accrodion-title" @click="accrodion1Idx = 3">
                  <h5>Check Your Status</h5>
                </div>

                <div
                  class="accrodion-content"
                  :class="{
                    'd-none': accrodion1Idx !== 3
                  }"
                >
                  <div class="inner">
                    <p>
                      Discover the beauty of the world around you, immerse
                      yourself in diverse cultures, and create lasting memories
                      through your travels. Embrace every moment as an
                      opportunity for growth and adventure
                    </p>
                  </div>
                </div>
              </div>

              <div class="accrodion" :class="{ active: accrodion1Idx === 4 }">
                <div class="accrodion-title" @click="accrodion1Idx = 4">
                  <h5>Why choose us?</h5>
                </div>

                <div
                  class="accrodion-content"
                  :class="{
                    'd-none': accrodion1Idx !== 4
                  }"
                >
                  <div class="inner">
                    <p>
                      Discover the beauty of the world around you, immerse
                      yourself in diverse cultures, and create lasting memories
                      through your travels. Embrace every moment as an
                      opportunity for growth and adventure
                    </p>
                  </div>
                </div>
              </div>

              <div class="accrodion" :class="{ active: accrodion1Idx === 5 }">
                <div class="accrodion-title" @click="accrodion1Idx = 5">
                  <h5>How do I post my listing</h5>
                </div>

                <div
                  class="accrodion-content"
                  :class="{
                    'd-none': accrodion1Idx !== 5
                  }"
                >
                  <div class="inner">
                    <p>
                      Discover the beauty of the world around you, immerse
                      yourself in diverse cultures, and create lasting memories
                      through your travels. Embrace every moment as an
                      opportunity for growth and adventure
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="col-lg-6 col-md-12 mb-4">
            <div
              class="accrodion-grp faq-accrodion faq-accrodion2"
              data-grp-name="faq-accrodion2"
            >
              <div class="accrodion" :class="{ active: accrodion2Idx === 1 }">
                <div class="accrodion-title" @click="accrodion2Idx = 1">
                  <h5>Why my card payment is failing?</h5>
                </div>

                <div
                  class="accrodion-content"
                  :class="{
                    'd-none': accrodion2Idx !== 1
                  }"
                >
                  <div class="inner">
                    <p>
                      Discover the beauty of the world around you, immerse
                      yourself in diverse cultures, and create lasting memories
                      through your travels. Embrace every moment as an
                      opportunity for growth and adventure
                    </p>
                  </div>
                </div>
              </div>

              <div class="accrodion" :class="{ active: accrodion2Idx === 2 }">
                <div class="accrodion-title" @click="accrodion2Idx = 2">
                  <h5>Can I upload attachments</h5>
                </div>

                <div
                  class="accrodion-content"
                  :class="{
                    'd-none': accrodion2Idx !== 2
                  }"
                >
                  <div class="inner">
                    <p>
                      Discover the beauty of the world around you, immerse
                      yourself in diverse cultures, and create lasting memories
                      through your travels. Embrace every moment as an
                      opportunity for growth and adventure
                    </p>
                  </div>
                </div>
              </div>

              <div class="accrodion" :class="{ active: accrodion2Idx === 3 }">
                <div class="accrodion-title" @click="accrodion2Idx = 3">
                  <h5>Can I create a profile page for business</h5>
                </div>

                <div
                  class="accrodion-content"
                  :class="{
                    'd-none': accrodion2Idx !== 3
                  }"
                >
                  <div class="inner">
                    <p>
                      Discover the beauty of the world around you, immerse
                      yourself in diverse cultures, and create lasting memories
                      through your travels. Embrace every moment as an
                      opportunity for growth and adventure
                    </p>
                  </div>
                </div>
              </div>

              <div class="accrodion" :class="{ active: accrodion2Idx === 4 }">
                <div class="accrodion-title" @click="accrodion2Idx = 4">
                  <h5>What is the price of posting</h5>
                </div>

                <div
                  class="accrodion-content"
                  :class="{
                    'd-none': accrodion2Idx !== 4
                  }"
                >
                  <div class="inner">
                    <p>
                      Discover the beauty of the world around you, immerse
                      yourself in diverse cultures, and create lasting memories
                      through your travels. Embrace every moment as an
                      opportunity for growth and adventure
                    </p>
                  </div>
                </div>
              </div>

              <div class="accrodion" :class="{ active: accrodion2Idx === 5 }">
                <div class="accrodion-title" @click="accrodion2Idx = 5">
                  <h5>How do I post my listing</h5>
                </div>

                <div
                  class="accrodion-content"
                  :class="{
                    'd-none': accrodion2Idx !== 5
                  }"
                >
                  <div class="inner">
                    <p>
                      Discover the beauty of the world around you, immerse
                      yourself in diverse cultures, and create lasting memories
                      through your travels. Embrace every moment as an
                      opportunity for growth and adventure
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="call-to-action pb-0 bg-lgrey border-t">
    <div class="container">
      <div class="section-title text-center w-75 mx-auto mb-5 px-5">
        <h2 class="mb-2">
          Do You Have Any <span class="theme">Questions?</span>
        </h2>
        <p class="mb-0">
          Discover the beauty of the world around you, immerse yourself in
          diverse cultures, and create lasting memories through your travels.
          Embrace every moment as an opportunity for growth and adventure
        </p>
      </div>

      <div class="reservation-main">
        <div class="row align-items-center">
          <div class="col-lg-6 mb-4">
            <img src="images/trending/trending4.jpg" alt="" class="rounded" />
          </div>

          <div class="col-lg-6 mb-4">
            <form method="post" @submit.prevent="() => {}">
              <div class="row">
                <div class="col-lg-6 col-md-6">
                  <div class="form-group mb-2">
                    <label>Full Name</label>

                    <input type="text" id="full-name" />
                  </div>
                </div>

                <div class="col-lg-6 col-md-6">
                  <div class="form-group mb-2">
                    <label>Phone No.</label>

                    <input type="text" id="phone-no" />
                  </div>
                </div>

                <div class="col-lg-6 col-md-6">
                  <div class="form-group mb-2">
                    <label>Email Address</label>

                    <input type="email" id="email-name" />
                  </div>
                </div>

                <div class="col-lg-6 col-md-6">
                  <div class="form-group mb-2">
                    <label>Destionation</label>

                    <div class="input-box">
                      <select class="niceSelect">
                        <option value="1">Albania</option>
                        <option value="2">Belgium</option>
                        <option value="3">Canada</option>
                      </select>
                    </div>
                  </div>
                </div>

                <div class="col-lg-12">
                  <div class="form-group mb-2">
                    <label>Message</label>

                    <textarea
                      name="message"
                      placeholder="Type your message here..."
                    ></textarea>
                  </div>
                </div>
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
  </section>

  <DiscountAction style="padding-top: 0 !important" />

  <Footer />
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
</style>
