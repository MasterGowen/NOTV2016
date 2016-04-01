from django.contrib import admin
from django.contrib.auth.models import Group
from reversion.admin import VersionAdmin

from .models import NOTVUser
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(VersionAdmin):
    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ('email', 'first_name', 'last_name', 'is_admin',)
    list_filter = ('is_admin',) 
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Персональная информация', {'fields': (('first_name', 'last_name'), 'department', 'position', 'tel', 'avatar')}),
        ('Участие', {'fields': ('status',)}),
        ('Даты', {'fields': ('last_login',)}),
        ('Проекты и права', {'fields': ('is_paid', 'is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(NOTVUser, UserAdmin)
admin.site.unregister(Group)