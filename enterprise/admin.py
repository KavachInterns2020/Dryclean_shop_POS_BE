from django.contrib import admin
from users.models import CustomUser
from .models import Enterprise
from settings.models import ProductType,ServiceType,Priority,PaymentModes,Status
from customers.models import Customer
from employees.models import Employee,Role
from orders.models import Order,OrderItem,StatusHistory
from logs.models import Logs
from workshops.models import Workshop

admin.site.register(CustomUser)
admin.site.register(Enterprise)
admin.site.register(ProductType)
admin.site.register(ServiceType)
admin.site.register(Priority)
admin.site.register(PaymentModes)
admin.site.register(Status)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Logs)
admin.site.register(Workshop)
admin.site.register(StatusHistory)
