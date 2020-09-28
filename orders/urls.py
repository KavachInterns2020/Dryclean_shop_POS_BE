from django.urls import path
import orders.views
''' The path '' corresponds to the GET request for all orders
	The path '<int:pk>/' corresponds to  GET request for individual order
	The path 'new/' corresponds to POST request for creating new orders
	The path '<int:pk>/edit/' corresponds to both PUT and DELETE requests to edit or delete the order

	The path '<int:pk>/order-items/' corresponds to the GET request for all order items present in the order 
	The path '<int:pk>/order-items/<int:pk_alt>/' corresponds to  GET request for individual order item in the particular order
	The path '<int:pk>/order-items/new/' corresponds to POST request for creating new order items within the order
	The path '<int:pk>/order-items/<int:pk_alt>/edit/' corresponds to both PUT and DELETE requests to edit or delete the order items within the order
	
	The path '<int:pk>/order-items/<int:pk_alt>/status-history/' corresponds to the GET request for the status history of the order item
	The path '<int:pk>/order-items/<int:pk_alt>/status-history/update-status' corresponds to  POST request for new updates in status history 
	
'''
urlpatterns = [	

		path('',orders.views.OrderView.as_view()),
		path('<int:pk>/',orders.views.OrderDetailView.as_view()),
	    path('new/',orders.views.OrderCreateView.as_view()),
	    path('<int:pk>/edit/',orders.views.OrderEditView.as_view()),
	    path('<int:pk>/order-items/',orders.views.OrderItemView.as_view()),
	    path('<int:pk>/order-items/<int:pk_alt>/',orders.views.OrderItemDetailView.as_view()),
	    path('<int:pk>/order-items/new/',orders.views.OrderItemCreateView.as_view()),
	    path('<int:pk>/order-items/<int:pk_alt>/edit/',orders.views.EditOrderItemView.as_view()),
	    path('<int:pk>/order-items/<int:pk_alt>/status-history/',orders.views.StatusHistoryView.as_view()),
	    path('<int:pk>/order-items/<int:pk_alt>/status-history/update-status/',orders.views.StatusHistoryUpdateView.as_view())
    ]