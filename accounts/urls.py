from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.UserLoginView.as_view(), name='login'),
    url(r'^logout/$', views.UserLogoutView.as_view(), name='logout'),
    url(r'^product/$', views.ProductComplaintView, name='product-view'),
    url(r'^company_sub/$', views.firstbitthird),
    url(r'^sub_product/(?P<product>\w+)/$', views.SubProductComplaint),
    url(r'^company_dispute/$', views.CompanyDispute),
    url(r'^product_dispute/$', views.Demographic),
    url(r'performance/$', views.performance),

    url(r'^sample/$', views.company_names),


]



