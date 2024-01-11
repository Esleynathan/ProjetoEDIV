from django.contrib import admin
from .models import Users
from django.contrib.auth import admin as admin_auth_django
from .forms import UserChangeForm,UserCreationForm

@admin.register(Users)
class UserADmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    list_display = ("email", "firt_name", "last_name", "is_staff")
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (

    )