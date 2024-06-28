from django.contrib import admin
from .models import Subject, Teacher, Class, Timetable

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Timetable)


