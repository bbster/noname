from django.urls import path

from some_api import views

urlpatterns = [
    path('', views.SomeList.as_view()),
]
