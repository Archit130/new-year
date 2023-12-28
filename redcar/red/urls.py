from django.urls import path
from red import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('SaveImage/', views.SaveImageview, name="SaveImage"),

]
