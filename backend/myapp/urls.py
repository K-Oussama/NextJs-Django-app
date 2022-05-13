from django.urls import path
from . import views

app_name= "myapp"

urlpatterns = [
    path("api/", views.PostListView.as_view(), name="myapp_home"),
    path("api/category/", views.CategoryListView.as_view(), name="categories"),
    path("api/post/<slug:slug>/", views.Post.as_view(), name="post"),
    path("api/category/<slug:slug>/", views.CategoryItemView.as_view(), name="category_item"),
]