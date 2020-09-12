from django.urls import path
import workshops.views

urlpatterns = [	
	path('',workshops.views.WorkshopView.as_view()),
	path('new/',workshops.views.WorkshopCreateView.as_view()),
	path('<int:pk>/',workshops.views.WorkshopDetailView.as_view()),
	path('<int:pk>/edit/',workshops.views.EditWorkshopView.as_view())
	]