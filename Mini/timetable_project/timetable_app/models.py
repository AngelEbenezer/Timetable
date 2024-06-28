from django.db import models

class TimetableEntry(models.Model):
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subject} on {self.day_of_week} from {self.start_time} to {self.end_time}"

