from . import views
from django.urls import path

urlpatterns = [
  path('',views.light_view, name="light_view"),
  ]
