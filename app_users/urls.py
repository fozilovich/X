from django.urls import path
from .views import CreateTeacherView, CreateStudentView, UserListView, UserDetailView

urlpatterns = [
    path('teachers/create/', CreateTeacherView.as_view(), name='create_teacher'),
    path('students/create/', CreateStudentView.as_view(), name='create_student'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]
