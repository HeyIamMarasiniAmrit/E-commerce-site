from django.contrib import admin

# Register your models here.
from .models import product,contact,orders, OrderUpdate

admin.site.register(product)
admin.site.register(contact)
admin.site.register(orders)
admin.site.register(OrderUpdate)
