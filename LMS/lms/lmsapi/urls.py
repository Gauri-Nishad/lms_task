from .views import *
from django.urls import path
urlpatterns = [
    #Loging and LOGOUT of adminand studENT
    path('admin_signup',admin_signup),
    path('admin_login',admin_login),
    path('admin_logout',admin_logout),
    path('student_logout',student_logout),
    path('student_login',student_login),
    
    #BOOK API
    path('add_book',add_book),
    path('update_book',update_book),
    path('get_book',get_book),
    path('get_booklist',get_booklist),
    path('delete_book',delete_book),
  
    #Students API
    path('add_student',add_student),
    path('update_student',update_student),
    path('get_student',get_student),
    path('get_studentlist',get_studentlist),
    path('delete_student',delete_student),
    
]
    
