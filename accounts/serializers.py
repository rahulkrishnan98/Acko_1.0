from django.contrib.auth.models import User
from rest_framework import serializers


class LoginSerializer(serializers.ModelSerializer):
    user = serializers.CharField()

    class Meta:
        model = User
        fields = ('pk', 'user', 'password',)
        read_only_fields = ('pk',)