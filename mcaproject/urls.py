"""mcaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based viewss sa
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projectapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.menu),
    path("about",views.ABOUT),
    path("links",views.links),
    path("donate",views.donate),
    


    path("home",views.home),
    path("parent",views.parent),


    path("insert",views.insert),
    path("save",views.save),
    path("show",views.show ,name='show'),
    path('edit/<int:id>',views.edit),
    path('update',views.update,name='update'),
    path('delete/<int:id>',views.delete),


    path('childreg',views.childreg),
    path('childsave',views.childsave),
    path('childshow',views.childshow,name='childshow'),
    path('childedit/<int:id>',views.childedit ,name='childedit'),
    path('updatechild',views.updatechild,name='updatechild'),
    path('childdelete/<int:id>',views.childdelete),

    path('login',views.signin,name='login'),
    path('loggin',views.loggin,),
    path('logout',views.loggout),
    path('mapdetails',views.abcd),
    path("details",views.details),
    path("data/<int:id>",views.data),
]
