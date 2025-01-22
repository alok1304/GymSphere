from . import views
from django.urls import path


urlpatterns = [
    path('', views.home,name='home'),
    path('faq/', views.faq,name='faq'),
    path('gallery/', views.gallery,name='gallery'),
    path('enquiry/', views.enquiry,name='enquiry'),
    path('pricing/', views.pricing,name='pricing'),
    path('privacy/', views.privacy,name='privacy'),
    path('terms/', views.terms,name='terms'),
        path('register/', views.register,name='register'),
]