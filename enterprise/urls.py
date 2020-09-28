from django.urls import path
import enterprise.views
''' The path 'profile/' corresponds to the GET request for the Enterprise
	The path 'profile/edit/<int:pk>/' corresponds to  PUT request for individual enterprise
	The path 'payments/' corresponds to GET request for all the payment records
	The path 'payments/<int:pk>/' corresponds to GET request for individual payment records
	The path 'payments/new/' corresponds to POST request for creating new payment record
	The path 'payments/<int:pk>/edit/' corresponds to both PUT and DELETE requests to edit or delete the payment record
'''
urlpatterns = [	


	path('profile/', enterprise.views.Profile.as_view()),
    path('profile/edit/<int:pk>/', enterprise.views.EditProfile.as_view()),
    path('payments/',enterprise.views.PaymentView.as_view()),
    path('payments/<int:pk>/',enterprise.views.PaymentDetailView.as_view()),
    path('payments/new/',enterprise.views.PaymentCreateView.as_view()),
    path('payments/<int:pk>/edit/',enterprise.views.PaymentEditView.as_view())
    ]