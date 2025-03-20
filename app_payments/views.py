from rest_framework import generics
from .models import Payment
from .serializers import PaymentSerializer

class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class StudentPaymentsView(generics.ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        student_id = self.kwargs['id']
        return Payment.objects.filter(student_id=student_id)
