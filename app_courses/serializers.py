from rest_framework import serializers
from .models import Course, Group
from app_users.serializers import TeacherSerializer, StudentSerializer

class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'teacher']

class GroupSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'course', 'students']
