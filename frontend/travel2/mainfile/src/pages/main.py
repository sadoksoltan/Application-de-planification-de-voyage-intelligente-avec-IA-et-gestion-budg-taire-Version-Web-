from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
from scipy.sparse import hstack, vstack
from math import radians, cos, sin, asin, sqrt

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fonction de calcul de distance haversine
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Rayon de la Terre en km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    return R * c

# Coordonnées des centres-villes
VILLE_CENTRES = {
    'tunis': (36.81897, 10.16579),
    'la goulette': (36.85222, 10.32500),
    'le bardo': (36.80333, 10.14444),
    'carthage': (36.85833, 10.33222),
    'manouba': (36.80000, 10.10000),
    'hrairia': (36.80333, 10.17833),
    'cite ettadhamen': (36.80000, 10.15000),
    'fouchana': (36.75000, 10.25000),
    'le kram': (36.86000, 10.33000),
    'mourouj': (36.75000, 10.25000),
    'sijoumi': (36.80000, 10.20000),
    'ghazela': (36.85000, 10.30000),
    'radès': (36.75000, 10.25000),
    'ariana': (36.86667, 10.10000),
    'ezzahra': (36.75000, 10.25000),
    'rades': (36.75000, 10.25000),
    'ezzhouhour': (36.75000, 10.25000),
    'mnihla': (36.80000, 10.20000),
    'khalidia': (36.80000, 10.20000),
    'ariana ville': (36.86667, 10.10000),
    'kalatin': (36.80000, 10.20000),
    'saouaf': (36.80000, 10.20000),
    'raoued': (36.80000, 10.20000),
    'bizerte': (37.27417, 9.87333),
    'tinja': (37.20000, 9.70000),
    'menzel abderrahmane': (37.20000, 9.80000),
    'dugga': (36.46000, 9.22000),
    'teboulba': (35.70000, 10.75000),
    'el alia': (37.00000, 9.50000),
    'el battah': (37.10000, 9.60000),
    'beja': (36.73333, 9.18333),
    'testour': (36.80000, 9.20000),
    'oum-hadjer': (36.90000, 9.30000),
    'el ksour': (36.95000, 9.35000),
    'teboursouk': (36.95000, 9.40000),
    'tlet': (36.95000, 9.45000),
    'jendouba': (36.50000, 8.76667),
    'boussalem': (36.50000, 8.80000),
    'aïn draham': (36.50000, 8.90000),
    'fériana': (35.50000, 8.50000),
    'menzel bouzelfa': (35.50000, 8.60000),
    'tella': (35.50000, 8.70000),
    'aïn kercha': (35.50000, 8.80000),
    'kairouan': (35.67611, 9.87667),
    'chebika': (35.50000, 9.50000),
    'baghdadi': (35.50000, 9.60000),
    'hajeb el ayoun': (35.50000, 9.70000),
    'hammam-lif': (36.75000, 10.25000),
    'hicheur': (35.75000, 9.75000),
    'haffouz': (35.75000, 9.85000),
    'sousse': (35.82500, 10.63611),
    'kanta': (35.80000, 10.60000),
    'sidi bou ali': (35.80000, 10.70000),
    'hergla': (35.80000, 10.80000),
    'msaken': (35.80000, 10.90000),
    'marsa sghira': (35.80000, 11.00000),
    'hammam sousse': (35.80000, 11.10000),
    'monastir': (35.76667, 10.81667),
    'ksar said': (35.75000, 10.90000),
    'el hamma': (35.75000, 10.95000),
    'ksar hellal': (35.75000, 11.00000),
    'sahline': (35.75000, 11.05000),
    'sidi el hadj el bedi': (35.75000, 11.10000),
    'zeramdine': (35.75000, 11.15000),
    'mahdia': (35.50000, 11.00000),
    'sayada': (35.50000, 11.10000),
    'sidi alouane': (35.50000, 11.20000),
    'ouled chamekh': (35.50000, 11.30000),
    'el jem': (35.50000, 11.40000),
    'sfax': (34.74000, 10.76000),
    'menzel chaker': (34.80000, 10.80000),
    'skhira': (34.90000, 10.90000),
    'chihia': (34.95000, 10.95000),
    'el ain': (34.95000, 11.00000),
    'ghraia': (34.95000, 11.05000),
    'bir ali ben kheli': (34.95000, 11.10000),
    'agareb': (34.95000, 11.15000),
    'gabès': (33.88333, 10.10000),
    'matmata': (33.46667, 9.46667),
    'hamma': (33.50000, 9.50000),
    'zarat': (33.53333, 9.53333),
    'menzel hayoun': (33.56667, 9.56667),
    'medenine': (33.35000, 10.50000),
    'ben gardane': (33.25000, 10.75000),
    'zarzis': (33.50000, 11.00000),
    'remada': (33.50000, 11.10000),
    'djerba': (33.86667, 10.85000),
    'tataouine': (32.93000, 10.44000),
    'ksar morra': (32.90000, 10.40000),
    'tozeur': (33.90000, 8.13333),
    'nefta': (33.90000, 8.20000),
    'degache': (33.90000, 8.30000),
    'hamat': (33.90000, 8.40000),
    'kasserine': (35.16667, 8.83333),
    'sbeïtla': (35.25000, 8.75000),
    'sbitla': (35.25000, 8.75000),
    'djelfa': (34.66667, 8.50000),
    'gafsa': (34.42500, 8.78333),
    'metlaoui': (34.40000, 8.70000),
    'reymada': (34.40000, 8.60000),
    'el ksar': (34.40000, 8.50000),
    'el guettar': (34.40000, 8.40000),
    'siliana': (36.08333, 9.38333),
    'el aroussa': (36.10000, 9.40000),
    'el ksiba': (36.10000, 9.50000),
    'rafraf': (36.10000, 9.60000),
    'zaghouan': (36.40000, 9.50000),
    'bir mcherga': (36.40000, 9.60000),
    'el fahs': (36.40000, 9.70000),
    'nabeul': (36.45000, 10.00000),
    'kélibia': (36.50000, 10.30000),
    'hammamet': (36.61667, 10.61667),
    'sidi bou rhail': (36.70000, 10.70000),
    'menzel jemil': (36.80000, 10.80000),
    'menzel bourguiba': (36.90000, 10.90000),
    'el kef': (36.16667, 8.70000),
    'tajerouine': (36.20000, 8.80000),
    'kef': (36.20000, 8.90000),
    'jandouba': (36.50000, 8.76667),
    'la marsa': (36.86000, 10.30000),
    'mateur': (37.05000, 9.65000),
    'ksar es-sid': (36.90000, 9.20000),
    'douz': (33.46000, 9.02000),
    'kebili': (33.70000, 8.96667),
    'tabarka': (36.95000, 8.76000),
}

# Chargement des artefacts
artefacts = {
    "2j": {
        "model": joblib.load("meilleur_modele_2jr.joblib"),
        "tfidf_desc": joblib.load("tfidf_desc_2jr.joblib"),
        "tfidf_interet": joblib.load("tfidf_interet_2jr.joblib"),
        "scaler_note": joblib.load("scaler_note_2jr.joblib"),
        "scaler_prix": joblib.load("scaler_prix_2jr.joblib"),
        "df": pd.read_csv("dataset_2j.csv").dropna(subset=['latitude', 'longitude'])
    },
    "7j": {
        "model": joblib.load("meilleur_modele_7jr.joblib"),
        "tfidf_desc": joblib.load("tfidf_desc_7jr.joblib"),
        "tfidf_interet": joblib.load("tfidf_interet_7jr.joblib"),
        "scaler_note": joblib.load("scaler_note_7jr.joblib"),
        "scaler_prix": joblib.load("scaler_prix_7jr.joblib"),
        "df": pd.read_csv("dataset_7j.csv").dropna(subset=['latitude', 'longitude'])
    },
    "14j": {
        "model": joblib.load("meilleur_modele_14jr.joblib"),
        "tfidf_desc": joblib.load("tfidf_desc_14jr.joblib"),
        "tfidf_interet": joblib.load("tfidf_interet_14jr.joblib"),
        "scaler_note": joblib.load("scaler_note_14jr.joblib"),
        "scaler_prix": joblib.load("scaler_prix_14jr.joblib"),
        "df": pd.read_csv("dataset_14j.csv").dropna(subset=['latitude', 'longitude'])
    },
    "21j": {
        "model": joblib.load("meilleur_modele_21jr.joblib"),
        "tfidf_desc": joblib.load("tfidf_desc_21jr.joblib"),
        "tfidf_interet": joblib.load("tfidf_interet_21jr.joblib"),
        "scaler_note": joblib.load("scaler_note_21jr.joblib"),
        "scaler_prix": joblib.load("scaler_prix_21jr.joblib"),
        "df": pd.read_csv("dataset_21j.csv").dropna(subset=['latitude', 'longitude'])
    },
}

# Schéma de la requête
class RecoRequest(BaseModel):
    ville: str
    budget: float
    interets: str
    periode: str
    top_k: int = 2

@app.post("/recommander/")
def recommander(req: RecoRequest):
    periode = req.periode
    if periode not in artefacts:
        return {"error": "Période non supportée"}

    art = artefacts[periode]
    df = art["df"]
    ville_lower = req.ville.lower()
    df_temp = df[df['prix'] <= req.budget].copy()

    # Filtrage géographique si ville connue
    if ville_lower in VILLE_CENTRES:
        lat_centre, lon_centre = VILLE_CENTRES[ville_lower]
        df_temp['distance_centre'] = df_temp.apply(
            lambda row: haversine(lat_centre, lon_centre, row['latitude'], row['longitude']), axis=1
        )
        df_filtre = df_temp[df_temp['distance_centre'] <= 15].copy()
    else:
        filtres = (df['ville'].str.lower().str.contains(req.ville.lower())) & (df['prix'] <= req.budget)
        df_filtre = df[filtres].copy()

    if df_filtre.empty:
        return {"result": []}

    # **Correction ici : remplacer NaN dans description**
    df_filtre['description'] = df_filtre['description'].fillna('')

    # Prétraitement intérêts
    interets_proc = ', '.join([i.strip().capitalize() for i in req.interets.split(',') if i.strip()])

    desc_vect = art["tfidf_desc"].transform(df_filtre['description'])
    interet_vect = art["tfidf_interet"].transform([interets_proc])
    interet_vect_rep = vstack([interet_vect] * len(df_filtre))
    X_combined = hstack([desc_vect, interet_vect_rep])
    scores = art["model"].predict(X_combined)
    df_filtre['score_recommandation'] = scores

    # Tri final
    recommandations = df_filtre.sort_values('score_recommandation', ascending=False).head(req.top_k * 2)

    # Supprimer doublons
    recommandations = recommandations.drop_duplicates(subset=['nom', 'prix', 'note'])

    # Garder les top_k après filtrage
    recommandations = recommandations.head(req.top_k)

    return {
        "result": recommandations[[
            'ville', 'nom', 'note', 'prix', 'interets', 'lien',
            'score_recommandation', 'distance_centre'
        ]].to_dict(orient='records')
    }
