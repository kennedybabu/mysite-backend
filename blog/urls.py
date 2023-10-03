from django.urls import path
from .import views 

app_name = 'blog'

urlpatterns = [
    path('users/', views.getAllUsers, name='get_users'),
    path('users/<str:id>/', views.getUser, name='get_user'),
    path('', views.post_list, name='post_list'),
    path('create/', views.create_post, name="create_post"),
    path('comments/create/', views.create_comment, name="create_comment"),
    path('posts/<str:id>/delete/', views.delete_post, name="delete_post"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]