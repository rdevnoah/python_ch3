"""python_ch3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from helloworld import views as helloworld_views
from emaillist import views as emaillist_views

urlpatterns = [
    path('helloworld/counter/update', helloworld_views.counter_update),
    path('helloworld/counter/add', helloworld_views.counter_add),
    path('helloworld/counter/max', helloworld_views.counter_max),

    path('emaillist/add', emaillist_views.add),
    path('emaillist/form/', emaillist_views.form),
    path('emaillist/', emaillist_views.index),
    path('helloworld/', helloworld_views.hello),
    path('admin/', admin.site.urls),
]
