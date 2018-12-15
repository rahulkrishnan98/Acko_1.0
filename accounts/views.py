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
   
def ProductComplaintView(request):
    filename = STATIC_ROOT + '/accounts/csv/consumer_complaints.csv'
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        products=[]
        for row in reader:
            products.append(row[1])
        plot1={}
        for product in products:
            if(product in plot1):
                plot1[product]+=1
            else:
                plot1[product]=1
        json1 = json.dumps(plot1)
        json2 = json.loads(json1)
        plt.bar(range(len(plot1)), list(plot1.values()), align='center')
        plt.xticks(range(len(plot1)), list(plot1.keys()),fontsize=7, rotation=30)
        plt.title('Complaint count over Registered products')
        plt.savefig("1.Product_Count.png")
        return JsonResponse({'message': json2})


def SubProductComplaint(request):
    product = 'Mortgage'
    filename = STATIC_ROOT + '/accounts/csv/consumer_complaints.csv'
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        sub_products = {}
        for row in reader:
            if row[1] == product:
                if row[2] in sub_products:
                    sub_products[row[2]] += 1
                else:
                    sub_products[row[2]] = 1
        json_values = json.loads(json.dumps(sub_products))
        plt.bar(range(len(sub_products)), list(sub_products.values()), align='center')
        plt.xticks(range(len(sub_products)), list(sub_products.keys()), fontsize=7, rotation=30)
        plt.title('Complaint count over Registered Sub_products for %s' %(product))
        plt.savefig("Sub_Product_Count.png")
        return JsonResponse(json_values)

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
