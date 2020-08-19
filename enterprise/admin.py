from django.contrib import admin
from users.models import CustomUser
from .models import Enterprise
from settings.models import ProductType,ServiceType,Priority,Rate,PaymentModes,Status
from customers.models import Customer
from employees.models import Employee,Role
from orders.models import Order,OrderItem
admin.site.register(CustomUser)
admin.site.register(Enterprise)
admin.site.register(ProductType)
admin.site.register(ServiceType)
admin.site.register(Priority)
admin.site.register(Rate)
admin.site.register(PaymentModes)
admin.site.register(Status)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Order)
admin.site.register(OrderItem)
