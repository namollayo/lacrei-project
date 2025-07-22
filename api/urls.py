# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessionalViewSet, AppointmentViewSet, AppointmentByProfessionalView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'professionals', ProfessionalViewSet)
router.register(r'appointments', AppointmentViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('appointments/by-professional/<int:professional_id>/', AppointmentByProfessionalView.as_view(), name='appointments-by-professional'),
]
