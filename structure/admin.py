from django.contrib import admin

# Register your models here.

from structure.models import *

admin.site.register(Collection)
admin.site.register(Artwork)
admin.site.register(Year)