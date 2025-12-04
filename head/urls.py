"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include    
from django.shortcuts import redirect
# from vege import views
# from home import views
# from accounts import views
from web_test import views
from django.conf.urls.static import static
from django .conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('home/', views.home , name="home"),
    # path('about/', views.about , name="about"),

    # path('product/', views.add_product , name="add_product"),
    # path('product_list/', views.product_list , name="product_list"),
    # path("products/delete/<uuid:uid>/", views.delete_product, name="delete_product"),
    # path("products/update/<uuid:uid>/", views.update_product, name="update_product"),
#start recipe project
    # path('reciepes/', views.reciepes , name="reciepes"),
    # path('delete_recipe/<id>/', views.delete_recipe , name="delete_recipe"),
    # path('update_recipe/<id>/', views.update_recipe , name="update_recipe"),
    
    # path('homepage', views.homepage, name='homepage'),
    # path('login/', views.login_page , name="login"),
    # path('logout/', views.log_out , name="logout"),
    # path('register/', views.Registar, name="register"),


    # path('student/', views.get_student, name="get_student"),
    # path('see_marks/<student_id>/', views.see_marks, name="see_marks"),

#end recipe project

    # path('page/' , views.sucess_page , name="secess_page"),

    # path('form', views.fake , name="fake"),

    # test project
  
    path('homepage', views.homepage, name='homepage'),
    path('login/', views.login_page , name="login"),
    path('logout/', views.log_out , name="logout"),
    path('register/', views.Registar, name="register"),

 
    path('admin/', admin.site.urls),
    # path('', include('web_test.urls')),  # app name updated

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()