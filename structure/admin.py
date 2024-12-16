from django.contrib import admin

# Register your models here.

from structure.models import *


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'collection', 'year', 'total_purchased', 'total_revenue')

    def total_purchased(self, obj):
        return obj.purchase_statistics()["total_purchased"]

    def total_revenue(self, obj):
        return obj.purchase_statistics()["total_revenue"]

    total_purchased.short_description = "Продано"
    total_revenue.short_description = "Выручка"


admin.site.register(Collection)
admin.site.register(Year)
admin.site.register(Basket)
