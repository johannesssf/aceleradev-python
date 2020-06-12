from django.contrib import admin

from api.models import User, Agent, Group, Event, GroupUser


admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Group)
admin.site.register(Event)
admin.site.register(GroupUser)
