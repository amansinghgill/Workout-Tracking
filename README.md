# Workout Tracking App

## Overview
This Python application integrates with the Nutritionix API to track exercises and logs the data using the Sheety API. It is designed for users who wish to automatically record their daily exercise routines and calorie expenditure.

## Features
- **Exercise Input and Analysis**: Users can input their exercise details, which are then analyzed using the Nutritionix API to determine parameters like duration and calories burned.
- **Data Logging**: The application logs exercise details such as date, time, exercise type, duration, and calories to a spreadsheet using the Sheety API.
- **User Customization**: User details like gender, weight, height, and age can be customized for more accurate analysis.

## Prerequisites
- Python 3
- `requests` library: Install using `pip install requests`
- Nutritionix API credentials: Obtain your `APP ID` and `API KEY` from [Nutritionix](https://www.nutritionix.com/business/api).
- Sheety API credentials: Set up a Sheety project and get your endpoint, username, and password.

## Environment Setup
Store your Nutritionix and Sheety API credentials in environment variables for security:
- `NUTRITIONIX_APP_ID`
- `NUTRITIONIX_API_KEY`
- `SHEETY_ENDPOINT`
- `SHEETY_USERNAME`
- `SHEETY_PASSWORD`

## Usage
1. Run the script: `python exercise_tracker.py`
2. Enter your exercises when prompted.
3. Check your Sheety spreadsheet to see the logged data.



<p>
  <img src="https://github.com/amansinghgill/Workout-Tracking/assets/90486946/08201d01-5ec9-42b8-891d-6ab84ee40cdd" alt="example" width="650px">
</p>

<p>
  <img src="https://github.com/amansinghgill/Workout-Tracking/assets/90486946/a5022a51-8dc4-4a2e-97f0-1ff09714bb01" alt="example" width="500px">
</p>




## Customization
Modify the user details (gender, weight, height, age) in the script to reflect your personal information for more accurate exercise tracking.

