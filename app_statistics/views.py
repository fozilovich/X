from django.db.models import Count, Avg, Sum
from rest_framework.response import Response
from rest_framework.views import APIView
from app_users.models import User, Student, Teacher
from app_courses.models import Course, Group
from app_attendance.models import Attendance, Grade
from app_payments.models import Payment

# 1. Foydalanuvchi statistikasi
class UserStatisticsView(APIView):
    def get(self, request):
        data = {
            "total_users": User.objects.count(),
            "admins": User.objects.filter(is_superuser=True).count(),
            "teachers": Teacher.objects.count(),
            "students": Student.objects.count(),
        }
        return Response(data)

class UserDetailStatisticsView(APIView):
    def get(self, request, id):
        user = User.objects.get(id=id)
        data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "is_superuser": user.is_superuser,
            "date_joined": user.date_joined
        }
        return Response(data)

# 2. Kurs va guruh statistikasi
class CourseStatisticsView(APIView):
    def get(self, request):
        courses = Course.objects.annotate(student_count=Count("groups__students"))
        data = [{"name": course.name, "students": course.student_count} for course in courses]
        return Response(data)

class GroupStatisticsView(APIView):
    def get(self, request):
        total_groups = Group.objects.count()
        active_groups = Group.objects.filter(is_active=True).count()
        canceled_groups = total_groups - active_groups

        data = {
            "total_groups": total_groups,
            "active_groups": active_groups,
            "canceled_groups": canceled_groups
        }
        return Response(data)

class GroupAttendanceStatisticsView(APIView):
    def get(self, request, id):
        avg_attendance = Attendance.objects.filter(course_id=id).aggregate(avg_attendance=Avg("is_present"))
        return Response({"average_attendance": avg_attendance["avg_attendance"]})

# 3. Talabalar statistikasi
class TopStudentsView(APIView):
    def get(self, request):
        top_students = Student.objects.annotate(avg_score=Avg("grades__score")).order_by("-avg_score")[:10]
        data = [{"username": student.user.username, "avg_score": student.avg_score} for student in top_students]
        return Response(data)

class MostAbsentStudentsView(APIView):
    def get(self, request):
        absent_students = Student.objects.annotate(absences=Count("attendances", filter=Attendance.objects.filter(is_present=False))).order_by("-absences")[:10]
        data = [{"username": student.user.username, "absences": student.absences} for student in absent_students]
        return Response(data)

# 4. Davomat va baho statistikasi
class AttendanceStatisticsView(APIView):
    def get(self, request):
        avg_attendance = Attendance.objects.aggregate(average=Avg("is_present"))
        return Response({"average_attendance": avg_attendance["average"]})

class StudentAttendanceView(APIView):
    def get(self, request, id):
        avg_attendance = Attendance.objects.filter(student_id=id).aggregate(average=Avg("is_present"))
        return Response({"student_average_attendance": avg_attendance["average"]})

class GradesStatisticsView(APIView):
    def get(self, request):
        avg_grade = Grade.objects.aggregate(average=Avg("score"))
        return Response({"average_grade": avg_grade["average"]})

# 5. To‘lov statistikasi
class PaymentsStatisticsView(APIView):
    def get(self, request):
        total_income = Payment.objects.aggregate(total=Sum("amount"))
        return Response({"total_income": total_income["total"]})

class DebtorsView(APIView):
    def get(self, request):
        debtors = Student.objects.filter(payments__isnull=True)  # To‘lov qilmagan talabalar
        data = [{"username": student.user.username} for student in debtors]
        return Response(data)
