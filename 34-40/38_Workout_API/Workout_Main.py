import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = 66
HEIGHT_CM = 1.8
AGE = 35

APP_ID ="956ea38b"
API_KEY ="517fb868f9df96dc551f47993340a82f"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/nat"
sheet_endpoint = "https://api.sheety.co/be411e8cf62d3966a9666c5b539f30ea/cambrightTest/sheet1"

exercise_text = input("Tell me which exercises you did: ")

exercise_headers = {
    "x-app-id": APP_ID,
    "x-api-key": API_KEY,

}

exercise_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, params=exercise_parameters, headers=exercise_headers)
print(response.text)
result= response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #No Auth
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)