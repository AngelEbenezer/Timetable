import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import requests



def submit_timetable():
    data = {
        "day_of_week": day_entry.get(),
        "start_time": start_time_entry.get(),
        "end_time": end_time_entry.get(),
        "subject": subject_entry.get(),
        "location": location_entry.get()
    }
    response = requests.post('http://localhost:8000/api/timetable/', data=data)
    print(response.status_code, response.json())

root = ThemedTk(theme="arc")
root.title("Timetable Entry")

ttk.Label(root, text="Day of Week").grid(row=0, column=0)
day_entry = ttk.Entry(root)
day_entry.grid(row=0, column=1)

ttk.Label(root, text="Start Time").grid(row=1, column=0)
start_time_entry = ttk.Entry(root)
start_time_entry.grid(row=1, column=1)

ttk.Label(root, text="End Time").grid(row=2, column=0)
end_time_entry = ttk.Entry(root)
end_time_entry.grid(row=2, column=1)

ttk.Label(root, text="Subject").grid(row=3, column=0)
subject_entry = ttk.Entry(root)
subject_entry.grid(row=3, column=1)

ttk.Label(root, text="Location").grid(row=4, column=0)
location_entry = ttk.Entry(root)
location_entry.grid(row=4, column=1)

submit_button = ttk.Button(root, text="Submit", command=submit_timetable)
submit_button.grid(row=5, columnspan=2)

root.mainloop()

