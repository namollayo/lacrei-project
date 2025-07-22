# api/views.py

from rest_framework import viewsets, generics
from .models import Professional, Appointment
from .serializers import ProfessionalSerializer, AppointmentSerializer

class ProfessionalViewSet(viewsets.ModelViewSet):

    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

class AppointmentViewSet(viewsets.ModelViewSet):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentByProfessionalView(generics.ListAPIView):

    serializer_class = AppointmentSerializer

    def get_queryset(self):

        professional_id = self.kwargs['professional_id']
        return Appointment.objects.filter(professional_id=professional_id)
