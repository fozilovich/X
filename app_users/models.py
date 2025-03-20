from django.contrib.auth.models import User
from django.db import models

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    experience = models.IntegerField()

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    grade = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
