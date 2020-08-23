from django.urls import path
import enterprise.views

urlpatterns = [	


	path('profile/<int:pk>/', enterprise.views.Profile.as_view()),
    path('editprofile/<int:pk>/', enterprise.views.EditProfile.as_view()),
    ]