from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    gender_display = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['gender', 'profile_pic', 'gender_display']


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'user_profile']

    def create(self, validated_data):
        print(validated_data)
        profile_data = validated_data.pop('user_profile')
        user = User(first_name=validated_data['first_name'], last_name=validated_data['last_name'],
                    username=validated_data['username'], password=validated_data['password'],
                    email=validated_data['email'])
        user.save()
        user.user_profile.profile_pic = profile_data['profile_pic']
        user.user_profile.gender = profile_data['gender']
        user.user_profile.save()
        return user
