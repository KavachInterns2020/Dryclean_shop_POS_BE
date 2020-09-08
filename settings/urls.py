from django.urls import path
import settings.views

urlpatterns = [	




 	path('product-type/',settings.views.ProductTypeView.as_view()),
    path('product-type/new/',settings.views.ProductTypeCreateView.as_view()),
    path('product-type/<int:pk>/edit/', settings.views.DeleteProductType.as_view()),
    path('service-type/',settings.views.ServiceTypeView.as_view()),
    path('service-type/new/',settings.views.ServiceTypeCreateView.as_view()),
    path('service-type/<int:pk>/edit/', settings.views.DeleteServiceType.as_view()),
    path('priority/',settings.views.PriorityView.as_view()),
    path('priority/new/',settings.views.PriorityView.as_view()),
    path('priority/<int:pk>/edit/', settings.views.DeletePriority.as_view()),
    path('status/',settings.views.StatusView.as_view()),
    path('status/new/',settings.views.StatusCreateView.as_view()),
    path('status/<int:pk>/edit/',settings.views.StatusEditView.as_view()),
    path('paymentmodes/',settings.views.PaymentModeView.as_view()),
    path('paymentmodes/new/',settings.views.PaymentModeCreateView.as_view()),
    path('paymentmodes/<int:pk>/edit/',settings.views.PaymentModeEditView.as_view())

    ]