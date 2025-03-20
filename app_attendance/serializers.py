from rest_framework import serializers
from .models import Attendance, Grade
from app_users.serializers import StudentSerializer
from app_courses.serializers import CourseSerializer

class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'student', 'course', 'date', 'is_present']

class GradeSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Grade
        fields = ['id', 'student', 'course', 'score', 'date']
