from rest_framework import serializers
from .models import Tasks
from accounts.models import User



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['title','date_added','reminder_time','number_repeat']

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(read_only =True)
    username = serializers.CharField(max_length = 200)

    class Meta:
        model = User
        fields = ['username','email','password']


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    # def validate_email(self, value):
    #     if User.objects.filter(email=value).exists():
    #         raise serializers.ValidationError(
    #             {'detail':"Email already exists"}
    #         )
    #     return value
    # def validate_username(self, value):
    #     if User.objects.filter(username = value).exists():
    #         raise serializers.ValidationError(
    #             {'detail':'User with current username already exists'}
    #         )
    #     return value
    