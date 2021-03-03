import os
import requests
from datetime import datetime as dt

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
TOKEN_SHEETY = os.getenv('TOKEN_SHEETY')
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_get_endpoint = "https://api.sheety.co/5d9e47121f37ae92e90f2f341f1d3f5d/myWorkouts/workouts"
sheety_post_endpoint= "https://api.sheety.co/5d9e47121f37ae92e90f2f341f1d3f5d/myWorkouts/workouts"
today = dt.now()
exercise_input = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
 "query": exercise_input,
 "gender": "male",
 "weight_kg": 69.0,
 "height_cm": 163.00,
 "age": 20
}

response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
exercises_data = response.json()['exercises']

sheet_headers = {"Authorization": f"Bearer {TOKEN_SHEETY} "}
for exercise in exercises_data:
    json = {"workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise['name'].title(),
        "duration": round(exercise['duration_min']),
        "calories": round(exercise['nf_calories'])
    }}

    response_sheet = requests.post(url=sheety_post_endpoint, json=json, headers=sheet_headers)
    print(response_sheet.text)
