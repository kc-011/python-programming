from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer

@api_view(['GET'])
def students(request):
    stds = Student.objects.all()

    serializer = StudentSerializer(stds, many=True)

    return Response(serializer.data)


