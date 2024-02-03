from django.contrib import admin

from .models import Birthday, Tag


class BirtdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday'
    )
    list_editable = (
        'birthday',
    )

    list_display_links = (
        'first_name',
    )

class TagAdmin(admin.ModelAdmin):
    list_display = (
        'tag',
    )
    list_display_links = (
        'tag',
    )


admin.site.register(Birthday, BirtdayAdmin)
admin.site.register(Tag, TagAdmin)
