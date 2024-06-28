from django.shortcuts import render
from .models import Timetable, Class, Teacher, Subject
import random
from django.http import JsonResponse
from datetime import time

def index(request):
    timetables = Timetable.objects.all()
    return render(request, 'timetable/index.html', {'timetables': timetables})

def generate_timetable(request):
    Timetable.objects.all().delete()
    classes = Class.objects.all()
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    time_slots = [(time(9, 0), time(10, 0)), (time(10, 0), time(11, 0)), (time(11, 0), time(12, 0)),
                  (time(13, 0), time(14, 0)), (time(14, 0), time(15, 0))]

    for class_obj in classes:
        for day in days:
            for start, end in time_slots:
                subject = random.choice(subjects)
                teacher = random.choice(teachers.filter(subject=subject))
                Timetable.objects.create(
                    class_name=class_obj,
                    teacher=teacher,
                    subject=subject,
                    day=day,
                    start_time=start,
                    end_time=end
                )
    return render(request, 'timetable/generate.html')

def api_timetables(request):
    timetables = Timetable.objects.all()
    data = [{
        'class_name': t.class_name.name,
        'teacher': t.teacher.name,
        'subject': t.subject.name,
        'day': t.day,
        'start_time': t.start_time.strftime('%H:%M'),
        'end_time': t.end_time.strftime('%H:%M')
    } for t in timetables]
    return JsonResponse(data, safe=False)

