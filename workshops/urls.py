from django.urls import path
import workshops.views

'''	The path '' corresponds to the GET request for all workshops
	The path '<int:pk>/' corresponds to  GET request for individual workshop
	The path 'new/' corresponds to POST request for creating new workshop
	The path '<int:pk>/edit/' corresponds to both PUT and DELETE requests to edit or delete the workshop
'''
urlpatterns = [	
	path('',workshops.views.WorkshopView.as_view()),
	path('new/',workshops.views.WorkshopCreateView.as_view()),
	path('<int:pk>/',workshops.views.WorkshopDetailView.as_view()),
	path('<int:pk>/edit/',workshops.views.EditWorkshopView.as_view())
	]