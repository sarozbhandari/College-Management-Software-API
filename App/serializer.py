from rest_framework import serializers
from .models import StudentManagement, CourseManagement, SessionCourseManagement, OfferedCourses, OfferedCourses, SessionManagement, DeadLine


#Student Management Serializer
class StudentManagementSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentManagement
        fields = '__all__'

#Course Management Serializer
class CourseManagementSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseManagement
        fields = '__all__'

#OfferedCourse Serializer
class OfferedCoursesSerializer(serializers.ModelSerializer):
	class Meta:
		model = OfferedCourses
		fields = '__all__'

#Session Management
class SessionManagementSerializer(serializers.ModelSerializer):
	class Meta:
		model = SessionManagement
		fields = '__all__'

#Session Course Management
class SessionCourseManagementSerializer(serializers.ModelSerializer):
	class Meta:
		model = SessionCourseManagement
		fields = ('course_name', 'course_code', 'course_credit')


class AcademicSerializer(serializers.ModelSerializer):
	class Meta:
		model = 'Academic'
		fields = '__all__'


class EnrollManagementSerializer(serializers.ModelSerializer):
	class Meta:
		model = 'CourseEnrollment'
		fields = ('full_name', 'university_id')