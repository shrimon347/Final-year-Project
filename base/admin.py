from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Message, Room, Topic, User


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email','is_staff')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('name','email','bio','avatar','follows')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email','name','bio','avatar', 'password1', 'password2','follows', ),
        }),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
