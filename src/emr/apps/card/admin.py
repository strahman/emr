from django.contrib import admin

from models import UserCard, Visits


class UserCardAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "code", "email", 'birthday')
    search_fields = [item.name for item in UserCard._meta.fields if item.name not in \
        ('city', 'oblast', 'birthday', 'last_visit', 'created', 'updated')]

admin.site.register(UserCard, UserCardAdmin)


class VisitsAdmin(admin.ModelAdmin):
    list_display = ("patient", "visit_time")

admin.site.register(Visits, VisitsAdmin)
