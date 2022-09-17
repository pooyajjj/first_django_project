from dataclasses import field
from datetime import timezone
from rest_framework import serializers
from blog.models import Article


# class BlogSerializers(serializers.serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length = 200)
#     slug = serializers.SlugField(max_length = 100, unique = True)
#     description = serializers.TextField()
#     thumbnail = serializers.ImageField(upload_to = 'images')
#     publish = serializers.DateField(default = timezone.now)
#     created = serializers.DateField(auto_now_add = True)
#     created = serializers.DateField(auto_now = True)

class BlogModelSerializers(serializers.ModelSerializers):
    class Meta:
        model = Article
        fields = '__all__'