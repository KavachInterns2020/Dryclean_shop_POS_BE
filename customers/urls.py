from django.urls import path
import customers.views
''' The path '' corresponds to the GET request for all customers
	The path '<int:pk>/' corresponds to  GET request for individual customer
	The path 'new/' corresponds to POST request for creating new customers
	The path '<int:pk>/edit/' corresponds to both PUT and DELETE requests to edit or delete the customer
'''
urlpatterns = [
	path('',customers.views.CustomerView.as_view()),
	path('<int:pk>/',customers.views.CustomerDetailView.as_view()),
    path('new/',customers.views.CustomerCreateView.as_view()),
    path('<int:pk>/edit/',customers.views.EditCustomerView.as_view()),
]