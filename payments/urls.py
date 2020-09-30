from django.urls import path
import payments.views

'''  
	The path '' corresponds to GET request for all the payment records
	The path '<int:pk>/' corresponds to GET request for individual payment records
	The path 'new/' corresponds to POST request for creating new payment record
	The path 'payments/<int:pk>/edit/' corresponds to both PUT and DELETE requests to edit or delete the payment record
'''

urlpatterns=[
	path('',payments.views.PaymentView.as_view()),
    path('<int:pk>/',payments.views.PaymentDetailView.as_view()),
    path('new/',payments.views.PaymentCreateView.as_view()),
    path('<int:pk>/edit/',payments.views.PaymentEditView.as_view())
    ]