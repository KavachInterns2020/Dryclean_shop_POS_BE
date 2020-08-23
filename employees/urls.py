from django.urls import path
import employees.views

urlpatterns = [	




	path('',employees.views.EmployeeView.as_view()),
    path('new/',employees.views.EmployeeCreateView.as_view()),
    path('edit-employee/<int:pk>/',employees.views.EditEmployeeView.as_view()),
    path('roles/',employees.views.RoleView.as_view()),
    path('roles/new/',employees.views.RoleCreateView.as_view()),

    ]