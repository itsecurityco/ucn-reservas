from django.contrib import admin
from .models import Device, Borrow

class DeviceAdmin(admin.ModelAdmin):
    list_display  = (
        'id',
        'type',
        'brand',
        'model',
        'available',
        'condition',
    )


class BorrowAdmin(admin.ModelAdmin):
    list_display  = (
        'id',
        'user',
        'device',
        'carrier',
        'status',
    )


# Register your models here.
admin.site.register(Device, DeviceAdmin)
admin.site.register(Borrow, BorrowAdmin)
