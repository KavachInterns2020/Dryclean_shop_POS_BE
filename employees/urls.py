from django.urls import path
import employees.views

urlpatterns = [	




	path('',employees.views.EmployeeView.as_view()),
	path('<int:pk>/',employees.views.EmployeeDetailView.as_view()),
    path('new/',employees.views.EmployeeCreateView.as_view()),
    path('<int:pk>/edit/',employees.views.EditEmployeeView.as_view()),
    path('roles/',employees.views.RoleView.as_view()),
    path('roles/<int:pk>/',employees.views.RoleDetailView.as_view()),
    path('roles/new/',employees.views.RoleCreateView.as_view()),
    path('roles/<int:pk>/edit/',employees.views.RoleEditView.as_view()),

    ]