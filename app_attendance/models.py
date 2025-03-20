from django.db import models
from app_users.models import Student
from app_courses.models import Course

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField(auto_now_add=True)
    is_present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name} - {'Bor' if self.is_present else 'Yo‘q'}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    score = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name} - {self.score}"
