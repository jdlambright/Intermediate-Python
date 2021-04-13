import requests
from datetime import date time
import os

GENDER = "Male"
WEIGHT_KG = ""
HEIGHT_CM = YOUR HEIGHT
AGE = YOUR AGE

APP_ID ="956ea38b"
API_KEY ="517fb868f9df96dc551f47993340a82f"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_query = input("what did you do today?")

exercise_headers = {
    "x-app-id": APP_ID,
    "x-api-key": API_KEY,

}

exercise_parameters = {
    "query": exercise_query,
}

response = requests.post(exercise_endpoint, params=exercise_parameters, headers=exercise_headers)
print(response.text)