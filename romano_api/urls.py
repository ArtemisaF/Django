from django.urls import path
from romano_api import views

urlpatterns =[
    path('romano-view/', views.RomanoApiView.as_view()),
]