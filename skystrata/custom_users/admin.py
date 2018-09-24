# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()
admin.site.register(User)

#from django.contrib.auth import admin as auth_admin
# @admin.register(User)
# class UserAdmin(auth_admin.UserAdmin):
#
#     form = UserChangeForm
#     add_form = UserCreationForm
#     fieldsets = (("User", {"fields": ("name",'address','phone','timezone')}),) + auth_admin.UserAdmin.fieldsets
#     list_display = ["username", "name", "is_superuser"]
#     search_fields = ["name"]