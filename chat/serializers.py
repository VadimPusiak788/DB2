from rest_framework import serializers
from .models import ChatModel
from rest_framework.validators import UniqueValidator


class CreatePostSerializers(serializers.ModelSerializer):
    author_email = serializers.EmailField(
        validators=[UniqueValidator(queryset=ChatModel.objects.all())],
    )

    class Meta:
        model = ChatModel
        fields = ('author_email', 'text')


class ListPostSerializers(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d%H:%M:%S",  read_only=True)
    update_date = serializers.DateTimeField(format="%Y-%m-%d%H:%M:%S",  read_only=True)

    class Meta:
        model = ChatModel
        fields = ('author_email', 'text', 'create_date', 'update_date')

