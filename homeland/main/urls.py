from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.create_contact, name='create_contact'),
    path('tour/<slug:slug>/', views.TourDetail.as_view(), name='detail')
]
