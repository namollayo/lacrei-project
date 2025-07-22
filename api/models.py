from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Professional(models.Model):
    """Modelo para representar profissionais da saúde."""
    social_name = models.CharField(max_length=255, blank=False, null=False)
    profession = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    contact = models.CharField(max_length=100, blank=False, null=False)  # Poderia ser EmailField se for apenas e-mail

    class Meta:
        db_table = 'professionals'
        verbose_name = 'Professional'
        verbose_name_plural = 'Professionals'
        indexes = [
            models.Index(fields=['social_name']),
            models.Index(fields=['profession']),
        ]

    def __str__(self):
        return self.social_name

class Appointment(models.Model):
    def validate_future_date(value):
        if value < timezone.now():
            raise ValidationError("Insira uma data valida")
    
    date = models.DateTimeField(blank=False, null=False, validators=[validate_future_date])
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    class Meta:
        db_table = 'appointments'
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['professional']),
        ]

    def __str__(self):
        return f"{self.professional.social_name} - {self.date.strftime('%Y-%m-%d %H:%M')}"