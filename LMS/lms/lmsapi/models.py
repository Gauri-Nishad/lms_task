# models.py

from django.db import models
from django.contrib.auth.hashers import make_password

class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roll_number=models.IntegerField()
    std_div=models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    added_by=models.ForeignKey(Admin, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

class AdminToken(models.Model):
    admin=models.ForeignKey(Admin, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=500, unique=True)
    is_active = models.BooleanField(default=True)

class StudentToken(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=500, unique=True)
    is_active = models.BooleanField(default=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE,default=1)
    is_active = models.BooleanField(default=True)