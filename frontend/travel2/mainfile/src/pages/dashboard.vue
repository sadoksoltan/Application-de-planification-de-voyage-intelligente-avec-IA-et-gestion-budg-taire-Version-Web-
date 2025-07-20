<template>
  <div class="dashboard-hero">
    <div class="dashboard-hero-bg"></div>
    <div class="dashboard-hero-content">
      <h1>
        <span class="gradient-text">Admin Dashboard</span>
      </h1>
    </div>
  </div>
  <div class="dashboard-container">
    <div class="dashboard-sections">
      <!-- Utilisateurs -->
      <section class="dashboard-section glass">
        <div class="section-icon users">
          <i class="fas fa-users"></i>
        </div>
        <h2>Utilisateurs</h2>
        <ul>
          <li>
            <router-link to="/users"
              ><i class="fas fa-user-cog"></i> Gérer les
              utilisateurs</router-link
            >
          </li>
          <li>
            <router-link to="/users/create"
              ><i class="fas fa-user-plus"></i> Ajouter un
              utilisateur</router-link
            >
          </li>
        </ul>
      </section>

      <!-- Réservations -->
      <section class="dashboard-section glass">
        <div class="section-icon bookings">
          <i class="fas fa-calendar-check"></i>
        </div>
        <h2>Réservations</h2>
        <ul>
          <li>
            <router-link to="/admin/reservations"
              ><i class="fas fa-list"></i> Voir toutes les
              réservations</router-link
            >
          </li>
          <li>
            <router-link to="/bookings/calendar">
              <i class="fas fa-calendar-alt"></i> Calendrier des réservations
            </router-link>
          </li>
        </ul>
      </section>

      <!-- Destinations -->
      <section class="dashboard-section glass">
        <div class="section-icon destinations">
          <i class="fas fa-map-marked-alt"></i>
        </div>
        <h2>Destinations</h2>
        <ul>
          <li>
            <router-link to="/destination-list"
              ><i class="fas fa-map"></i> Liste des destinations</router-link
            >
          </li>
        </ul>
      </section>

      <!-- Tours -->
      <section class="dashboard-section glass">
        <div class="section-icon tours">
          <i class="fas fa-route"></i>
        </div>
        <h2>Tours</h2>
        <ul>
          <li>
            <router-link to="/admin/tours"
              ><i class="fas fa-list-ul"></i> Liste des tours</router-link
            >
          </li>
          <li>
            <router-link to="/admin/tours/create"
              ><i class="fas fa-plus"></i> Ajouter un tour</router-link
            >
          </li>
        </ul>
      </section>

      <!-- Blog -->
      <section class="dashboard-section glass">
        <div class="section-icon blog">
          <i class="fas fa-blog"></i>
        </div>
        <h2>Blog</h2>
        <ul>
          <li>
            <router-link to="/admin/posts"
              ><i class="fas fa-newspaper"></i> Liste des articles</router-link
            >
          </li>
          <li>
            <router-link to="/admin/posts/create"
              ><i class="fas fa-pen"></i> Ajouter un article</router-link
            >
          </li>
        </ul>
      </section>

      <!-- Statistiques -->
      <section class="dashboard-section glass">
        <div class="section-icon stats">
          <i class="fas fa-chart-line"></i>
        </div>
        <h2>Statistiques</h2>
        <ul>
          <li>
            <router-link to="/stats"
              ><i class="fas fa-chart-pie"></i> Voir les
              statistiques</router-link
            >
          </li>
        </ul>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
// Ici tu peux ajouter des appels API ou de la logique si besoin
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

.dashboard-hero {
  position: relative;
  width: 100vw;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  min-height: 260px;
  background: linear-gradient(120deg, #10a7a7 0%, #2dd4bf 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.dashboard-hero-bg {
  position: absolute;
  width: 100%;
  height: 100%;
  background: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80')
    center/cover no-repeat;
  opacity: 0.18;
  z-index: 1;
}
.dashboard-hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  color: #fff;
  padding: 40px 0 20px 0;
}
.gradient-text {
  background: linear-gradient(90deg, #fff 100% /* turquoise */);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: 2.8rem;
  font-weight: 900;
  letter-spacing: 2px;
}
.dashboard-subtitle {
  font-size: 1.2rem;
  margin-top: 12px;
  color: #e0f7fa;
  font-weight: 500;
  text-shadow: 0 1px 8px rgba(16, 167, 167, 0.1);
}

.dashboard-container {
  max-width: 1200px;
  margin: -60px auto 40px auto;
  padding: 32px 18px 18px 18px;
  background: transparent;
  border-radius: 18px;
  box-shadow: none;
}
.dashboard-sections {
  display: flex;
  flex-wrap: wrap;
  gap: 36px;
  justify-content: center;
}
.dashboard-section {
  flex: 1 1 320px;
  min-width: 320px;
  max-width: 370px;
  background: rgba(255, 255, 255, 0.85);
  border-radius: 18px;
  padding: 32px 24px 24px 24px;
  margin-bottom: 16px;
  box-shadow: 0 6px 32px rgba(16, 167, 167, 0.13),
    0 1.5px 8px rgba(0, 0, 0, 0.04);
  position: relative;
  transition: transform 0.18s, box-shadow 0.18s;
  border: 1.5px solid #e0f2f1;
  overflow: hidden;
}
.dashboard-section:hover {
  transform: translateY(-8px) scale(1.03);
  box-shadow: 0 12px 40px rgba(16, 167, 167, 0.18),
    0 2px 12px rgba(0, 0, 0, 0.07);
  border-color: #10a7a7;
}
.section-icon {
  width: 54px;
  height: 54px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  margin-bottom: 18px;
  box-shadow: 0 2px 12px rgba(16, 167, 167, 0.1);
  background: linear-gradient(135deg, #10a7a7 60%, #2dd4bf 100%);
  color: #fff;
  border: 2px solid #fff;
}
.section-icon.users {
  background: linear-gradient(135deg, #10a7a7 60%, #2dd4bf 100%);
}
.section-icon.bookings {
  background: linear-gradient(135deg, #2dd4bf 60%, #10a7a7 100%);
}
.section-icon.destinations {
  background: linear-gradient(135deg, #10a7a7 60%, #fbbf24 100%);
}
.section-icon.tours {
  background: linear-gradient(135deg, #2dd4bf 60%, #f472b6 100%);
}
.section-icon.blog {
  background: linear-gradient(135deg, #fbbf24 60%, #10a7a7 100%);
}
.section-icon.stats {
  background: linear-gradient(135deg, #10a7a7 60%, #6366f1 100%);
}
.section-icon.settings {
  background: linear-gradient(135deg, #2dd4bf 60%, #10a7a7 100%);
}

.dashboard-section h2 {
  color: #10a7a7;
  font-size: 1.25rem;
  margin-bottom: 16px;
  font-weight: 700;
  letter-spacing: 1px;
}
.dashboard-section ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.dashboard-section li {
  margin-bottom: 12px;
}
.dashboard-section a {
  color: #222;
  text-decoration: none;
  font-weight: 500;
  font-size: 1.08rem;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: color 0.2s, transform 0.15s;
  border-radius: 6px;
  padding: 6px 0 6px 0;
}
.dashboard-section a:hover {
  color: #10a7a7;
  background: #e0f7fa;
  transform: translateX(6px) scale(1.04);
  text-decoration: underline;
}
.stats-nav-bar-inside .stats-btn {
  pointer-events: auto;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  background: linear-gradient(90deg, #10a7a7 30%, #2dd4bf 70%);
  color: #fff;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  padding: 10px 22px;
  font-size: 1.05rem;
  text-decoration: none;
  box-shadow: 0 2px 8px rgba(16, 167, 167, 0.1);
  transition: background 0.18s, transform 0.15s;
}
.stats-nav-bar-inside .stats-btn:hover {
  background: linear-gradient(90deg, #2dd4bf 30%, #10a7a7 100%);
  color: #fff;
  transform: scale(1.04);
  text-decoration: none;
}
.stats-nav-bar-inside .stats-btn i {
  font-size: 1.2em;
  margin-right: 6px;
}
@media (max-width: 1200px) {
  .dashboard-sections {
    flex-direction: column;
    gap: 0;
    align-items: center;
  }
  .dashboard-section {
    min-width: unset;
    max-width: 98vw;
    margin-bottom: 28px;
  }
}
</style>
