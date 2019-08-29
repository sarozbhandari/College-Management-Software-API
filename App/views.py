from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentManagement, CourseManagement, SessionCourseManagement, GradeManagement, DeadLine, CourseEnrollment, SessionManagement as ss, OfferedCourses as a
from .serializer import *
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import json
from django.core.serializers.json import DjangoJSONEncoder

#Student Management Operations
class StudentView(APIView):

    def get(self, request):
        student = StudentManagement.objects.all()
        serializer = StudentManagementSerializer(student, many = True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = StudentManagementSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

        else:
            return  Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class StudentManage(APIView):

    def get(self, request, university_id):
        student = StudentManagement.objects.get(university_id = university_id)
        serializer = StudentManagementSerializer(student)
        return Response({'Students': serializer.data})
        

    def put(self, request, university_id, format =None):
        student = StudentManagement.objects.get(university_id = university_id)
        serializer = StudentManagementSerializer(student, data = request.data)

        if serializer.is_valid(raise_exception = True):
            UpdateStudent = serializer.save()

        return Response({"Student '{}' is updated Successfully" .format(UpdateStudent.university_id)})


    def delete(self, request, university_id):
        student = StudentManagement.objects.get(university_id = university_id)
        student.delete()
        return Response("Student deleted Successfully")


class CourseView(APIView):

    def get(self, request):
        course = CourseManagement.objects.all()
        serializer = CourseManagementSerializer(course, many = True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CourseManagementSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

        else:
            return  Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CourseManage(APIView):

    def get(self, request, course_code):
        course = CourseManagement.objects.get(course_code = course_code)
        serializer = CourseManagementSerializer(course)
        return Response({'Courses': serializer.data})



    def put(self, request, course_code, format =None):
        course = CourseManagement.objects.get(course_code = course_code)
        serializer = CourseManagementSerializer(course, data = request.data)

        if serializer.is_valid(raise_exception = True):
            UpdateCourse = serializer.save()

        return Response({"Course '{}'' is updated Successfully" .format(UpdateCourse.course_code)})


    def delete(self, request, course_code):
        course = CourseManagement.objects.get(course_code = course_code)
        course.delete()
        return Response("Course deleted Successfully")



#Offered Courses 
class OfferedCourses():
    def get(self, request):
        session = a.objects.all()
        serializer = OfferedCoursesSerializer(session, many = True)
        return Response(serializer.data)

    def get(self, request, course_code):
        try:
            session = a.objects.get(course_code = course_code)
            if course:
                response = {
                'session': session.offered_session
                }
                return Response(response)
        except a.DoestNotExist:
            return Response('Course Not Found')

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = OfferedCoursesSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, course_id):
        course = a.objects.get(course_id = course_id)
        serializer = OfferedCoursesSerializer(course, many = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, course_id):
        course = a.objects.get(course_id= course_id)
        course.delete()


# #Session Search 
# def sess(request):
#     if request.POST:
#         name = request.POST['sess']

#         offsess = a.objects.filter(offered_session = name)
#         course_code = []
#         course_name = []
#         credit = []

#         for i in offsess:
#             course_code.append(i.course_code.course_code)
#             course_name.append(i.course_code.course_name)
#             credit.append(i.course_code.credit)

#         course_dict = {
#             'course_code': course_code,
#             'course_name': course_name,
#             'credit': credit,
#         }
#         return render(request, 'App/insert.html', course_dict)

#     else:
#         return render(request, 'App/insert.html')


class StudentProfile(APIView):

    def get(self, request, university_id):
        student = StudentManagement.objects.get(university_id = university_id)
        serializer = StudentManagementSerializer(student)
        return Response({'Students Details': serializer.data})


class SessionManagement(APIView):
    def get(self, request):
        session = ss.objects.all()

        sessioncourse = SessionCourseManagement.objects.filter(session_name = session[0].session_name)
        # print(sessioncourse.course_code)
        courselist = []
        for i in sessioncourse:

            course = CourseManagement.objects.get(course_code=i.course_code.course_code)
            # print(course)

            data_dict = {
                'course_code':course.course_code,
                'course_name':course.course_name,
                'credit':course.credit,
                'session_name':session[0].session_name,
                'max_credit': session[0].max_credit
            }        
            courselist.append(data_dict)
        return Response(courselist)

    def post(self, request, *args, **kwargs):
        # course_code = request.data['coursecode']
        # print("........course code yo hoooooooo")
        # print(course_code)
        # print('course code yo vitra xa')
        # course_name = request.data['coursename']
        # print(course_name)
        # course_credit = request.data['credit']
        session_name = request.data['sessionname']
        print(session_name)
        checkbox = request.data.get('checkbox')
        print(checkbox)
        max_credit = request.data['maxcredit']
        print(max_credit)
        total_credit = 0

        for i in checkbox:
            course = CourseManagement.objects.get(course_code = i)
            if course.prerequisite:
                try:
                    grade = GradeManagement.objects.get(course_code=course.course_code)
                    if grade.status == 'Pass':
                        total_credit = total_credit + course.credit
                        session_credit = ss.objects.get(session_name = session_name)
                        if total_credit <= session_credit.max_credit:
                            enroll = CourseEnrollment.objects.create(university_id_id = 10017, course_code_id = course.course_code)
                            # print('enrolleddddddd')
                except GradeManagement.DoesNotExist:
                    total_credit = total_credit + course.credit
                    session_credit = ss.objects.get(session_name = session_name)
                    if total_credit <= session_credit.max_credit:
                        enroll = CourseEnrollment.objects.create(university_id_id = 10017, course_code_id = course.course_code)
            else:
                try:
                    grade = GradeManagement.objects.get(course_code=course.course_code)
                    if grade.status == 'Pass':
                        total_credit = total_credit + course.credit
                        session_credit = ss.objects.get(session_name = session_name)
                        if total_credit <= session_credit.max_credit:
                            enroll = CourseEnrollment.objects.create(university_id_id = 10017, course_code_id = course.course_code)

                except GradeManagement.DoesNotExist:
                    total_credit = total_credit + course.credit
                    session_credit = ss.objects.get(session_name = session_name)
                    if total_credit <= session_credit.max_credit:
                        enroll = CourseEnrollment.objects.create(university_id_id = 10017, course_code_id = course.course_code)


class GradeManagementView(APIView):
    def get(self, request, university_id):
        try:
            stud = StudentManagement.objects.get(university_id=university_id)
            student = CourseEnrollment.objects.filter(university_id = stud.university_id)
            # serializer = CourseEnrollmentSerializer(student)
            # return Response(serializer.data)
            # print(student)
            student_id = []
            for i in student:
                dictionary={
                    'student_id':i.university_id,
                    'course_code':i.course_code
                }
                student_id.append(dictionary)
                return Response(student_id)
        except CourseEnrollment.DoesNotExist:
            return Response("Grade Not found")



#Grade Management Functionalities
class GradeManagement(APIView):
    def get(self, request):
        try: 
            student = StudentManagement.objects.all()
            studentID = []

            for i in student:
                studentID.append(i.university_id)

            studentgrade = []
            for j in studentID:
                course = CourseEnrollment.objects.filter(university_id = j)

                data_dict = {
                    'university_id': course.university_id,
                    'course_code': course.course_code
                }
                studentgrade.append(data_dict)
                return Response(studentgrade)
        except:
            return Response("Details Not Found!!!")



        def post(self, request, *args, **kwargs):
            data = request.data
            serializer = GradeManagementSerializer(data= data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


        def put(self, request, course_code):
            student = GradeManagement.objects.get(university_id = university_id)
            serializer = GradeManagementSerializer(Student, many = True)

            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


        def delete(self, request, course_code):
            course = GradeManagement.objects.get(course_code = course_code)
            dl = course.delete()
            return Response("Course deleted from the user")
