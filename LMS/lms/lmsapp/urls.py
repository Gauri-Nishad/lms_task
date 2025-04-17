from .views import *
from django.urls import path
urlpatterns = [
    path('signup',signup,name="signup"),
    path('',home,name='home'),
    path('admin_logout',admin_logout,name="admin_logout"),
    path('student_logout',student_logout,name="student_logout"),
    path('admin_login',admin_login,name="admin_login"),
    path('student_login',student_login,name="student_login"),
    path('admin_dashboard',admin_dashboard,name="admin_dashboard"),
    path('student_dashboard',student_dashboard,name="student_dashboard"),
 
    path('add_student',add_student,name='add_student'),
    path('update_student/<int:id>',update_student,name='update_student'),
    path('get_student/<int:id>',get_student,name='get_student'),
    path('student_list',student_list,name='student_list'),
    path('delete_student/<int:id>',delete_student,name='delete_student'), 

    path('add_book',add_book,name='add_book'),
    path('update_book/<int:id>',update_book,name='update_book'),
    path('get_book/<int:id>',get_book,name='get_book'),
    path('book_list',book_list,name='book_list'),
    path('delete_book/<int:id>',delete_book,name='delete_book'),


   

    
]
