from django.urls import path
import orders.views

urlpatterns = [	

		path('',orders.views.OrderView.as_view()),
		path('<int:pk>/',orders.views.OrderDetailView.as_view()),
	    path('new/',orders.views.OrderCreateView.as_view()),
	    path('<int:pk>/edit/',orders.views.OrderEditView.as_view()),
	    path('<int:pk>/order-items/',orders.views.OrderItemView.as_view()),
	    path('<int:pk>/order-items/<int:pk_alt>/',orders.views.OrderItemDetailView.as_view()),
	    path('<int:pk>/new-order-item/',orders.views.OrderItemCreateView.as_view()),
	    path('<int:pk>/edit-order-item/<int:pk_alt>/',orders.views.EditOrderItemView.as_view()),
	    path('<int:pk>/order-items/<int:pk_alt>/status-history/',orders.views.StatusHistoryView.as_view()),
	    path('<int:pk>/order-items/<int:pk_alt>/status-history/update-status/',orders.views.StatusHistoryUpdateView.as_view())
    ]