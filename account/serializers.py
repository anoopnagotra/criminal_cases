from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=False)

    class Meta:
        model = models.Profile
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data.pop('user')
        new_user = User.objects.create_user(**user)
        profile = models.Profile.objects.create(user=new_user, **validated_data)
        return profile