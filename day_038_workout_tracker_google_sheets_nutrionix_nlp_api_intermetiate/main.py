"""
    Workout tracker, 
    uses nutritionix nlp to get the excercise stats
    then uses the sheety api to post the endpoint to google sheets
    A nutritionix app id and api key, as well as a sheety endpoint is needed for it to run
    the program looks for it in a secret.txt file in the same working directory, otherwise it will crash,
    you can also modify the script directly
"""

import requests
import datetime

secret_file = open("secret.txt", "r")

NUTRITIONIX_APP_ID = secret_file.readline().strip()
NUTRITIONIX_API_KEY = secret_file.readline().strip()
SHEETS_ENDPOINT = secret_file.readline().strip()
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

secret_file.close()


def get_exercise_stat(raw_string):
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
        "x-remote-user-id": "0"
    }
    body = {"query": raw_string, }
    response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=headers, data=body)

    return response.json()


def post_response(response):
    date_time = datetime.datetime.now()
    for exercise in response["exercises"]:
        body = {
            "workout": {
                "date": str(date_time.date()),
                "time": str(date_time.time()),
                "exercise": exercise['user_input'],
                "duration": exercise['duration_min'],
                "calories": exercise['nf_calories']
            }
        }
        response = requests.post(url=SHEETS_ENDPOINT, json=body)
        print(response.text)


def run():
    workout_done = input("Tell me what exercise have you done: ")
    workout_done = workout_done if workout_done != "" else "I played soccer for 1 hour and dance for 20 minutes"
    processed_response = get_exercise_stat(workout_done)
    post_response(processed_response)


if __name__ == '__main__':
    run()