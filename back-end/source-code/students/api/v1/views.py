from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ...models import StudentModel
from ...serializers import StudentSerializer

"""
Creates a new student.
"""
@api_view(["POST"])
def create(request):
    # Create a new student from the request's data.
    # TODO: Does this update existing students?
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        # The student was created correctly - save it to the database,
        # and notify the other end of the request's completion.
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        # Failed to create the student :-(
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
Returns a list of students matching the specified names.
"""
@api_view(["GET"])
def read_by_names(request, expected_names):
    # Get all students from the database.
    students = StudentModel.objects.all()
    
    # Filter the students whose name does not contain the current expected
    # name. Then, do it again - shrinking the list of students at each
    # iteration. In the end we get only those students whose name contains
    # ALL of the expected names.
    for current_expected_name in expected_names.split("-"):
        students = students.filter(names__icontains=current_expected_name)

    # Serialize the results and send them back.
    serializer = StudentSerializer(students, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

"""
Returns a list of students matching the specified file. Unless there's
something wrong with the database (two students with the same file), the
list should contain a single value.
"""
@api_view(["GET"])
def read_by_file(request, expected_file):
    # Find the students whose file matches.
    students = StudentModel.objects.all().filter(file = expected_file)
    
    # Serialize the results and send them back.
    serializer = StudentSerializer(students, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)
