from django.urls import path
from . import views
urlpatterns = [
    path('product_list', views.product_list, name='product_list'),
]