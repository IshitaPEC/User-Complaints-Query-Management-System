from rest_framework import serializers
from myportfolio.models import Message
from django.contrib.auth.models import User


class ToUserSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()

    def get_text(self, obj):
        return obj.username

    class Meta:
        model = User
        fields = ('id', 'username', 'text')