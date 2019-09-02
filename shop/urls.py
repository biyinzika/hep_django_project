'''
Created on 2 Sep 2019

@author: benjaminsenyonyi
'''

from django.urls import path
from . import views

app_name = 'shop'

urlpatters = [
    path('', views.product_list, name  = 'product_list'),
    path('<slug:category_slug>/', views.product_list, name= 'product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name = 'product_detail'),
    ]