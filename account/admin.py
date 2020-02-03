from django.contrib import admin

from .models import Roles
# Customise the Question admin section
class RolesAdmin(admin.ModelAdmin):
    list_display = ('id', 'role','created')
    # search_fields = ('title',)
    # list_display_links = ('id', 'title')

admin.site.register(Roles, RolesAdmin)