from django.urls import path
import employees.views
''' The path '' corresponds to the GET request for all employees
	The path '<int:pk>/' corresponds to  GET request for individual employee
	The path 'new/' corresponds to POST request for creating new new
	The path '<int:pk>/edit/' corresponds to both PUT and DELETE requests to edit or delete the employee

	The path 'roles/' corresponds to the GET request for all roles
	The path '<int:pk>/' corresponds to  GET request for individual role
	The path 'new/' corresponds to POST request for creating new roles
	The path '<int:pk>/edit/' corresponds to both PUT and DELETE requests to edit or delete the role

'''
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