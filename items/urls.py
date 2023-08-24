from django.urls import path
from . import views
from django.urls import path,include
app_name='item'

urlpatterns=[
    path('<int:pk>/',views.detail,name='detail'),
]