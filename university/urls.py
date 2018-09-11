from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('my_univer/', views.first_html_page, name="first_html_page"),
    path('add_student/', views.AddStudent.as_view(), name="add_student"),
    path('add_teacher/', views.AddTeacher.as_view(), name="add_teacher"),
    # path('add_class/', views.add_class, name="add_class")
]
