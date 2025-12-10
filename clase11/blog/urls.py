from django.urls import path
from . import views

urlpatterns = [
    path('post', views.mostrar_post, name="post"),
    path('comments', views.mostrar_comments, name="comments")
]
    
    
    