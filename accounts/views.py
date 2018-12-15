import json

from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from knox.views import LoginView, LogoutView
from rest_framework.permissions import AllowAny
from . import serializers
from django.contrib.auth.models import User
from hacko.settings import STATIC_ROOT
import csv
import matplotlib.pyplot as plt
from . import models
from rest_framework.generics import CreateAPIView
# Create your views here.


# User LoginView
class UserLoginView(LoginView):
    http_method_names = ['post']
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        s = serializers.LoginSerializer(data=self.request.data)
        s.is_valid(raise_exception=True)
        username_or_email = s.validated_data.get('user', None)
        password = s.validated_data.get('password', None)
        try:
            validate_email(username_or_email)
            username = User.objects.filter(email=username_or_email)
            if username.exists():
                user = authenticate(username=username[0].username, password=password)
        except ValidationError:
            user = authenticate(username=username_or_email, password=password)

        if user is None:
            return Response({'message': 'No user found as per given credentials', 'error': 1},
                            status=status.HTTP_400_BAD_REQUEST)
        if user.is_active is False:
            return Response({'message': 'Please wait till the admin confirms your account', 'error': 1},
                            status=status.HTTP_202_ACCEPTED)
        login(request, user)
        context = super(UserLoginView, self).post(request, format=None)
        context.data['error'] = 0
        return context


# Logout View
class UserLogoutView(LogoutView):
    http_method_names = ['post']

    def post(self, request, format=None):
        super(UserLogoutView, self).post(request, format=None)
        return Response({'message': 'successfully logged out!', 'error': 0})


#'date_received
# 'product'
# 'sub_product'
# 'issue'
# 'sub_issue'
# 'consumer_complaint_narrative'
# 'company_public_response'
# 'company'
# 'state'
# 'zipcode'
# 'tags'
# 'consumer_consent_provided'
# 'submitted_via'
# 'date_sent_to_company'
# 'company_response_to_consumer'
# 'timely_response'
# 'consumer_disputed?'
# 'complaint_id'