<template>
  <div class="stats-nav-bar-inside">
    <router-link to="/" class="stats-btn">
      <i class="fas fa-home"></i> Accueil
    </router-link>
  </div>
  <section class="travelia-tunisie-section">
    <div class="travelia-header">
      <img src="" class="motif-bg" />
      <h2>
        <span class="tunisian-flag">🇹🇳</span>
        Planifiez votre voyage en Tunisie avec l’IA
      </h2>
      <p class="subtitle">
        Laissez notre assistant intelligent vous proposer un itinéraire
        sur-mesure, selon vos envies tunisiennes !
      </p>
    </div>
    <div class="travelia-form-card">
      <div class="row g-3">
        <div class="col-md-6">
          <label>Ville de départ</label>
          <select v-model="iaCity" class="form-control">
            <option disabled value="">Choisissez une ville</option>
            <option v-for="v in villesTunisie" :key="v">{{ v }}</option>
          </select>
        </div>
        <div class="col-md-3">
          <label>Date début</label>
          <input type="date" v-model="iaStartDate" class="form-control" />
        </div>
        <div class="col-md-3">
          <label>Période</label>
          <select v-model="iaPeriod" class="form-control">
            <option :value="2">2 jours</option>
            <option :value="7">7 jours</option>
            <option :value="14">14 jours</option>
            <option :value="21">21 jours</option>
          </select>
        </div>
        <div class="col-12">
          <label>Budget (TND): {{ iaBudget }}</label>
          <input
            type="range"
            v-model="iaBudget"
            min="100"
            max="10000"
            step="50"
            class="form-range"
          />
        </div>
        <div class="col-12">
          <label>Centres d'intérêt</label>
          <div class="d-flex flex-wrap gap-2">
            <button
              v-for="interest in interetsTunisie"
              :key="interest.text"
              :class="[
                'interest-btn',
                iaInterests.includes(interest.text) ? 'active' : ''
              ]"
              @click="toggleIaInterest(interest.text)"
            >
              <img :src="interest.icon" class="interest-icon" />
              {{ interest.text }}
            </button>
          </div>
        </div>
        <div class="col-12">
          <label>Type de séjour</label>
          <select v-model="iaTypeSejour" class="form-control">
            <option>Solo</option>
            <option>Famille</option>
            <option>Couple</option>
            <option>Groupe</option>
          </select>
        </div>
        <div class="col-12 mt-3">
          <button
            class="nir-btn w-100 btn-teal"
            @click="searchTravelIA"
            :disabled="iaLoading"
          >
            <i class="fa fa-magic me-2"></i>
            <span v-if="!iaLoading">Générer mon itinéraire IA</span>
            <span v-else>Génération...</span>
          </button>
        </div>
        <div class="col-12 mt-2">
          <button
            class="nir-btn w-100 btn-teal"
            type="button"
            @click="resetForm"
            :disabled="iaLoading"
          >
            <i class="fa fa-undo me-2"></i>
            Réinitialiser
          </button>
        </div>
        <div v-if="iaError" class="alert alert-danger mt-3">{{ iaError }}</div>
        <div v-if="iaResultList.length" class="ia-result-special mt-3">
          <div class="ia-result-header">
            <i class="fa fa-lightbulb"></i>
            <span>Votre itinéraire IA tunisien</span>
          </div>
          <div class="ia-result-content">
            <ol>
              <li v-for="(hotel, i) in iaResultList" :key="i">
                <strong>{{ hotel.nom }}</strong> à {{ hotel.ville }} (Note:
                {{ hotel.note }}/10, Prix: {{ hotel.prix }} TND)<br />
                Distance du centre :
                {{ hotel.distance_centre?.toFixed(1) }} km<br />
                Intérêts: {{ hotel.interets }}<br />
                <a :href="hotel.lien" target="_blank">Voir l'offre</a>
              </li>
            </ol>
          </div>
        </div>
        <div v-else-if="iaResult" class="ia-result-special mt-3">
          <div class="ia-result-header">
            <i class="fa fa-lightbulb"></i>
            <span>Votre itinéraire IA tunisien</span>
          </div>
          <div class="ia-result-content">
            <pre>{{ iaResult }}</pre>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import beachIcon from './../assets/icons/beach.png'
import cultureIcon from 'assets/icons/culture.png'
import natureIcon from 'assets/icons/nature.png'
import foodIcon from 'assets/icons/food.png'
import adventureIcon from 'assets/icons/adventure.png'
import shoppingIcon from 'assets/icons/shopping.png'
import spaIcon from 'assets/icons/spa.png'

const villesTunisie = [
  'Tunis',
  'La Goulette',
  'Le Bardo',
  'Carthage',
  'Manouba',
  'Hrairia',
  'Cite Ettadhamen',
  'Fouchana',
  'Le Kram',
  'Mourouj',
  'Sijoumi',
  'Ghazela',
  'Radès',
  'Ariana',
  'Ezzahra',
  'Rades',
  'Ezzhouhour',
  'Mnihla',
  'Khalidia',
  'Ariana Ville',
  'Kalatin',
  'Saouaf',
  'Raoued',
  'Bizerte',
  'Tinja',
  'Menzel Abderrahmane',
  'Dugga',
  'Teboulba',
  'El Alia',
  'El Battah',
  'Beja',
  'Testour',
  'Oum-Hadjer',
  'El Ksour',
  'Teboursouk',
  'Tlet',
  'Jendouba',
  'Boussalem',
  'Aïn Draham',
  'Fériana',
  'Menzel Bouzelfa',
  'Tella',
  'Aïn Kercha',
  'Kairouan',
  'Chebika',
  'Baghdadi',
  'Hajeb El Ayoun',
  'Hammam-Lif',
  'Hicheur',
  'Haffouz',
  'Sousse',
  'Kanta',
  'Sidi Bou Ali',
  'Hergla',
  'Msaken',
  'Marsa Sghira',
  'Hammam Sousse',
  'Monastir',
  'Ksar Said',
  'El Hamma',
  'Ksar Hellal',
  'Sahline',
  'Sidi El Hadj El Bedi',
  'Zeramdine',
  'Mahdia',
  'Sayada',
  'Sidi Alouane',
  'Ouled Chamekh',
  'El Jem',
  'Sfax',
  'Menzel Chaker',
  'Skhira',
  'Chihia',
  'El Ain',
  'Ghraia',
  'Bir Ali Ben Kheli',
  'Agareb',
  'Gabès',
  'Matmata',
  'Hamma',
  'Zarat',
  'Menzel Hayoun',
  'Medenine',
  'Ben Gardane',
  'Zarzis',
  'Remada',
  'Djerba',
  'Tataouine',
  'Ksar Morra',
  'Tozeur',
  'Nefta',
  'Degache',
  'Hamat',
  'Kasserine',
  'Sbeïtla',
  'Sbitla',
  'Djelfa',
  'Gafsa',
  'Metlaoui',
  'Redeyef',
  'El Ksar',
  'El Guettar',
  'Siliana',
  'El Aroussa',
  'El Ksiba',
  'Rafraf',
  'Zaghouan',
  'Bir Mcherga',
  'El Fahs',
  'Nabeul',
  'Kélibia',
  'Hammamet',
  'Sidi Bou Rhail',
  'Menzel Jemil',
  'Menzel Bourguiba',
  'El Kef',
  'Tajerouine',
  'Kef',
  'Jandouba',
  'La Marsa',
  'Mateur',
  'Ksar es-Sid',
  'Douz',
  'Kebili',
  'Tabarka'
]
const interetsTunisie = [
  { text: 'Plage', icon: beachIcon },
  { text: 'Culture', icon: cultureIcon },
  { text: 'Nature', icon: natureIcon },
  { text: 'Gastronomie', icon: foodIcon },
  { text: 'Aventure', icon: adventureIcon },
  { text: 'Shopping', icon: shoppingIcon },
  { text: 'Bien-être', icon: spaIcon }
]

const iaCity = ref('')
const iaStartDate = ref('')
const iaEndDate = ref('')
const iaBudget = ref(1500)
const iaInterests = ref<string[]>([])
const iaTypeSejour = ref('Solo')
const iaLoading = ref(false)
const iaResult = ref('')
const iaError = ref('')
const iaPeriod = ref(2)
const iaResultList = ref<any[]>([])

const toggleIaInterest = (interest: string) => {
  if (iaInterests.value.includes(interest)) {
    iaInterests.value = iaInterests.value.filter((i) => i !== interest)
  } else {
    iaInterests.value.push(interest)
  }
}

const searchTravelIA = async () => {
  iaLoading.value = true
  iaError.value = ''
  iaResult.value = ''
  iaResultList.value = []
  try {
    const res = await axios.post('http://localhost:8000/api/recommander', {
      ville: iaCity.value,
      budget: Number(iaBudget.value),
      interets: iaInterests.value.map((i) => i.toLowerCase()).join(','),
      periode: iaPeriod.value + 'j',
      top_k: 2
    })
    if (res.data.result && res.data.result.length > 0) {
      iaResultList.value = res.data.result
    } else {
      iaResult.value = 'Aucune suggestion trouvée.'
    }
  } catch (e: any) {
    iaError.value =
      e.response?.data?.error || 'Erreur lors de la génération du plan'
  } finally {
    iaLoading.value = false
  }
}

const resetForm = () => {
  iaCity.value = ''
  iaStartDate.value = ''
  iaEndDate.value = ''
  iaBudget.value = 1500
  iaInterests.value = []
  iaTypeSejour.value = 'Solo'
  iaPeriod.value = 2
  iaResult.value = ''
  iaResultList.value = []
  iaError.value = ''
}
</script>

<style scoped>
.travelia-tunisie-section {
  background: #f8fcff;
  padding: 32px 0 48px 0;
  position: relative;
}
.travelia-header {
  text-align: center;
  position: relative;
  margin-bottom: 32px;
}
.motif-bg {
  position: absolute;
  left: 0;
  top: 0;
  width: 120px;
  opacity: 0.12;
}
.tunisian-flag {
  font-size: 1.5em;
  margin-right: 8px;
}
.subtitle {
  color: #009688;
  font-size: 1.1em;
  margin-top: 8px;
}
.travelia-form-card {
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 4px 24px rgba(0, 191, 165, 0.08);
  padding: 32px 24px;
  max-width: 700px;
  margin: 0 auto;
  border: 2px solid #00bfa5;
}
.interest-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  border: 1.5px solid #00bfa5;
  background: #fff;
  color: #00bfa5;
  border-radius: 24px;
  padding: 8px 18px;
  font-weight: 500;
  font-size: 1em;
  transition: background 0.2s, color 0.2s;
  cursor: pointer;
}
.interest-btn.active {
  background: #00bfa5;
  color: #fff;
}
.interest-icon {
  width: 20px;
  height: 20px;
}
.nir-btn.btn-teal {
  background: #00bfa5;
  color: #fff;
  border-radius: 30px;
  font-weight: bold;
  font-size: 1.1em;
  border: none;
}
.ia-result-special {
  background: linear-gradient(120deg, #e0f7fa 0%, #fff 100%);
  border-radius: 18px;
  box-shadow: 0 4px 24px rgba(0, 191, 165, 0.08);
  padding: 24px 18px;
  border: 1.5px solid #00bfa5;
  margin-top: 16px;
}
.ia-result-header {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: bold;
  color: #009688;
  font-size: 1.2em;
  margin-bottom: 10px;
}
.ia-result-header .fa-lightbulb {
  color: #ffd600;
  font-size: 1.5em;
}
.ia-result-content {
  font-family: 'Fira Mono', 'Consolas', monospace;
  color: #222;
  font-size: 1.05em;
  white-space: pre-line;
  background: #f8fcff;
  border-radius: 10px;
  padding: 12px;
  margin-top: 4px;
  border-left: 4px solid #00bfa5;
}
.stats-nav-bar {
  width: 100vw;
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 18px 32px 0 32px;
  box-sizing: border-box;
  z-index: 10;
}
.stats-nav-bar-inside {
  position: absolute;
  top: 18px;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding: 0 32px;
  z-index: 2;
  pointer-events: none;
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
.result-item {
  margin-bottom: 16px;
}
</style>
