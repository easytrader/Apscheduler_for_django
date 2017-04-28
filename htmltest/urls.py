"""htmltest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from trips.views import hello_world,test1,test2,test3,aps_del

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test1/', test1),
    url(r'^test2/', test2),
    url(r'^test3/', test3),
    url(r'^aps/del/', aps_del),
    url(r'^$', hello_world),
]
