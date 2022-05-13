from rest_framework import serializers

from .models import Category, Post, PostImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ["image", "alt_text"]



class PostSerializer(serializers.ModelSerializer):
    post_image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "category", "title", "content", "slug", "author", "post_image"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]
