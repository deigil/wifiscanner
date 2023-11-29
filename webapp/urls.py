# webapp/urls.py

from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('db/', views.db_view, name='db_view'),
    path('frontendAPI/', views.WifiDataCreateView.as_view()),
    # Add other URL patterns as needed
]