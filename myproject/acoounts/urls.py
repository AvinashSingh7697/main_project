from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("todo/", views.todo, name= "todo"),
    path("todo_del/<id>", views.todo_del, name="todo_del"),
    path("mark_comp/<id>", views.mark_comp, name="mark_comp"),
    path("login", views.logiin, name="logiin"),
    path("register", views.registreation, name="register"),
    path("logout", views.logout_view),

]

