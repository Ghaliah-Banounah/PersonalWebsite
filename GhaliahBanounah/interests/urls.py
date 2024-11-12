from django.urls import path
from . import views

app_name = "interests"

urlpatterns = [
    path('add/', views.addInterestView, name='addInterestView'),
    path('display/', views.displayInterestsView, name='displayInterestsView')
]