from todoist_api_python.api import TodoistAPI
import datetime
import os

# grab api key using os.getenv from .env file

todoist_api_key = os.getenv('TODOIST_API_KEY')
api = TodoistAPI(todoist_api_key)

today = datetime.date.today()

print(today)

# TODO:
# 1. Get all tasks assigned in the morning
# 2. Count the number of completed tasks by 11pm
# 3. Print the number of tasks completed out of the total number of tasks assigned
# 4. Print the percentage of tasks completed
# 5. Email the results to myself and cc the mrs (optional)