from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Simple serializer that list all comments API with all fields
    """

    class Meta:
        model = Comment
        fields = '__all__'
