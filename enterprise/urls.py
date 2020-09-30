from django.urls import path
import enterprise.views
''' The path 'profile/' corresponds to the GET request for the Enterprise
	The path 'profile/edit/<int:pk>/' corresponds to  PUT request for individual enterprise
'''
urlpatterns = [	


	path('profile/', enterprise.views.Profile.as_view()),
    path('profile/edit/<int:pk>/', enterprise.views.EditProfile.as_view()),
   ]