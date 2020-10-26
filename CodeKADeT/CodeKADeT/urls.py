"""CodeKADeT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login import views as login_views
from file_upload import views as file_upload_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', login_views.signup,name="signup"),
    path('fileupload/logout/',file_upload_views.logout_user,name="logout"),
    path('login/',  login_views.login),
    path('fileupload/', file_upload_views.upload_from_computer,name="upload"),
    path('', include('login.urls')),
    path('signup/login/',  login_views.login),
    path('fileupload/file_view/', file_upload_views.view_function, name='view_function')
]
