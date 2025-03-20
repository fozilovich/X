from rest_framework import generics
from .models import Course, Group
from .serializers import CourseSerializer, GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET'])
def teacher_groups(request):
    teacher = request.user.teacher  # Hozirgi foydalanuvchini teacher sifatida olish
    groups = Group.objects.filter(teacher=teacher)  # Faqat ushbu teacher guruhlarini olish
    serializer = GroupSerializer(groups, many=True)  # Seriyalizatsiya qilish
    return Response(serializer.data)  # JSON javob qaytarish





