import requests
from datetime import datetime
import os

# User details for the Nutritionix API.
GENDER = "male"
WEIGHT_KG = 76
HEIGHT_CM = 177
AGE = 24

# API credentials from environment variables.
X_APP_ID  = os.getenv("NUTRITIONIX_APP_ID")
X_APP_KEY = os.getenv("NUTRITIONIX_API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Get exercise details from user.
exercise_input = input("Enter your exercises: ")

# Headers and paramaters for Nutritionix API request.
nutritionix_headers = {
    "x-app-id": X_APP_ID,
    "x-app-key": X_APP_KEY,
}

nutritionix_paramaters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Making the request to the Nutritionix API.
try:
    nutritionix_response = requests.post(exercise_endpoint, json=nutritionix_paramaters, headers=nutritionix_headers)
    nutritionix_response.raise_for_status()
    exercise_data = nutritionix_response.json()
    print("Nutritionix Response: \n", exercise_data, "\n")
except requests.RequestException as e:
    print("Error during Nutritionix API call:", e)
    exit()

# Date and time for logging.
current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")

# Sheety API endpoint and credentials.
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
sheety_username = os.getenv("SHEETY_USERNAME")
sheety_password = os.getenv("SHEETY_PASSWORD")

# Sending data to Sheety using Basic Authentication.
for exercise in exercise_data["exercises"]:
    sheety_data = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    try:
        sheety_response = requests.post(sheety_endpoint, json=sheety_data, auth=(sheety_username, sheety_password))
        sheety_response.raise_for_status()
        print("Sheety Response: \n", sheety_response.text)
    except requests.RequestException as e:
        print("Error during Sheety API call:", e)