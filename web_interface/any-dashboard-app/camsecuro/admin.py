from django.contrib import admin

# Register your models here.
from .models import Cities
from .models import Addresses
from .models import Cameras

admin.site.register(Cities)
admin.site.register(Addresses)
# admin.site.register(Cameras)

@admin.register(Cameras)
class CamerasAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'address_id', 'get_city')
    # list_filter = (SpeciesListFilter, )
    def get_city(self, obj):
        return obj.address_id.city_id