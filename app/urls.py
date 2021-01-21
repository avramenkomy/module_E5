from django.contrib import admin
from django.urls import path, include
from app.views import NewsList

app_name = 'app'

urlpatterns = [
    path('', NewsList.as_view(), name='news-list'),
]