from rest_framework import serializers
from .models import Payment
from app_users.serializers import StudentSerializer

class PaymentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'student', 'amount', 'date', 'description']
