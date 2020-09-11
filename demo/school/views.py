from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


# Create your views here.
class StudentList(APIView):

    def get(self, request):
        e = Student.objects.all()
        serializer = StudentSerializer(e, many=True)
        return Response(serializer.data)
