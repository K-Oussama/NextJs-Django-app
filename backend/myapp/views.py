from rest_framework import generics
from django.shortcuts import render

from . import models
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer

# Create your views here.
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class Post(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(level=1)
    serializer_class = CategorySerializer

class CategoryItemView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return models.Post.objects.filter(
            category__in=Category.objects.get(slug=self.kwargs["slug"]).get_descendants(include_self=True)
        )




