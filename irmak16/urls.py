"""irmak16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from tekne import views
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('logout', views.logoutUser, name='logout'),
    path('permission_not_granted/', TemplateView.as_view(template_name='Forbidden.html'),name="permission_not_granted"),
    path('login', views.login, name='login'),
    path('', views.rzv, name='rezerve'),
    path('irmak', views.irmak, name='irmak'),
    path('filter', views.filter, name='filter'),
    path('rezerveedit/<int:id>', views.rezerveedit, name='rezerveedit'),
    path('kaan', views.kaan, name='kaan'),
    path('filter1', views.filter1, name='filter1'),
    path('rezerveedit1/<int:id>', views.rezerveedit1, name='rezerveedit1'),
    path('mkpills24', views.mkpills24, name='mkpills24'),
    path('mkpills25', views.mkpills25, name='mkpills25'),
    path('mkpills26', views.mkpills26, name='mkpills26'),

]

