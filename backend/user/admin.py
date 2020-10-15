from django.contrib import admin
from backend.user.models import User
from django.contrib.auth.admin import UserAdmin
from backend.user.models import UserManager

# Register your models here.

# class AccountAdmin(AccountAdmin):
#     # add_form = 
#     # form = 
#     model = Account

# admin.site.register(Account,Accountadmin)

admin.site.register(User)