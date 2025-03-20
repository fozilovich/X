from django.urls import path
from .views import (
    UserStatisticsView, UserDetailStatisticsView, CourseStatisticsView, GroupStatisticsView,
    GroupAttendanceStatisticsView, TopStudentsView, MostAbsentStudentsView, AttendanceStatisticsView,
    StudentAttendanceView, GradesStatisticsView, PaymentsStatisticsView, DebtorsView
)

urlpatterns = [
    path('users/', UserStatisticsView.as_view(), name='user-statistics'),
    path('users/<int:id>/', UserDetailStatisticsView.as_view(), name='user-detail-statistics'),

    path('courses/', CourseStatisticsView.as_view(), name='course-statistics'),
    path('groups/', GroupStatisticsView.as_view(), name='group-statistics'),
    path('groups/<int:id>/attendance/', GroupAttendanceStatisticsView.as_view(), name='group-attendance'),

    path('students/top/', TopStudentsView.as_view(), name='top-students'),
    path('students/attendance/', MostAbsentStudentsView.as_view(), name='most-absent-students'),

    path('attendance/', AttendanceStatisticsView.as_view(), name='attendance-statistics'),
    path('attendance/<int:id>/', StudentAttendanceView.as_view(), name='student-attendance'),

    path('grades/', GradesStatisticsView.as_view(), name='grades-statistics'),

    path('payments/', PaymentsStatisticsView.as_view(), name='payments-statistics'),
    path('payments/debtors/', DebtorsView.as_view(), name='debtors-list'),
]
