from django.contrib import admin
from .models import Profile


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'surname', 'bio', 'avatar', 'user')
    list_display_links = ('pk', 'user')


admin.site.register(Profile, ProfilesAdmin)
