from django.contrib import admin

from .models import Flat, Complaints, Owner


class OwnersInline(admin.TabularInline):
    model = Owner.flats.through
    allow_add = True
    raw_id_fields = ('owner',)
    

class FlatAdmin(admin.ModelAdmin):
    inlines = [
        OwnersInline,
    ]
    search_fields = ('town', 'address', 'owner', 'town')
    readonly_fields = ["created_at"]
    list_display = ["address", "price", "new_building", "construction_year"]
    list_editable = ["new_building"]
    list_filter = ["new_building", "rooms_number", "has_balcony"]
    raw_id_fields = ("like",)


class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ["author", "flat"]
    raw_id_fields = ("author", "flat")


class OwnerAdmin(admin.ModelAdmin):
    list_display = ["name"]
    raw_id_fields = ("flats",)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaints, ComplaintsAdmin)
admin.site.register(Owner, OwnerAdmin)
