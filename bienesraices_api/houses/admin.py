from django.contrib import admin
from .models import Houses, Sellers, HousesSellers

# Register your models here.
admin.site.register(Houses)
admin.site.register(Sellers)
admin.site.register(HousesSellers)


