# 🏥 Système de Surveillance Sanitaire Multi-Patients en Temps Réel (IoMT)

Ce projet implémente une plateforme IoT complète de télésurveillance médicale en temps réel, permettant de suivre les constantes vitales de plusieurs patients simultanément et de détecter les anomalies cliniques critiques.

## 🚀 Architecture Technique
* **Orchestration & Isolation** : Docker Compose
* **Simulation Multi-Agents** : Script Python 3 (bibliothèque `paho-mqtt`) simulant des constantes réalistes (BPM, SpO2, Température, Tension)
* **Bus de Messages** : Broker MQTT Mosquitto (Protocole asynchrone léger)
* **Moteur de Traitement Événementiel** : Node-RED (Classification algorithmique des alertes avec un temps de traitement < 45ms)
* **Historisation des Données** : InfluxDB v2 (Base de données orientée séries temporelles - TSDB)
* **Supervision Médicale** : Interface de visualisation unifiée avec Grafana

## 🛠️ Lancement de l'Infrastructure

### 1. Démarrer les conteneurs Docker
```bash
docker compose up -d
```

### 2. Lancer le simulateur de patients
```bash
pip install paho-mqtt
python simulation.py
```

## 📊 Accès aux Consoles
* **Node-RED (Flux de classification)** : http://localhost:1880
* **Grafana (Tableau de bord)** : http://localhost:3000 *(Identifiants : admin / admin123)*
