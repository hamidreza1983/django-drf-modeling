from django.contrib import admin
from .models import Service ,Menu,Events,Order, Skills,Chefs,ContactUs




admin.site.register(Menu)
admin.site.register(Events)
admin.site.register(Order)
admin.site.register(Skills)
admin.site.register(Chefs)
admin.site.register(ContactUs)
admin.site.register(Service)