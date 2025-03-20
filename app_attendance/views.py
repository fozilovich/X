from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Attendance, Grade
from .serializers import AttendanceSerializer, GradeSerializer

# --- Attendance (Davomat) API ---
class AttendanceListCreateView(generics.ListCreateAPIView):
    """Barcha davomatlarni olish va yangi davomat qo‘shish"""
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

class AttendanceDetailView(generics.RetrieveAPIView):
    """Bitta davomat tafsilotlarini olish"""
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

class StudentAttendanceView(generics.ListAPIView):
    """Berilgan student ID bo‘yicha davomatni olish"""
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student_id = self.kwargs['id']
        return Attendance.objects.filter(student_id=student_id)

class StudentAttendanceList(generics.ListAPIView):
    """Hozirgi tizimga kirgan student o‘zining davomat ro‘yxatini ko‘radi"""
    serializer_class = AttendanceSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not hasattr(user, 'student'):
            raise PermissionDenied("Siz student emassiz yoki tizimga kirmagansiz.")
        return Attendance.objects.filter(student=user.student)


# --- Grades (Baholar) API ---
class GradeListCreateView(generics.ListCreateAPIView):
    """Barcha baholarni olish va yangi baho qo‘shish"""
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]

class GradeDetailView(generics.RetrieveUpdateAPIView):
    """Bitta bahoni ko‘rish va o‘zgartirish"""
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]

class StudentGradesView(generics.ListAPIView):
    """Berilgan student ID bo‘yicha baholarni olish"""
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student_id = self.kwargs['id']
        return Grade.objects.filter(student_id=student_id)


def get_queryset(self):
    user = self.request.user

    # Foydalanuvchi tizimga kirmagan bo‘lsa, xatolik chiqaramiz
    if user.is_anonymous:
        raise PermissionDenied("Siz tizimga kirmagansiz.")

    # Foydalanuvchi student emasligini tekshiramiz
    if not hasattr(user, 'student'):
        raise PermissionDenied("Siz student emassiz.")

    return Attendance.objects.filter(student=user.student)

