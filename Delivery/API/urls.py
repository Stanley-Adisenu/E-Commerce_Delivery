from django.urls import path,include
from . import views

urlpatterns = [
    path('deliver/',views.deliveries),
    path('update/<int:pk>/',views.update_delivery),
]