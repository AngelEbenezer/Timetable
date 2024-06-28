from django.urls import path
from .views import TimetableEntryCreateView

urlpatterns = [
    path('api/timetable/', TimetableEntryCreateView.as_view(), name='timetable-entry-create'),
]




