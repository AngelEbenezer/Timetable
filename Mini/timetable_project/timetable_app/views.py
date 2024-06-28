from rest_framework import generics
from .models import TimetableEntry
from .serializers import TimetableEntrySerializer

class TimetableEntryCreateView(generics.CreateAPIView):
    queryset = TimetableEntry.objects.all()
    serializer_class = TimetableEntrySerializer

