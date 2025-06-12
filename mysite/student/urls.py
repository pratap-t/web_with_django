from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.viewStudentList, name='viewStudentList'),
    # path(r'^(?P<student_id>\d+)/$', views.viewStudentDetails, name='viewStudentDetails'),
    path('<int:student_id>/', views.viewStudentDetails, name='student_details'),
]
