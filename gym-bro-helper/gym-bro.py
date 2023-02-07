import random
import os
from todoist_api_python.api import TodoistAPI

api = TodoistAPI(os.environ["TODOIST_API_TOKEN"])

# List of push workouts
push_workouts = [
    "Barbell Bench Press",
    "Dumbbell Bench Press",
    "Dumbbell Incline Press",
    "Dumbbell Flys",
    "Barbell Shoulder Press",
    "Dumbbell Shoulder Press",
    "Push Ups",
    "Tricep Dips",
    "Barbell Overhead Press",
    "Dumbbell Overhead Press",
    "Tricep Extension",
    "Tricep Kickback",
    "Pushdown",
    "Chest Flys",
    "Chest Press",
    "Shoulder Press",
    "Shoulder Flys",
    "Tricep Pushdown",
    "Tricep Dips",
    "Tricep Extension",
    "Tricep Kickback"
]

# List of pull workouts
pull_workouts = [
    "Barbell Row",
    "Dumbbell Row",
    "Lat Pulldown",
    "Pull Ups",
    "Seated Cable Row",
    "Bicep Curls",
    "Hammer Curls",
    "Cable Curls",
    "Barbell Curl",
    "Dumbbell Curl",
    "Preacher Curl",
    "Concentration Curl",
    "Pulldown",
    "Pull Up",
    "Row",
    "Deadlift",
    "Shrug",
    "Pullover",
    "Lat Raise",
    "Facepull",
    "Rear Delt Flys"
]

# List of leg workouts
leg_workouts = [
    "Squats",
    "Lunges",
    "Leg Press",
    "Step Ups",
    "Leg Extension",
    "Leg Curl",
    "Calf Raise",
    "Box Jumps",
    "Deadlift",
    "Bulgarian Split Squat",
    "Squat",
    "Step Up",
    "Jump Squat",
    "Leg Press",
    "Leg Extension",
    "Leg Curl",
    "Calf Raise",
    "Burpee",
    "Mountain Climber",
    "Jump Rope"
]

split = input("Please select a workout split (push, pull, or legs): ")

split = split.lower()

if split == "push":
    selected_workouts = random.sample(push_workouts, min(len(push_workouts), 8))
elif split == "pull":
    selected_workouts = random.sample(pull_workouts, min(len(pull_workouts), 8))
elif split == "legs":
    selected_workouts = random.sample(leg_workouts, min(len(leg_workouts), 8))
else:
    selected_workouts = []
    print("Invalid selection. Please choose 'push', 'pull', or 'legs'.")

if selected_workouts:
    print("Here are your 8 random workouts for the {} split:".format(split))
    for workout in selected_workouts:
        try:
            task = api.add_task(content=workout, project_id="2307581379")
            print(workout)
        except Exception as error:
            print(error)
