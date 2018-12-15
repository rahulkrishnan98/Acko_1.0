from django.conf.urls import url
from . import views

urlpatterns = [
    url('^login/$', views.UserLoginView.as_view(), name='login'),
    url('^logout/$', views.UserLogoutView.as_view(), name='logout'),
    url('^product/$', views.ProductComplaintView, name='product-view'),
    url('^subproduct/$', views.SubProductComplaint),
    url('^CompanyDispute/$', views.CompanyDispute),
    url('^ProductDispute/$', views.Demographic),
    url('^progressive_analysis/$', views.progressive_analysis),
    url('^firstbitthird/$',views.firstbitthird)
]





