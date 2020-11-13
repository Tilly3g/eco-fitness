from django.contrib import admin
from .models import Session, Expert

# Register your models here.


class SessionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "amount",
        "length",
        "price",
        "Expert",
    )

    ordering = ('amount',)


class ExpertAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Session, SessionAdmin)
admin.site.register(Expert, ExpertAdmin)
