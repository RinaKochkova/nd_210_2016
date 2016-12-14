from django.contrib import admin

# Register your models here.

from .models import Deputy, Faction

admin.site.register(Deputy,Faction)
