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
Removes one or more students that match the specified file number.
"""
@api_view(["DELETE"])
def delete_by_file(request):
    # Get file number.
    # TODO: Wrap in a `try` statement.
    file = request.data

    # Find the students whose file matches and remove them.
    students = StudentModel.objects.all().filter(file = file).delete()
    students_count = students[0]

    if students_count > 0:
        # Students deleted successfully.
        return Response(students_count, status=status.HTTP_200_OK)
    else:
        # No students found with the given file number.
        # TODO: Maybe this response should be returned if the request's data
        # is ill-formed, instead of returning it when no students were found.
        return Response(students_count, status=status.HTTP_400_BAD_REQUEST)

"""
Updates a given student, finding it through its file number.
TODO: Check if there are more than one entries with the same file number?
TODO: Consider unifying this function with `create()`, maybe by using Django's
`update_or_create()` method.
"""
@api_view(["PUT"])
def update_by_file(request, file):
    # Find the student.
    student = StudentModel.objects.get(file = file)

    # Update each field.
    # TODO: Check if fields exist.
    for key, value in request.data.items():
        setattr(student, key, value)

    # Save new values in the database.
    student.save()

    # TODO: Return another response if the student couldn't be found.
    return Response(None, status=status.HTTP_200_OK)

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
