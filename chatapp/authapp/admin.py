from django.contrib import admin
from .models import User

# Register your models here.
class UserCostumers(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'password')

admin.site.register(User, UserCostumers)