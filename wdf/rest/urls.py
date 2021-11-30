from django.urls import path
from .views import LogsViews

urlpatterns = [
    path('create', LogsViews.as_view())
]