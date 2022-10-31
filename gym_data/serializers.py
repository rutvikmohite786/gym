from rest_framework import serializers
from gym_data.models import SliderHome
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderHome
        fields = ('id',
                  'title',
                  'desc',
                  'img_path')

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password','email')
        extra_kwargs = {'password': {'write_only': True},'email':{'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['password'],validated_data['email'])
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email')
