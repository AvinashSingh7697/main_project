from django.http.response import HttpResponse
from .models import Customer, Todo
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
# from django.http import HttpResponse
# Create your views here.


def index(request):

   context  = {"page" : "home"}
   return render(request,"index.html",context)


def about(request):
   page  = {"page" : "about"}
   return render (request, "about.html", page) 

def todo(request):
   if request.method == "POST" :
        todo = request.POST.get("todo")
        if todo is not None:

          todo_obj = Todo(todo_name = todo)
          todo_obj.save()
          return redirect("/todo")
   todos =  Todo.objects.all()  

   context = {"todos": todos}
   return render(request, "todo.html", context)


def todo_del(request , id):

   try:
      todo = Todo.objects.get(id = id)
      todo.delete()
   except Todo.DoesNotExist:
      pass
   return redirect("/todo/")


def mark_comp(request , id):

   try:
      todo = Todo.objects.get(id = id)
      todo.is_completed = True 
      todo.save()
   except Todo.DoesNotExist:
      pass
   return redirect("/todo/")

def logiin(request):
   if request.method== "GET":
      return render(request, "logiin.html",{})
   if request.method == "POST":
      email = request.POST.get("email") 
      password = request.POST.get("password") 
      user = User.objects.filter(email = email).first()
      if user is None: 
         return redirect('/login')

      user = authenticate(request, user = user,password = password)
      print(request.session.user)
      return redirect('/todo')

def logout_view(request):
   print(request.session)
   logout(request)
   print(request.session)
   return HttpResponse("logout successfully")
   

def registreation(request):
   print(dict(request.POST))
   if request.method == "POST":
      email = request.POST.get("email") 
      password = request.POST.get("password") 
      user = User(username = email, password = password, superuser =False)  
      user.set_password(password)
      user.save()

   return render(request,"registreation.html" )
   
