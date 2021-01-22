from django.urls import path, include
from cars import views
from cars.views import CarDetailView


app_name = "cars"

urlpatterns = [
    path('', views.index),
    path('car/<int:pk>', CarDetailView.as_view(), name="car-detail"),
]