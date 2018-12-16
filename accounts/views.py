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
def firstbitthird(response):
    sub_product='Second mortgage'
    filename = STATIC_ROOT + '/accounts/csv/consumer_complaints.csv'
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        companies={}
        for row in reader:
            if(row[2]==sub_product):
                if(row[7] in companies):
                    companies[row[7]]+=1
                else:
                    companies[row[7]]=1
        print(companies)
def CompanyDispute(request):
    filename = STATIC_ROOT + '/accounts/csv/consumer_complaints.csv'
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        company=[]
        dispute=[]
        for row in reader:
            company.append(row[7])
            dispute.append(row[16])
        disputes={}
        for i in range(len(company)):
            disputes[company[i]]=0
        for i in range(len(company)):
            if(dispute[i]=='Yes'):
                disputes[company[i]]+=1
        sorted_disputes=sorted(disputes.values())
        max_disputes=sorted_disputes[-10:]
        min_disputes=sorted_disputes[30:50]
        final_dis={}
        print(max_disputes)
        print(min_disputes)
        for i in disputes:
            if(disputes[i] in max_disputes and len(final_dis)<20 and disputes[i]!=0 ):
                final_dis[i]=disputes[i]
            if(disputes[i] in min_disputes and len(final_dis)<20 and disputes[i]!=0):
                final_dis[i]=disputes[i]

        json_values = json.loads(json.dumps(final_dis))
        labels = final_dis.keys()
        sizes = final_dis.values()
        # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.savefig("DisComp.png")
        return JsonResponse(json_values)

def Demographic(response):
    company='Capital One'
    filename = STATIC_ROOT + '/accounts/csv/consumer_complaints.csv'
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        product=[]
        dispute=[]
        for row in reader:
            if(row[7]==company):
                product.append(row[1])
                dispute.append(row[16])
        sum1={}
        for i in range(len(dispute)):
            if(dispute[i]=='Yes'):
                dispute[i]=0
            else:
                dispute[i]=1
        for i in range(len(product)):
            if(product[i] in sum1):
                sum1[product[i]]+=dispute[i]
            else:
                sum1[product[i]]=dispute[i]
        sorted1=sorted(sum1.values())
        print(sorted1)
        add1=0
        note=[]
        for i in sum1:
            if(sum1[i]<sorted1[-3]):
                add1+=sum1[i]
                note.append(i)

        for i in note:
            sum1.pop(i, None)
        sum1['others']=add1
        json_values = json.loads(json.dumps(sum1))
        labels = sum1.keys()
        sizes = sum1.values()
        # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.savefig("DisComp_prod_comp.png")
        return JsonResponse(json_values)
    
def progressive_analysis(request):
    filename = STATIC_ROOT + '/accounts/csv/consumer_complaints.csv'
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        date=[]
        company=[]
        for row in reader:
            date.append(row[0])
            company.append(row[7])
        #correct years format from date
        dates=[]
        for dates1 in date:
            dates1=list(dates1)
            dates1=dates1[6:]
            dates1="".join(dates1)
            dates.append(dates1)
        company2012={}
        company2013={}
        company2014={}
        company2015={}
        print(len(dates),len(company))
        for i in range(1,len(company)):
            if(dates[i]=='2012' and company[i] in company2012):
                company2012[company[i]]+=1
            elif(dates[i]=='2012'):
                company2012[company[i]]=1

            if (dates[i] == '2013' and company[i] in company2013):
                company2013[company[i]] += 1
            elif (dates[i] == '2013'):
                company2013[company[i]] = 1

            if (dates[i] == '2014' and company[i] in company2014):
                company2014[company[i]] += 1
            elif (dates[i] == '2014'):
                company2014[company[i]] = 1

            if (dates[i] == '2015' and company[i] in company2015):
                company2015[company[i]] += 1
            elif (dates[i] == '2015'):
                company2015[company[i]] = 1
        all_years={company2012,company2013,company2014,company2015}
        json_values = json.loads(json.dumps(all_years))
        return JsonResponse(json_values)

# #'date_received
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
