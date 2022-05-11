from django.contrib import admin
from .models import Profile
from django.core.exceptions import PermissionDenied


class ProfileAdmin(admin.ModelAdmin):

    list_display = ['user', 'is_verify']

    actions = ['set_verify', 'set_unverify']

    def set_verify(self, request, queryset):
        print(request.user.has_perm('user_auth.can_verify_profile'))
        if not request.user.has_perm('user_auth.can_verify_profile'):
            raise PermissionDenied('У вас нет разрешения к этому действию')
        queryset.update(is_verify=True)
        for user in queryset:
            user.group.add(2)

    def set_unverify(self, request, queryset):
        queryset.update(is_verify=False)

    set_verify.short_description = 'Верифицировать'
    set_unverify.short_description = 'Снять верификацию'

admin.site.register(Profile, ProfileAdmin)
