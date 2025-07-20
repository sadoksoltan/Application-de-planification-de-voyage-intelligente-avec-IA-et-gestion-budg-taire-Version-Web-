<script setup lang="ts">
import BG1Image from 'assets/images/bg/bg1.jpg'
import Shape8Image from 'assets/images/shape8.png'

defineProps<{
  headline?: string
  pageTitle: string
}>()
</script>

<template>
  <section
    class="breadcrumb-main pb-20 pt-14"
    :style="{ backgroundImage: `url('${BG1Image}')` }"
  >
    <div
      class="section-shape section-shape1 top-inherit bottom-0"
      :style="{ backgroundImage: `url('${Shape8Image}')` }"
    ></div>

    <div class="breadcrumb-outer">
      <div class="container">
        <div class="breadcrumb-content text-center">
          <h1 class="mb-3">{{ headline ?? pageTitle }}</h1>

          <nav aria-label="breadcrumb" class="d-block">
            <ul class="breadcrumb">
              <li class="breadcrumb-item">
                <a href="#">Home</a>
              </li>

              <li class="breadcrumb-item active" aria-current="page">
                {{ pageTitle }}
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </div>

    <div class="dot-overlay"></div>
  </section>
</template>
