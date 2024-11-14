from django.urls import path
from . import views

app_name = "interests"

urlpatterns = [
    path('display/', views.displayInterestsView, name='displayInterestsView'),
    path('details/<int:interId>', views.interestDetailsView, name='interestDetailsView')
]