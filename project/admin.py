from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Boat)
admin.site.register(Customer)
admin.site.register(Guide)
admin.site.register(Booking)


