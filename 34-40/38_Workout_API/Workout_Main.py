import requests


APP_ID ="956ea38b"
API_KEY ="517fb868f9df96dc551f47993340a82f"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
    "x-app-id": APP_ID,
    "x-api-key": API_KEY,
    "x-remote-user-id": "0"
}

response = requests.post(url=exercise_endpoint, headers=params)
print(response.text)