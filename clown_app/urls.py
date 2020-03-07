from django.urls import path
from .views import Home, AddPost, ShowPost, EditPost, DeletePost

urlpatterns = [
    path('', Home.as_view(), name="clown_home"),
    path('addPost/', AddPost.as_view(), name="add_post"),
    path('post/<slug>', ShowPost.as_view(), name="show_post"),
    path('post/edit/<slug>', EditPost.as_view(), name="edit_post"),
    path('post/delete/<slug>', DeletePost.as_view(), name="delete_post"),

]