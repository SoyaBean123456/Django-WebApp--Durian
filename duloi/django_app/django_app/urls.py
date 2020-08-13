"""django_app URL Configuration

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
from django.urls import path
from duriann.views import index
#from errora.views import errora
#from errorb.views import errorb
#from errorc.views import errorc
#from charts.views import charts
#from layoutside.views import layoutsidenavlight
#from layoutstatic.views import layoutstatic
#from login.views import login
#from password.views import password
#from register.views import register
#from tables.views import tables


urlpatterns = [
    path('admin/', admin.site.urls),
    path('duriann/', index),
    #path('errora/', errora),
    #path('errorb/', errorb),
    #path('errorc/', errorc),
    #path('charts/', charts),
    #path('layoutside/', layoutsidenavlight),
    #path('layoutstatic/', layoutstatic),
    #path('login/', login),
    #path('password/', password),
    #path('register/', register),
    #path('tables/', tables)

    
]
