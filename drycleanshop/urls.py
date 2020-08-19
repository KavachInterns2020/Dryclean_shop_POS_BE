"""drycleanshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
import enterprise.views
import settings.views
import customers.views
import orders.views
import employees.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
    path('profile/<int:pk>/', enterprise.views.Profile.as_view()),
    path('editprofile/<int:pk>/', enterprise.views.EditProfile.as_view()),
    path('product-type/',settings.views.ProductTypeView.as_view()),
    path('delete-product-type/<int:pk>/', settings.views.DeleteProductType.as_view()),
    path('service-type/',settings.views.ServiceTypeView.as_view()),
    path('delete-service-type/<int:pk>/', settings.views.DeleteServiceType.as_view()),
    path('priority/',settings.views.PriorityView.as_view()),
    path('delete-priority/<int:pk>/', settings.views.DeletePriority.as_view()),
    path('rate/',settings.views.RateView.as_view()),
    path('edit-rate/<int:pk>/', settings.views.EditRate.as_view()),
    path('customer/',customers.views.CustomerView.as_view()),
    path('edit-customer/<int:pk>/',customers.views.EditCustomerView.as_view()),
    path('order/',orders.views.OrderView.as_view()),
    path('order/order-item/',orders.views.OrderItemView.as_view()),
    path('order/order-item/edit-order-item/',orders.views.EditOrderItemView.as_view()),
    path('employees/',employees.views.EmployeeView.as_view()),
    path('edit-employee/<int:pk>/',employees.views.EditEmployeeView.as_view()),
    



]
