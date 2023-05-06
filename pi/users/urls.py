from django.urls import path
from . import views

urlpatterns = [
    #path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
    path('users/create/', views.user_create),
    path('users/update/<int:pk>/', views.user_update),
    path('users/delete/<int:pk>/', views.user_delete),
    path('users/get', views.user_list),
    path('users/login', views.login_view)
  #  path('',views.user_list)
]
