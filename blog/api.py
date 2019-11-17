from rest_framework import serializers, viewsets
from .models import PersonalBlog

class PersonalBlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalBlog
        fields = ('title', 'content', 'category')
    
    #adding the author field
    def create(self, validated_data):
        author = self.context['request'].user
        blog = PersonalBlog.objects.create(author=author, **validated_data)
        return blog

class PersonalBlogViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalBlogSerializer
    queryset = PersonalBlog.objects.all()