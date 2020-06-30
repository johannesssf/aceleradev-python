from django.contrib import admin

from api.models import User, Agent, Group, Event


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_login', 'view_groups')
    ordering = ['name']

    def view_groups(self, obj):
        return obj.group.first().name


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('level',)


admin.site.register(Agent)
admin.site.register(Group)
