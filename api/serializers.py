from rest_framework import serializers
from .models import Professional, Appointment
from django.utils import timezone
from django.core.validators import validate_email
import bleach
import re

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'

    def validate_social_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("O nome social não pode estar vazio.")
        return bleach.clean(value, tags=[], strip=True)

    def validate_profession(self, value):
        if not value.strip():
            raise serializers.ValidationError("A profissão não pode estar vazia.")
        return bleach.clean(value, tags=[], strip=True)

    def validate_address(self, value):
        if not value.strip():
            raise serializers.ValidationError("O endereço não pode estar vazio.")
        return bleach.clean(value, tags=[], strip=True)

    def validate_contact(self, value):
        value = bleach.clean(value, tags=[], strip=True)
        if not value.strip():
            raise serializers.ValidationError("O contato não pode estar vazio.")
        
        # Validação de e-mail !!!!!!!!!!!!!!!!!!!
        try:
            validate_email(value)
            return value
        except serializers.ValidationError:
            pass
        
        # Validação de telefone (ex.: (11) 91234-5678, +5511912345678, 11912345678)
        phone_pattern = r'^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
        if not re.match(phone_pattern, value):
            raise serializers.ValidationError("O contato deve ser um e-mail ou número de telefone válido.")
        return value

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        extra_kwargs = {
            'date': {'format': '%Y-%m-%dT%H:%M:%SZ'}
        }

    def validate_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("A data da consulta não pode ser no passado.")
        return value

    def validate_professional(self, value):
        if not Professional.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("O profissional não existe.")
        return value
