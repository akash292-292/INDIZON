from django.urls import path,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from items import urls
from .forms import LoginForm
urlpatterns=[
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('admin/', admin.site.urls),
    path('items/',include('items.urls')),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

