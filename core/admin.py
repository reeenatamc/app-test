from django.contrib import admin
from django.contrib.auth.models import User

from unfold.admin import ModelAdmin as UnfoldModelAdmin

# Register your models here.
admin.site.unregister(User)

@admin.register(User)
class UserAdmin(UnfoldModelAdmin):
    pass

