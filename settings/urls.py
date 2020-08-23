from django.urls import path
import settings.views

urlpatterns = [	




 	path('product-type/',settings.views.ProductTypeView.as_view()),
    path('product-type/new/',settings.views.ProductTypeCreateView.as_view()),
    path('delete-product-type/<int:pk>/', settings.views.DeleteProductType.as_view()),
    path('service-type/',settings.views.ServiceTypeView.as_view()),
    path('service-type/new/',settings.views.ServiceTypeCreateView.as_view()),
    path('delete-service-type/<int:pk>/', settings.views.DeleteServiceType.as_view()),
    path('priority/',settings.views.PriorityView.as_view()),
    path('priority/new/',settings.views.PriorityView.as_view()),
    path('delete-priority/<int:pk>/', settings.views.DeletePriority.as_view()),

    ]