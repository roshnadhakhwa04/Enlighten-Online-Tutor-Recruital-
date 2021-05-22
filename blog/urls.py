from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('teacher_sign',views.teacher_sign,name='teacher_sign'),
    path('student_sign',views.student_sign,name='student_sign')
]