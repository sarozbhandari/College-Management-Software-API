from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from App import views


urlpatterns = [
	path('course/', views.CourseView.as_view()),
    path('course/<int:course_code>', views.CourseManage.as_view()),
    path('student/', views.StudentView.as_view()),
    path('student/<int:university_id>', views.StudentManage.as_view()),
    #path('deadline/', views.DeadLineView.as_view()),  
    #path('insert/', views.sess, name = 'Session'), 
    #path('registercourse/', views.CourseRegister.as_view()),
    # path('registercourse', views.CourseRegister, name = 'courseregister'),
    path('sessions', views.SessionManagement.as_view()),
    path('grademanage/', views.GradeManagement.as_view()),
    path('studentgrade/<int:university_id>', views.GradeManagementView.as_view())


]






