# _*_ coding:utf-8_*_
"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

"""
param1：匹配的url请求格式
param2：对应的View中的方法
param3：url映射的名称
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'MySiteMain.views.index', name='index'),
    url(r'^cal/', 'MySiteMain.views.cal', name='cal'),
    url(r'^add2/(\d+)/(\d+)/$', 'MySiteMain.views.add2', name='add2'),
    url(r'^$', 'MySiteMain.views.getblogs', name='blog_get_blogs'),
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]


