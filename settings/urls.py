from django.urls import path
import settings.views

''' The path 'product-type/' corresponds to the GET request for all product types
    The path 'product-type/<int:pk>/' corresponds to  GET request for individual product type
    The path 'product-type/new/' corresponds to POST request for creating new product types
    The path 'product-type/<int:pk>/edit/' corresponds to both PUT and DELETE requests to edit or delete the product type

    The path 'service-type/' corresponds to the GET request for all service types
    The path 'service-type/<int:pk>/' corresponds to  GET request for individual service type
    The path 'service-type/new/' corresponds to POST request for creating new service types
    The path 'service-type/<int:pk>/edit/' corresponds to both PUT and DELETE requests to edit or delete the service type

    The path 'priority/' corresponds to the GET request for all priorities
    The path 'priority/<int:pk>/' corresponds to  GET request for individual priority
    The path 'priority/new/' corresponds to POST request for creating new priority
    The path 'priority/<int:pk>/edit/' corresponds to both PUT and DELETE requests to edit or delete the priority

    The path 'status/' corresponds to the GET request for all statuses
    The path 'status/<int:pk>/' corresponds to  GET request for individual status
    The path 'status/new/' corresponds to POST request for creating new status
    The path 'status/<int:pk>/edit/' corresponds to both PUT and DELETE requests to edit or delete the status

    The path 'paymentmodes/' corresponds to the GET request for all payment modes
    The path 'paymentmodes/<int:pk>/' corresponds to  GET request for individual payment mode
    The path 'paymentmodes/new/' corresponds to POST request for creating new payment mode
    The path 'paymentmodes/<int:pk>/edit/' corresponds to both PUT and DELETE requests to edit or delete the payment modes

'''

urlpatterns = [	



 	path('product-type/',settings.views.ProductTypeView.as_view()),
    path('product-type/new/',settings.views.ProductTypeCreateView.as_view()),
    path('product-type/<int:pk>/',settings.views.ProductTypeDetailView.as_view()),
    path('product-type/<int:pk>/edit/', settings.views.DeleteProductType.as_view()),
    path('service-type/',settings.views.ServiceTypeView.as_view()),
    path('service-type/new/',settings.views.ServiceTypeCreateView.as_view()),
    path('service-type/<int:pk>/',settings.views.ServiceTypeDetailView.as_view()),
    path('service-type/<int:pk>/edit/', settings.views.DeleteServiceType.as_view()),
    path('priority/',settings.views.PriorityView.as_view()),
    path('priority/new/',settings.views.PriorityView.as_view()),
    path('priority/<int:pk>/',settings.views.PriorityDetailView.as_view()),
    path('priority/<int:pk>/edit/', settings.views.DeletePriority.as_view()),
    path('status/',settings.views.StatusView.as_view()),
    path('status/new/',settings.views.StatusCreateView.as_view()),
    path('status/<int:pk>/',settings.views.StatusDetailView.as_view()),
    path('status/<int:pk>/edit/',settings.views.StatusEditView.as_view()),
    path('paymentmodes/',settings.views.PaymentModeView.as_view()),
    path('paymentmodes/new/',settings.views.PaymentModeCreateView.as_view()),
    path('paymentmodes/<int:pk>/',settings.views.PaymentModeDetailView.as_view()),
    path('paymentmodes/<int:pk>/edit/',settings.views.PaymentModeEditView.as_view())

    ]