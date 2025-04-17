from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
import re
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.

@api_view(['POST'])
def admin_signup(request):
    data=request.data.copy()
    email=data.get('email')
    name=data.get('name')
    pasword=data.get('password')
    data['is_active']=True
    if not name:
        return Response({'msg': 'enter an name.','n':0})
    if not email:
        return Response({'msg': 'enter an email.','n':0})
    if not pasword:
        return Response({'msg': 'enter password.','n':0})
    
    existing_email=Admin.objects.filter(email=email).exclude(id=request.data.get('id')).first()
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email) :
        return Response({'msg': 'Incorrect email id','n':0})
    if existing_email !=None:
        return Response({'msg':'email is already in use.Use Different email','n':0})
    data['password']=make_password(data['password'])
    serializer = AdminSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data":serializer.data,"msg":"Thank you for signing up!",'n':1})
    return Response({"errors":serializer.errors,"msg":"something went wrong",'n':0})



@api_view(['POST'])
def admin_login(request):
    data=request.data.copy()
    email = data.get('email')
    print("username;;;;", email )
    password=data.get('password')
    print("password;;;;",password)
    if not email:
        return Response({ 'msg': 'Please enter the email!','n':0})
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email) :
        return Response({'msg': 'Invalid email','n':0})
    if not password:
        return Response({ 'msg': 'Please enter the password!','n':0})

    admin=Admin.objects.filter(email=email, is_active=True).first()
    print("./",admin)
    if not admin:
        return Response({'msg': 'Admin not found, please try again later', 'n': 0})
    if not check_password(password, admin.password):
        return Response({'msg': 'Invalid username or password', 'n': 0})
     
    refresh_token = RefreshToken.for_user(admin)
    access_token = refresh_token.access_token

    admin_token = AdminToken(admin=admin, access_token=access_token)
    admin_token.save()
 
    serializer = AdminSerializer(admin)

    return Response({
        'msg': 'Logged in successfully',
        'accesstoken': str(access_token),
        'data': serializer.data,
        'n': 1
    })
    



@api_view(['POST'])
def student_login(request):
    data=request.data.copy()
    email = data.get('email')
    print("email", email )
    password=data.get('password')
    print("passw",password)
   
    if not email:
        return Response({ 'msg': 'Please enter the email','n':0})
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email) :
        return Response({'msg': 'Invalid email','n':0})
    if not password:
        return Response({ 'msg': 'Please enter the password'})

    student=Student.objects.filter(email=email, is_active=True).first()
   
    print("user",email)
 
    if email :
    
        serializer = StudentSerializer(student)
        print("dnknfnm",serializer.data)
        refresh_token=RefreshToken.for_user(student)
        access_token=refresh_token.access_token
        student_token=StudentToken(student=student,access_token=access_token)
        student_token.save()
        if not check_password(password, student.password):
            return Response({'msg': 'Invalid username or password'})

    
        return Response({'msg': 'Logged in successfully','accesstoken':str(access_token),'data': serializer.data,'n': 1})
    else:
        return Response({'msg': 'User not found,Please try again letter','n': 0,})
    



@api_view(['POST'])
def admin_logout(request):
   
    token = request.data.get('access_token')
    print("Received token:", token)
    
   
    admin_token = AdminToken.objects.filter(access_token=token, is_active=True).first()
    print("admin token:", admin_token)
    
    if admin_token:
        admin_token.is_active = False
        admin_token.save()
        return Response({"msg": "Logged out successfully.", "n": 1})
    else:
        return Response({"msg": "Already logged out.", "n": 0})
    

@api_view(['POST'])
def student_logout(request):
   
    token = request.data.get('access_token')
    print("Received token:", token)
    
   
    student_token = StudentToken.objects.filter(access_token=token, is_active=True).first()
    print("admin token:", student_token)
    
    if student_token:
        student_token.is_active = False
        student_token.save()
        return Response({"msg": "Logged out successfully.", "n": 1})
    else:
        return Response({"msg": "Already logged out.", "n": 0})


@api_view(['POST'])
def add_book(request):
    data=request.data.copy()
    data['is_active']=True
    title=data.get('title')
    author=data.get('author')
    isbn=data.get('isbn')
    published_date=data.get('published_date')
    category=data.get('category')
    admin=data.get('admin')
   
    if not title:
       return Response({'msg': 'enter title','n':0})
    if not author:
       return Response({'msg': 'enter author','n':0})
    if not isbn:
       return Response({'msg': 'enter isbn number','n':0})
    regex = r'978(?:-?\d){10}'
    if not re.match(regex, isbn) :
        return Response({'msg': 'Invalid ISBN','n':0})
    if not  published_date:
       return Response({'msg': 'enter  published_date','n':0})
    if not category:
       return Response({'msg': 'enter category','n':0})
    if not admin:
       return Response({'msg': 'enter admin id','n':0})
    serializer=BookSerializer(data=data)
    if serializer.is_valid():
       serializer.save()
       return Response({"data":serializer.data,"msg":"book is added",'n':1})
    return Response({"error":serializer.errors,"msg":"something went wrong",'n':0})



@api_view(['POST'])
def update_book(request):
    data=request.data.copy()
    title=data.get('title')
    author=data.get('author')
    isbn=data.get('isbn')
    published_date=data.get('published_date')
    category=data.get('category')
    admin=data.get('admin')
    id=data.get('id')
    obj=Book.objects.get(id=id)
    data['is_active']=True
    if not title:
       return Response({'msg': 'enter title','n':0})
    if not author:
       return Response({'msg': 'enter author','n':0})
    if not isbn:
       return Response({'msg': 'enter isbn number','n':0})
    regex = r'978(?:-?\d){10}'
    if not re.match(regex, isbn) :
        return Response({'msg': 'Invalid ISBN','n':0})
    if not  published_date:
       return Response({'msg': 'enter  published_date','n':0})
    if not category:
       return Response({'msg': 'enter category','n':0})
    
    serializer=BookSerializer(obj,data,partial=True)
    if serializer.is_valid():
       serializer.save()
       return Response({'data':serializer.data,'msg':'updated','n':1})
    return Response({"error":serializer.errors,'msg':'something went wrong','n':0})

@api_view(['GET'])
def get_book(request):
    data=request.data
    id=data.get('id')
    obj=Book.objects.filter(id=id).first()
    print(obj)
    serializer=BookSerializer(obj)
    return Response(serializer.data) 

@api_view(['GET'])
def get_booklist(request):
   
    objs=Book.objects.filter(is_active=True).all()
    serializer=BookSerializer(objs,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def delete_book(request):
    data=request.data
    id=data.get('id')
    obj=Book.objects.filter(id=id,is_active=True).first()
    print("obj",obj)
    if obj:
        obj.is_active=False
        obj.save()  
        return Response({"msg":"book deleted","n":1}) 
    else:
        return Response({"msg":"now book is not available","n":1})





@api_view(['POST'])
def add_student(request):
    data=request.data.copy()
    data['is_active']=True
    name=data.get('name')
    roll_number=data.get('roll_number')
    std_div=data.get('std_div')
    email=data.get('email')
    password=data.get('password')
    data['password']=make_password(data['password'])
   
    if not name:
       return Response({'msg': 'enter your name','n':0})
    if not roll_number:
       return Response({'msg': 'enter your roll number','n':0})
    if not std_div:
       return Response({'msg': 'enter your Division','n':0})
    if not email:
       return Response({'msg': 'enter author','n':0})
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email) :
        return Response({'msg': 'Invalid email','n':0})
    existing_email=Student.objects.filter(email=email).exclude(id=request.data.get('id')).first()
    if existing_email !=None:
        return Response({'msg':'email is already in use','n':0})
    if not password:
       return Response({'msg': 'enter password','n':0})
   
  
    serializer=StudentSerializer(data=data)
    if serializer.is_valid():
       serializer.save()
       return Response({"data":serializer.data,"msg":"student is added",'n':1})
    return Response({"error":serializer.errors,"msg":"something went wrong",'n':0})



@api_view(['POST'])
def update_student(request):
    data=request.data.copy()
    id=data.get('id')
    obj=Student.objects.get(id=id)
    name=data.get('name')
    roll_number=data.get('roll_number')
    std_div=data.get('std_div')
    email=data.get('email')
    password=data.get('password')
    data['password']=make_password(data['password'])
   
    if not name:
       return Response({'msg': 'enter your name','n':0})
    if not roll_number:
       return Response({'msg': 'enter your roll number','n':0})
    if not std_div:
       return Response({'msg': 'enter your Division','n':0})
    if not email:
       return Response({'msg': 'enter author','n':0})
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email) :
        return Response({'msg': 'Invalid email','n':0})
    existing_email=Student.objects.filter(email=email).exclude(id=request.data.get('id')).first()
    if existing_email !=None:
        return Response({'msg':'email is already in use','n':0})
    existing_roll_number=Student.objects.filter(roll_number=roll_number).exclude(id=request.data.get('id')).first()
    if existing_roll_number !=None:
        return Response({'msg':'roll number is already in use','n':0})
    if not password:
       return Response({'msg': 'enter password','n':0})
   
  
    serializer=StudentSerializer(obj,data,partial=True)
    if serializer.is_valid():
       serializer.save()
       return Response({'data':serializer.data,"msg":"student is updated",'n':1})
    return Response({"error":serializer.errors,"msg":"something went wrong",'n':0})

    

@api_view(['GET'])
def get_student(request):
    data=request.data
    id=data.get('id')
    obj=Student.objects.filter(id=id).first()
    print(obj)
    serializer=StudentSerializer(obj)
    return Response(serializer.data) 

@api_view(['GET'])
def get_studentlist(request):
   
    objs=Student.objects.filter(is_active=True).all()
    serializer=StudentSerializer(objs,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def delete_student(request):
    data=request.data
    id=data.get('id')
    obj=Student.objects.filter(id=id,is_active=True).first()

    obj.is_active=False
    obj.save()  
    
    return Response({"msg":"student deleted","n":1}) 