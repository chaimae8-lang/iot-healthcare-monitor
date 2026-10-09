import paho.mqtt.client as mqtt
import time
import random
import json

# Configuration MQTT
BROKER = "localhost"
PORT = 1883
TOPIC_TEMPLATE = "patients/{}/data"

# Liste des patients simulés
patients = [
    {"id": "P001", "name": "Patient 1"},
    {"id": "P002", "name": "Patient 2"},
    {"id": "P003", "name": "Patient 3"},
    {"id": "P004", "name": "Patient 4"},
    {"id": "P005", "name": "Patient 5"},
]

# Connexion au broker
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

def generate_data(patient_id):
    """ Génère des données biométriques réalistes avec anomalies aléatoires """
    # Valeurs normales
    bpm = random.randint(60, 100)
    temp = round(random.uniform(36.5, 37.5), 1)
    spo2 = random.randint(95, 100)
    sys = random.randint(110, 130)
    dia = random.randint(70, 85)

    # Probabilité d'anomalie (10% chance)
    if random.random() < 0.1:  
        bpm = random.choice([random.randint(40, 50), random.randint(121, 140)])
    if random.random() < 0.1:
        temp = round(random.choice([random.uniform(35.0, 35.9), random.uniform(38.6, 39.5)]), 1)
    if random.random() < 0.1:
        spo2 = random.randint(85, 91)

    data = {
        "patient_id": patient_id,
        "bpm": bpm,
        "temperature": temp,
        "spo2": spo2,
        "systolic": sys,
        "diastolic": dia
    }
    return data

# Boucle infinie de simulation
while True:
    for patient in patients:
        vitals = generate_data(patient["id"])
        payload = json.dumps(vitals)
        
        # Envoi sur le topic dynamique attendu par Node-RED
        dynamic_topic = TOPIC_TEMPLATE.format(patient["id"])
        client.publish(dynamic_topic, payload)
        
        print(f"Publié sur {dynamic_topic}: {payload}")
    time.sleep(5)
