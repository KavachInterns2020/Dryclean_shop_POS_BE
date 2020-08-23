from django.urls import path
import orders.views

urlpatterns = [	

		path('',orders.views.OrderView.as_view()),
	    path('new/',orders.views.OrderCreateView.as_view()),
	    path('<int:pk>/order-items/',orders.views.OrderItemView.as_view()),
	    path('<int:pk>/new-order-item/',orders.views.OrderItemCreateView.as_view()),
	    path('<int:pk>/edit-order-item/',orders.views.EditOrderItemView.as_view()),
    ]