from django.shortcuts import render,redirect
import requests
from django.contrib import messages
from .decorators import admin_required
# Create your views here.

login_url="http://127.0.0.1:8000/api/admin_login"
student_login_url="http://127.0.0.1:8000/api/student_login"

admin_logout_url="http://127.0.0.1:8000/api/admin_logout"
student_logout_url="http://127.0.0.1:8000/api/student_logout"
signup_url="http://127.0.0.1:8000/api/admin_signup"

add_student_url="http://127.0.0.1:8000/api/add_student"
update_student_url="http://127.0.0.1:8000/api/update_student"
get_student_url="http://127.0.0.1:8000/api/get_student"
get_studentlist_url="http://127.0.0.1:8000/api/get_studentlist"
delete_student_url="http://127.0.0.1:8000/api/delete_student"


add_book_url="http://127.0.0.1:8000/api/add_book"
update_book_url="http://127.0.0.1:8000/api/update_book"
get_book_url="http://127.0.0.1:8000/api/get_book"
get_booklist_url="http://127.0.0.1:8000/api/get_booklist"
delete_book_url="http://127.0.0.1:8000/api/delete_book"


def signup(request):
    data=request.POST.copy()
    if request.method == 'POST':
        
        signup_request= requests.post(signup_url,data=data)
        print('signup_request',signup_request)
       
        signup_response=signup_request.json()
        print('signup_response',signup_response)
      
        if signup_response['n'] == 1:
          
           
            messages.success(request,signup_response['msg'])
            return redirect("app:admin_login")  
        
        else:
            messages.error(request,signup_response['msg'])
            return redirect("app:signup")
        
    return render(request,'signup.html')

def home(request):
    user_role = request.session.get('user_role')
    print("Logged-in user role:", user_role)
    return render(request,'home.html')

@admin_required
def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def student_dashboard(request):
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))
    get_booklist_request=requests.get(get_booklist_url)
    print("get_booklist_request",get_booklist_request)
    get_booklist_response=get_booklist_request.json()
    print("get_booklist_response",get_booklist_response)
    return render(request,'student_dashboard.html',{"books":get_booklist_response})

def admin_login(request):
    data=request.POST.copy()
    if request.method == 'POST':
    
        login_request= requests.post(login_url,data=data)
        login_response=login_request.json()
      
        if login_response['n'] == 1:
            request.session['user_role'] = 'admin'
            request.session['admin_email']= login_response['data']['email']
            request.session['admin_id']= login_response['data']['id']
            request.session['admin_name']= login_response['data']['name']
            request.session['access_token']= login_response['accesstoken']
            print("Admin Login =>", login_response['data']['name'], login_response['data']['id'])
    
            messages.success(request,login_response['msg'])
            return redirect("app:admin_dashboard")  
        
        else:
            messages.error(request,login_response['msg'])
            return redirect("app:admin_login")
        
  
    return render(request,'admin_login.html')

def admin_logout(request):
  
    data={}
    data['access_token'] = request.session.get('access_token')
    access_token = request.session.get('access_token')
    print("ADMIN TOKEN",access_token)
    if not access_token:
        messages.error(request, "No active session found.")
        return redirect('app:home')

    data = {'access_token': access_token}
    
    log_out_request=requests.post(admin_logout_url,data=data)
    print('log_out_request',log_out_request)
    log_out_response=log_out_request.json()   
    print('log_out__rspons',log_out_response)
    if log_out_response['n']==1:
        messages.success(request,log_out_response['msg'])
        request.session.flush()
        return redirect('app:home')
    return redirect('app:home')



def student_login(request):
    data=request.POST.copy()
    if request.method == 'POST':
    
        login_request= requests.post(student_login_url,data=data)
        login_response=login_request.json()
      
        if login_response['n'] == 1:
            request.session['user_role'] = 'student'
            request.session['student_email']= login_response['data']['email']
            request.session['student_id']= login_response['data']['id']
            request.session['student_name']= login_response['data']['name']
            request.session['access_token']= login_response['accesstoken']
            print("Student Login =>", login_response['data']['name'], login_response['data']['id'])
            messages.success(request,login_response['msg'])
            return redirect("app:home")  
        
        else:
            messages.error(request,login_response['msg'])
            return redirect("app:student_login")

  
    return render(request,'student_login.html')


def student_logout(request):
  
    data={}
    data['access_token'] = request.session.get('access_token')
    access_token = request.session.get('access_token')
    print("aaaaaaaaaaa",access_token)
    if not access_token:
        messages.error(request, "No active session found.")
        return redirect('app:home')

    data = {'access_token': access_token}
    
    log_out_request=requests.post(student_logout_url,data=data)
    print('log_out_request',log_out_request)
    log_out_response=log_out_request.json()   
    print('rspons...',log_out_response)
    if log_out_response['n']==1:
        messages.success(request,log_out_response['msg'])
        request.session.flush()
        return redirect('app:student_login')
    return redirect('app:student_login')

@admin_required
def add_book(request):
    data=request.POST.copy()
    
    if request.method=="POST":
        add_book_request=requests.post(add_book_url,data=data)
        print("add_book_request",add_book_request)
        add_book_response=add_book_request.json()
        print("add_book_response",add_book_response)
        
        if add_book_response['n']==1:
            messages.success(request,add_book_response['msg'])
            return redirect("app:book_list")
        else:
            messages.error(request,add_book_response['msg'])
            return redirect("app:book_list")
    
    return render(request,'add_book.html')

@admin_required
def update_book(request,id):
    data=request.POST.copy()
    data['id']=id
    get_book_request=requests.get(get_book_url,data=data)
    print("get_book_request",get_book_request)
    get_book_response=get_book_request.json()
    print("get_user_response",get_book_response)
    if request.method=="POST":
        update_book_request=requests.post(update_book_url,data=data)
        print("update_book_request",update_book_request)
        update_book_response=update_book_request.json()
        print("update_book_response",update_book_response)
        
        if update_book_response['n']==1:
            messages.success(request,update_book_response['msg'])
            return redirect("app:admin_dashboard")
        else:
            messages.error(request,update_book_response['msg'])
            return redirect("app:admin_dashboard")
    return render(request,'update_book.html',{'book':get_book_response})


@admin_required
def get_book(request,id):
    data=request.POST.copy()
    data['id']=id
    get_book_request=requests.get(get_book_url,data=data)
    print("get_book_request",get_book_request)
    get_book_response=get_book_request.json()
    print("get_user_response",get_book_response)
    
    return render(request, 'get_book.html',{"book":get_book_response})



def book_list(request):

    
    get_booklist_request=requests.get(get_booklist_url)
    print("get_booklist_request",get_booklist_request)
    get_booklist_response=get_booklist_request.json()
    print("get_booklist_response",get_booklist_response)
    
    return render(request, 'book_list.html',{"books":get_booklist_response})

@admin_required
def delete_book(request,id):
    data={}
    data['id']=id
    delete_book_request=requests.post(delete_book_url,data=data)
    delete_book_response=delete_book_request.json()
    if delete_book_response['msg']==1:
        messages.success(request,delete_book_response['msg'])
        return redirect("app:book_list")
    else:
        messages.error(request,delete_book_response['msg'])
        return redirect("app:book_list")
   

@admin_required
def add_student(request):
    data=request.POST.copy()
    
    if request.method=="POST":
        add_student_request=requests.post(add_student_url,data=data)
        print("add_student_request",add_student_request)
        add_student_response=add_student_request.json()
        print("add_student_response",add_student_response)
        
        if add_student_response['n']==1:
            messages.success(request,add_student_response['msg'])
            return redirect("app:student_list")
        else:
            messages.error(request,add_student_response['msg'])
            return redirect("app:student_list")
    
    return render(request,'add_student.html')


@admin_required
def update_student(request,id):
    data=request.POST.copy()
    data['id']=id
    get_student_request=requests.get(get_student_url, data=data)
    print("get_student_request",get_student_request)
    get_student_response=get_student_request.json()
    print("get_student_response",get_student_response)
    if request.method=="POST":
        update_student_request=requests.post(update_student_url,data=data)
        print("update_student_request",update_student_request)
        update_student_response=update_student_request.json()
        print("update_student_response",update_student_response)
        
        if update_student_response['n']==1:
            messages.success(request,update_student_response['msg'])
            return redirect("app:student_list")
        else:
            messages.error(request,update_student_response['msg'])
            return redirect("app:student_list")
    return render(request,'update_student.html',{'student':get_student_response})

@admin_required
def get_student(request,id):
    data=request.POST.copy()
    data['id']=id
    get_student_request=requests.get(get_student_url,data=data)
    print("get_student_request",get_student_request)
    get_student_response=get_student_request.json()
    print("get_user_response",get_student_response)
    
    return render(request, 'get_student.html',{"student":get_student_response})


@admin_required
def student_list(request):
    get_studentlist_request=requests.get(get_studentlist_url)
    print("get_studentlist_request",get_studentlist_request)
    get_studentlist_response=get_studentlist_request.json()
    print("get_studentlist_response",get_studentlist_response)
    
    return render(request, 'student_list.html',{"students":get_studentlist_response})

@admin_required
def delete_student(request,id):
    data={}
    data['id']=id
    delete_student_request=requests.post(delete_student_url,data=data)
    delete_student_response=delete_student_request.json()
    if delete_student_response['msg']==1:
        messages.success(request,delete_student_response['msg'])
        return redirect("app:student_list")
    else:
        messages.error(request,delete_student_response['msg'])
        return redirect("app:student_list")
   