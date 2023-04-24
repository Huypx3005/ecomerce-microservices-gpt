from django.contrib import admin

from .models import Customer, Recommendation

# Register your models here.
admin.site.register(Customer)
admin.site.register(Recommendation)
