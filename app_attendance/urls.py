from django.urls import path
from .views import (
    AttendanceListCreateView, AttendanceDetailView, StudentAttendanceView,
    StudentAttendanceList, GradeListCreateView, GradeDetailView, StudentGradesView
)

urlpatterns = [
    # Attendance (Davomat)
    path('', AttendanceListCreateView.as_view(), name='attendance-list-create'),
    path('<int:pk>/', AttendanceDetailView.as_view(), name='attendance-detail'),
    path('student/<int:id>/', StudentAttendanceView.as_view(), name='student-attendance'),
    path('student/my/', StudentAttendanceList.as_view(), name='my-attendance'),


    # Grades (Baholar)
    path('grades/', GradeListCreateView.as_view(), name='grade-list-create'),
    path('grades/<int:pk>/', GradeDetailView.as_view(), name='grade-detail'),
    path('grades/student/<int:id>/', StudentGradesView.as_view(), name='student-grades'),
]
