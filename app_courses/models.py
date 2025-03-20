from django.db import models
from app_users.models import Teacher, Student

class Course(models.Model):
    name = models.CharField(max_length=255, default="Default Course Name")
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='groups')
    students = models.ManyToManyField(Student, blank=True, related_name='groups')

    def __str__(self):
        return f"{self.name} ({self.course.name})"
