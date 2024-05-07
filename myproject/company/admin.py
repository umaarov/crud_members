from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = "image", "firstname", "lastname", "position"


admin.site.register(Member, MemberAdmin)
