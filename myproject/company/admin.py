from django.contrib import admin
from .models import Member
from .models import About
from .models import Contact


class MemberAdmin(admin.ModelAdmin):
    list_display = "image", "firstname", "lastname", "position"


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if About.objects.exists():
            obj = About.objects.first()
            return self.change_view(request, str(obj.id), extra_context=extra_context)
        return super().changelist_view(request, extra_context=extra_context)


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "created_at")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)


admin.site.register(Member, MemberAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)

