from django.contrib import admin
from .models import order,Client,product,ClientTypes


admin.site.register(order)
admin.site.register(ClientTypes)
admin.site.register(product)
admin.site.register(Client)
