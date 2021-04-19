"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView
from . import views

urlpatterns = [

    path('',views.index,name='index'),

    path('test/create/<int:pk_recruit>', views.TestCreate.as_view(), name='test-create'),
    path('test/result',TemplateView.as_view(template_name='test_result.html'), name='test-result'),

    path('sith/all',views.SithListView.as_view(),name='sith-list'),
    path('sith/<int:pk>',views.SithDetailView.as_view(),name='sith-detail'),
    path('sith/<int:pk>/notice',TemplateView.as_view(template_name='sith_notice.html'), name='sith-notice'),

    path('recruit/all',views.RecruitListView.as_view(),name='recruit-list'),
    path('recruit/<int:pk>', views.RecruitDetailView.as_view(), name='recruit-detail'),
    path('recruit/create', views.RecruitCreate.as_view(), name='recruit-create'),

    path('hands/<int:pk_sith>/<int:pk_recruit>', views.hands, name='hands'),

    ]
