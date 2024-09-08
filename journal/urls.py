from django.urls import path
from journal import views

urlpatterns = [
    path("", views.index, name='index'),
    path("signup", views.signup, name='signup'),
    path("login", views.login, name='login'),
    path("home", views.home, name='home'),
    # path("about", views.about, name='about'),
]
