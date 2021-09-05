from django.urls import path
from appFour import views

app_name = 'app'
urlpatterns = [
    path(r'other', views.other, name ='other'),
    path(r'help', views.help, name='help'),

    
]