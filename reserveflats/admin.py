from django.contrib import admin
from .models import *

class ReserveFlatsAdmin(admin.ModelAdmin):
    list_display = 'id', 'floor', 'price', 'reserved'

class StripeAdmin(admin.ModelAdmin):
    list_display = 'id', 'payment_id', 'date_time'

class SuccessPaymentUserAdmin(admin.ModelAdmin):
    list_display = 'name', 'surname', 'email', 'phone', 'date_time'

admin.site.register(ReserveFlats, ReserveFlatsAdmin)
admin.site.register(StripePayment, StripeAdmin)
admin.site.register(SuccessPaymentUser, SuccessPaymentUserAdmin)
