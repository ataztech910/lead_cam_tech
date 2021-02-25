from django.contrib import admin

# Register your models here.
from .models import Cities
from .models import Addresses
from .models import Cameras

admin.site.register(Cities)
admin.site.register(Addresses)
admin.site.register(Cameras)