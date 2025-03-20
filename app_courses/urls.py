from django.urls import path
from .views import CourseListCreateView, CourseDetailView, GroupListCreateView, GroupDetailView
from .views import teacher_groups
urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('groups/', GroupListCreateView.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('teacher/groups/', teacher_groups, name='teacher-groups'),
]
