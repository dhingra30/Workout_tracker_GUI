import requests
import json
from date import Date

# Global constant variables including details of the API and the personal details
APP_ID = 'c3fe4d1c'
API_KEY = '5897dfb72778ff2209db7a00cd26a3ad'
API_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
AGE = 32
HEIGHT = 177
WEIGHT = 88


class Exercise(Date):
    def __init__(self, user_input):
        super().__init__()
        self.user_response = user_input
        self.date_string, self.time_string = self.current_datetime()

    def get_exercise_info(self):
        # Parameters and headers to go to the API post request
        params = {
            'query': self.user_response,
            'weight_kg': WEIGHT,
            'height_cm': HEIGHT,
            'age': AGE
        }
        headers = {
            'x-app-id': APP_ID,
            'x-app-key': API_KEY
        }
        # Getting the response from the API link
        response = requests.post(url=API_ENDPOINT, json=params, headers=headers)
        # Raise exceptions while trying to get the data from API
        response.raise_for_status()
        # Converting the string into a dictionary using json module
        api_response = json.loads(response.text)
        return api_response

    def makes_data_for_sheety(self):
        nutritionix_api_response = self.get_exercise_info()
        for exercises in nutritionix_api_response['exercises']:
            name_of_exercise = exercises['name'].title()
            duration = exercises['duration_min']
            calories_burnt = exercises['nf_calories']
            data_for_excel = {'date': self.date_string,
                              'time': self.time_string,
                              'exercise': name_of_exercise,
                              'duration': duration,
                              'calories': calories_burnt
                              }
            return data_for_excel
