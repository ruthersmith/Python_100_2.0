"""
    Author: Ruthersmith Bercy
    Workout Tracker

    A command-line application that parses natural-language exercise input,
    retrieves structured workout statistics from a mock NLP API, and logs
    the results to a Google Sheets spreadsheet using the Sheety API.

    Originally built using the Nutritionix NLP API, this version replaces
    Nutritionix with a mock API that provides similar exercise parsing
    functionality due to changes in Nutritionix's free tier availability.

    Workflow:
    1. User provides a natural language description of exercise
    (e.g., "Swam for an hour").
    2. The program sends the input to a mock NLP API to extract:
    - Exercise type
    - Duration
    - Other relevant statistics
    3. The parsed data is then posted to a Google Sheets document
    via the Sheety API.

    Environment Variables:
    This program requires a `.env` file containing necessary API keys,
    authentication credentials, and endpoint URLs.

    It is recommended to include a `.env.dist` file as a template
    for required environment variables.

    The application is implemented as a single-file program
    containing the `WorkoutTracker` class.

     How to run:
        python main.py

"""


from dotenv import load_dotenv
import os
import requests
import datetime

load_dotenv()

class WorkoutTracker:
    """Core controller for the Workout Tracker application."""
    
    def __init__(self):
        
        self.nutritionix_app_id = os.getenv("NUTRITIONIX_APP_ID")
        self.nutritionix_app_key = os.getenv("NUTRITIONIX_API_KEY")
        self.nutritionix_base_endpoint = os.getenv("NUTRITIONIX_ENDPOINT")
        self.sheets_endpoint = os.getenv("SHEETS_ENDPOINT")
        self.sheets_bearer_token = os.getenv("SHEETS_BEARER_TOKEN")

    def get_exercise_stat(self, raw_string):
        """
            Sends a natural-language exercise description to the mock NLP API
            and retrieves structured workout statistics.

            Parameters:
            - raw_string (str): Natural-language input describing the workout
            (e.g., "Ran 3 miles", "Swam for 45 minutes").
        """
        url = f"{self.nutritionix_base_endpoint}/v1/nutrition/natural/exercise"

        headers = {
            "x-app-id": self.nutritionix_app_id,
            "x-app-key": self.nutritionix_app_key,
            "Content-Type": "application/json"
        }

        data = {"query": raw_string, }
        response = requests.post(url=url, headers=headers, json=data)

        return response.json()

    
    def post_excercise_stats_to_sheets(self, excercise_stats):
        """
            Posts structured exercise statistics to a Google Sheets document
            using the Sheety API.
        """
        
        headers = {"Authorization" : f"Bearer {self.sheets_bearer_token}"}
        date_time = datetime.datetime.now()
        
        for exercise in excercise_stats["exercises"]:
            body = {
                "workout": {
                    "date": str(date_time.date()),
                    "time": str(date_time.time()),
                    "exercise": exercise['user_input'],
                    "duration": exercise['duration_min'],
                    "calories": exercise['nf_calories']
                }
            }
            response = requests.post(url=self.sheets_endpoint, json=body, headers=headers)
            print(response.text)


    def run(self):
        workout_done = input("Tell me what exercise have you done: ")
        processed_response = self.get_exercise_stat(workout_done)
        self.post_excercise_stats_to_sheets(processed_response)


if __name__ == '__main__':
    tracker = WorkoutTracker()
    tracker.run()
