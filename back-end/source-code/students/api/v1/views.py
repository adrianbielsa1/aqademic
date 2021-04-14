from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ...models import StudentModel
from ...serializers import StudentSerializer


class StudentsByNamesAPIView(APIView):
    def get(self, request, expectedNames, *args, **kwargs):
        """
        Returns a list of students matching the specified names.
        """
        expectedNames = expectedNames.split("-")

        # First get all of the students from the database.
        students = StudentModel.objects.all()

        # Now get students that have the names we've been requested.
        for currentExpectedName in expectedNames:
            students = students.filter(names__icontains=currentExpectedName)

        # Serialize the results.
        serializer = StudentSerializer(students, many = True)

        return Response(serializer.data, status = status.HTTP_200_OK)

class StudentsByFileAPIView(APIView):
    def get(self, request, expectedFile, *args, **kwargs):
        """
        Returns a list of students matching the specified file. There should
        be at most one student with said file.
        """
        try:
            # Find the student in the database.
            student = StudentModel.objects.get(file = expectedFile)
        except StudentModel.DoesNotExist:
            return Response(
                { "error": "No student found with file: " + str(expectedFile) },
                status = status.HTTP_400_BAD_REQUEST
            )
        else:
            # Serialize the student.
            serializer = StudentSerializer(student)

            return Response(serializer.data, status = status.HTTP_200_OK)
