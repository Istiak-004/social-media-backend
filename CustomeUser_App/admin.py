from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea,TextInput 
from djrichtextfield.widgets import RichTextWidget



class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'username', 'first_name','last_name')
    list_filter = ('email', 'username', 'first_name','last_name','is_active', 'is_staff')
    ordering = ('username',)
    list_display = ('email', 'username', 'first_name','last_name',
                    'is_active', 'is_staff')
    fieldsets = (
        ('General', {'fields': ('email', 'username', ('first_name','last_name'))}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        NewUser.about: {'widget': RichTextWidget()},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide','extrapretty',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
