from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index), 
    path('destroy/', views.destroy), 
    path('post/', views.post), 
    path('post/delete/<int:id>/', views.deletePost), 
    path('post/comment/<int:id>/', views.commentPost), 

] 
