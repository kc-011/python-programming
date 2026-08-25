from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializer import StudentSerializer

@api_view(['GET', 'POST'])
def students(request):

    if request.method == 'GET':
        stds = Student.objects.all()

        serializer = StudentSerializer(stds, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def studentdetail(request, rolno):

    try:
        student = Student.objects.get(rolno=rolno)
    except Student.DoesNotExist:
        return Response({'message':'Student Not Found'}, status=404)

    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    if request.method == 'DELETE':
        student.delete()
        return Response({'message':'Student deleted successfully'})

@api_view(['GET'])
def searchstudents(request):
    query = request.GET.get('query')
    students = Student.objects.filter(name__icontains=query)
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

class StudentsAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class StudentDetailAPIView(APIView):
    def get_object(self, rolno):
        try:
            return Student.objects.get(rolno=rolno)
        except Student.DoesNotExist:
            return None

    def get(self, request, rolno):
        student= self.get_object(rolno)

        if student is None:
            return Response({'message': 'Student Not Found'},status=404)

        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, rolno):
        student= self.get_object(rolno)

        if student is None:
            return Response({'message': 'Student Not Found'},status=404)

        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, rolno):
        student = self.get_object(rolno)

        if student is None:
            return Response({'message': 'Student Not Found'},status=404)

        student.delete()
        return Response({'message': 'Student Deleted Successfully'})
