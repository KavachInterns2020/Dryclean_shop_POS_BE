from django.urls import path
import enterprise.views

urlpatterns = [	


	path('profile/<int:pk>/', enterprise.views.Profile.as_view()),
    path('profile/<int:pk>/edit/', enterprise.views.EditProfile.as_view()),
    path('payments/',enterprise.views.PaymentView.as_view()),
    path('payments/<int:pk>/',enterprise.views.PaymentDetailView.as_view()),
    path('payments/new/',enterprise.views.PaymentCreateView.as_view()),
    path('payments/<int:pk>/edit/',enterprise.views.PaymentEditView.as_view())
    ]