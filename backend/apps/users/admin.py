from django.contrib import admin

from backend.apps.users.models import User, ActivationCode, AssociatedEmail


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('email', 'phone', )
    list_display = ('email', 'phone', 'superuser', 'is_active', 'email_confirmed', '_balance', )
    list_filter = ('is_active', 'email_confirmed', 'superuser', )


@admin.register(ActivationCode)
class ActivationCodeAdmin(admin.ModelAdmin):
    pass


@admin.register(AssociatedEmail)
class AssociatedEmailAdmin(admin.ModelAdmin):
    pass
