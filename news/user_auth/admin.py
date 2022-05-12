from django.contrib import admin
from .models import Profile
from django.core.exceptions import PermissionDenied


class ProfileAdmin(admin.ModelAdmin):

    list_display = ['user', 'is_verify']

    actions = ['set_verify', 'set_unverify']

    def set_verify(self, request, queryset):
        # при проверке permissions, добавляемого в Meta модели не нужно указывать ..._<model>:
        # просто <app>.<action> 
        if not request.user.has_perm('user_auth.can_verify'):
            raise PermissionDenied('У вас нет разрешения к этому действию')
        queryset.update(is_verify=True)
        for profile in queryset:
            profile.user.groups.add(2)

    def set_unverify(self, request, queryset):
        if not request.user.has_perm('user_auth.can_verify'):
            raise PermissionDenied('У вас нет разрешения к этому действию')
        queryset.update(is_verify=False)
        for profile in queryset:
            profile.user.groups.remove(2)

    set_verify.short_description = 'Верифицировать'
    set_unverify.short_description = 'Снять верификацию'

admin.site.register(Profile, ProfileAdmin)
