from django.urls import path
from contact_us import views

urlpatterns = [
    path('', views.message_send, name='contact_us')
]