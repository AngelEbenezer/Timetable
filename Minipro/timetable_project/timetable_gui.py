import tkinter as tk
from tkinter import ttk
import requests

class TimetableApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timetable Viewer")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self, columns=("class_name", "teacher", "subject", "day", "start_time", "end_time"), show='headings')
        self.tree.heading("class_name", text="Class")
        self.tree.heading("teacher", text="Teacher")
        self.tree.heading("subject", text="Subject")
        self.tree.heading("day", text="Day")
        self.tree.heading("start_time", text="Start Time")
        self.tree.heading("end_time", text="End Time")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.refresh_button = tk.Button(self, text="Refresh Timetable", command=self.refresh_timetable)
        self.refresh_button.pack(pady=20)

    def refresh_timetable(self):
        response = requests.get('http://127.0.0.1:8000/timetable/api/timetables/')
        if response.status_code == 200:
            self.update_treeview(response.json())
        else:
            print("Failed to fetch timetable")

    def update_treeview(self, timetable):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for item in timetable:
            self.tree.insert('', 'end', values=(item['class_name'], item['teacher'], item['subject'], item['day'], item['start_time'], item['end_time']))

if __name__ == "__main__":
    app = TimetableApp()
    app.mainloop()
