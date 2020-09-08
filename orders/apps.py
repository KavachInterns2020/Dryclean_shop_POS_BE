from django.apps import AppConfig
from orders.models import StatusHistory
from django.core.mail import send_mail

class OrdersConfig(AppConfig):
    name = 'orders'

        