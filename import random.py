import random
import time

# Function to simulate sensor data
def get_health_data():
    heart_rate = random.randint(60, 120)        # bpm
    temperature = round(random.uniform(36.0, 39.0), 1)  # °C
    spo2 = random.randint(85, 100)              # %

    return heart_rate, temperature, spo2

# Function to check health conditions
def check_health(hr, temp, spo2):
    alerts = []

    if hr < 60 or hr > 100:
        alerts.append("Abnormal Heart Rate!")

    if temp > 37.5:
        alerts.append("High Body Temperature!")

    if spo2 < 95:
        alerts.append("Low Oxygen Level!")

    return alerts

# Main monitoring loop
print("Smart Health Monitoring System Started...\n")

for i in range(5):  # simulate 5 readings
    hr, temp, spo2 = get_health_data()

    print(f"Reading {i+1}:")
    print(f"Heart Rate: {hr} bpm")
    print(f"Temperature: {temp} °C")
    print(f"SpO2: {spo2} %")

    alerts = check_health(hr, temp, spo2)

    if alerts:
        print("ALERTS:")
        for alert in alerts:
            print(" -", alert)
    else:
        print("All readings are normal.")

    print("-" * 30)
    time.sleep(2)
    
    
    SHORT BACKSTORY
    Backstory (Short)
During the COVID-19 pandemic, many people struggled to get timely medical help due to overcrowded hospitals and lack of continuous health monitoring. In rural and semi-urban areas, patients often ignore early symptoms because regular checkups are difficult. This inspired the idea of a Smart Health Monitoring System that allows people to track their basic health parameters at home and share them with doctors remotely.

README FOR YOUR HEALYHCARE PROJECT
# Smart Health Monitoring System

## 📌 Description
This project is a simple Smart Health Monitoring System that tracks basic health parameters like heart rate, body temperature, and oxygen level (SpO2). It helps in early detection of health issues.

## 🎯 Objective
To provide a low-cost solution for monitoring health at home.

## ⚙️ Features
- Monitors Heart Rate
- Measures Body Temperature
- Tracks Oxygen Level (SpO2)
- Generates alerts for abnormal readings

## 🛠️ Technologies Used
- Python
- Random module (for simulation)

## ▶️ How to Run
1. Install Python
2. Copy the code into a `.py` file
3. Run using: