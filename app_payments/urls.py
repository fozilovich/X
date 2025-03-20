from django.urls import path
from .views import PaymentListCreateView, PaymentDetailView, StudentPaymentsView

urlpatterns = [
    path('payments/', PaymentListCreateView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('payments/student/<int:id>/', StudentPaymentsView.as_view(), name='student-payments'),
]
