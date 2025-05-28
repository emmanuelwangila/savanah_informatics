from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer
from django.utils.translation import gettext_lazy as _

# Register your models here.
class CustomerAdmin(UserAdmin):
    model = Customer
    list_display = ('username', 'email', 'phone_number', 'email_verified', 'is_staff', 'sign_up_date')
    list_filter = ('is_staff', 'is_superuser', 'email_verified', 'sign_up_date')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('-sign_up_date',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'sign_up_date')}),
        (_('Verification'), {'fields': ('email_verified',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'phone_number', 'date_of_birth'),
        }),
    )

# Register the custom user
admin.site.register(Customer, CustomerAdmin)



