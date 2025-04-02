from . import views
from django.urls import path
from .views import workout_view


urlpatterns = [
    path('', views.home,name='home'),
    path('faq/', views.faq,name='faq'),
    path('gallery/', views.gallery,name='gallery'),
    path('enquiry/', views.enquiry,name='enquiry'),
    path('pricing/', views.pricing,name='pricing'),
    path('privacy/', views.privacy,name='privacy'),
    path('terms/', views.terms,name='terms'),
    path('bmi/', views.bmi,name='bmi'),
    path('register/', views.register,name='register'),
    path('checkout/<int:plan_id>', views.checkout,name='checkout'),
    path('checkout_session/<int:plan_id>', views.checkout_session,name='checkout_session'),
    path('success/', views.success,name='success'),
    path('cancel/', views.cancel,name='cancel'),
    path('workout/', workout_view, name='workout'),
]