from tkinter import *
from date import Date
from exercise_data import Exercise
import requests

date = Date()
date_string, time_string = date.current_datetime()


def get_user_text():
    """Gets user input from the tkinter entry box and storing it in the variable """
    user_input = user_entry.get()
    return user_input


def display_exercise_text():
    user_text = get_user_text()
    exercise = Exercise(user_text)
    # returning the api response from exercise api to the function for converting it into datasheet
    data = exercise.makes_data_for_sheety()
    label_exercise_text.config(text=data["exercise"])
    label_duration_text.config(text=data["duration"])
    label_calories_text.config(text=data["calories"])


def add_data():
    """Accepts data as the parameters and adds it to the list"""
    exercise = Exercise(get_user_text())
    data = exercise.makes_data_for_sheety()
    sheety_api = 'https://api.sheety.co/a0a4b1970c6dcbbe06e3caadbe1e830c/workout/sheet1'
    # Parameters for sheety sheets
    parameters = {"sheet1": data}
    # Authentication header for sheety
    sheety_headers = {'Authorization': 'Basic c3VwZXJub3ZhMzA6U3VwZXJub3ZhQDMw'}
    # post requests for sheety api
    response2 = requests.post(sheety_api, json=parameters, headers=sheety_headers)
    response2.raise_for_status()
    if 200 <= response2.status_code < 300:
        print("Record added successfully")
    label_confirmation = Label(text="Record added successfully!", bg="burlywood1", font=("Courier", 25, "bold"))
    label_confirmation.grid(row=7, column=1)


# Creating the user interface for the app
window = Tk()
window.maxsize(1200, 1200)
window.title("Workout Tracker")
window.resizable(False,False)
window.config(padx=100, pady=50, bg="burlywood1")
label_title = Label(text="WORKOUT TRACKER", bg="burlywood1", font=("Courier", 45, "bold"))
label_title.grid(row=0, column=1, columnspan=2)
label_date = Label(text="DATE", bg="burlywood1", font=("Courier", 25, "bold"))
label_date.grid(row=1, column=0)
label_date_text = Label(text=f"{date_string}", bg="burlywood1", font=("Courier", 25, "bold"))
label_date_text.grid(row=1, column=1)
label_title_question = Label(text="USER-TEXT", bg="burlywood1", font=("Courier", 25, "bold"))
label_title_question.grid(row=2, column=0)
user_entry = Entry(bg="burlywood1", fg="black", font=("Courier", 25, "normal"))
user_entry.grid(row=2, column=1, columnspan=2)
submit_button = Button(text="Submit", height=2, width=6, command=display_exercise_text, bg="burlywood1", fg="black",
                       font=("Courier", 25, "bold"))
submit_button.grid(row=2, column=3)
label_exercise = Label(text="EXERCISE", bg="burlywood1", font=("Courier", 25, "bold"))
label_exercise.grid(row=3, column=0)
label_exercise_text = Label(text=" ", bg="burlywood1", font=("Courier", 25, "bold"))
label_exercise_text.grid(row=3, column=1)
label_duration = Label(text="DURATION", bg="burlywood1", font=("Courier", 25, "bold"))
label_duration.grid(row=4, column=0)
label_duration_text = Label(text=" ", bg="burlywood1", font=("Courier", 25, "bold"))
label_duration_text.grid(row=4, column=1)
label_calories = Label(text="CALORIES", bg="burlywood1", font=("Courier", 25, "bold"))
label_calories.grid(row=5, column=0)
label_calories_text = Label(text=" ", bg="burlywood1", font=("Courier", 25, "bold"))
label_calories_text.grid(row=5, column=1)
add_data_button = Button(text="ADD DATA TO SHEETS", height=3, command=add_data, bg="burlywood1", fg="black",
                         font=("Courier", 25, "bold"))
add_data_button.grid(row=6, column=1)
window.mainloop()
