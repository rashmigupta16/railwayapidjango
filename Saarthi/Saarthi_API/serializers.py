from rest_framework import serializers
from .models import User, ChatHistory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id','first_name', 'last_name', 'email_id')


    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatHistory
        fields=('user_id','msg','reply')
        # fields = '__all__'
