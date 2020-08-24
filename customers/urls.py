from django.urls import path
import customers.views

urlpatterns = [
	path('',customers.views.CustomerView.as_view()),
	path('<int:pk>/',customers.views.CustomerDetailView.as_view()),
    path('new/',customers.views.CustomerCreateView.as_view()),
    path('<int:pk>/edit/',customers.views.EditCustomerView.as_view()),
]