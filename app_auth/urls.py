from django.urls import path
from .views import LoginView, LogoutView, ChangePasswordView, MeView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('me/', MeView.as_view(), name='me'),
]
