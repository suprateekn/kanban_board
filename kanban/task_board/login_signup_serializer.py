from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import CharField, EmailField

from task_board.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    gender_display = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['gender', 'profile_pic', 'gender_display']


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()
    email = EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'user_profile']

    def create(self, validated_data):
        print(validated_data)
        profile_data = validated_data.pop('user_profile')
        user = User(first_name=validated_data['first_name'], last_name=validated_data['last_name'],
                    username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        user.user_profile.profile_pic = profile_data['profile_pic']
        user.user_profile.gender = profile_data['gender']
        user.user_profile.save()
        return user

    def validate_email(self, attr):
        check_user = User.objects.filter(email=attr)
        if check_user.exists():
            raise ValidationError("A user with that email id already exists.")
        return attr

class UserLoginSerializer(serializers.ModelSerializer):
    username = CharField(required=False, allow_blank=True)
    email = EmailField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]

        if not email and not username:
            raise ValidationError("A username or email is required to login")

        user = User.objects.filter(Q(email=email) | Q(username=username)).distinct()

        if user.exists() and user.count() == 1:
            user = user.first()
        else:
            raise ValidationError("Invalid  username/email.")

        if user:
            if not user.check_password(password):
                raise ValidationError("Invalid Password.")

        return user
