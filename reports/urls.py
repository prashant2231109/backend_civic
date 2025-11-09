from django.urls import path
from . import views

urlpatterns = [
    path('api/reports/', views.create_report, name='create_report'),
    path('api/reports/list/', views.get_reports, name='get_reports'),
]
