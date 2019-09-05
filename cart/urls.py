'''
Created on 3 Sep 2019

@author: benjaminsenyonyi
'''
# import sys
# sys.path.append("..")

from django.urls import path
from django.conf.urls import url
from . import views #here
# from .views import cart_add, cart_detail, cart_remove





app_name = 'cart'

urlpatterns = [
#     url('', views.cart_detail, name='cart_detail'),
#     url('add/<int:product_id>/', views.cart_add, name = 'cart_add'),
#     url('remove/<int:product_id>/', views.cart_remove, name = 'cart_remove'),
    #     url(r'^admin/', admin.site.urls),

    path('', views.cart_detail, name = 'cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name = 'cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name = 'cart_remove'),

#     path('', views.product_list, name  = 'product_list'),
#     path('<slug:category_slug>/', views.product_list, name= 'product_list_by_category'),
#     path('<int:id>/<slug:slug>/', views.product_detail, name = 'product_detail'),
    
#     path('', cart_detail, name = 'cart_detail'),
#     path('add/<int:product_id>/', cart_add, name = 'cart_add'),
#     path('remove/<int:product_id>/', cart_remove, name = 'cart_remove'),
#     
    ]


