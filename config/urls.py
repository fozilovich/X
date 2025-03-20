from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger uchun sozlamalar
schema_view = get_schema_view(
    openapi.Info(
        title="Education API",
        default_version='v1',
        description="This is the API documentation for the Education Management System",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Education Management System API</h1>")
# URL yo‘nalishlar
urlpatterns = [
    # Admin panel
    path('', home, name='home'),  # Bosh sahifa uchun yo‘nalish

    path('admin/', admin.site.urls),
    path('attendance/', include('app_attendance.urls')),  # ❗️ BU YERDA attendance BOR!
    path('courses/', include('app_courses.urls')),
    path('payments/', include('app_payments.urls')),
    path('statistics/', include('app_statistics.urls')),
    path('auth/', include('app_auth.urls')),

    path('users/', include('app_users.urls')),







    # Swagger va Redoc dokumentatsiyasi
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # Auth, Users, Courses modullari
    path('auth/', include('app_auth.urls')),
    path('users/', include('app_users.urls')),
    path('courses/', include('app_courses.urls')),
]


