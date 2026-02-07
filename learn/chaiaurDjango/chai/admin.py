from django.contrib import admin
from .models import ChaiVariety, ChaiReview, Store, ChaiCertificate


# Inline review (one-to-many)
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1


# Chai variety admin
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "date_added")
    inlines = [ChaiReviewInline]


# Store admin (many-to-many)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    filter_horizontal = ("chai_varieties",)


# Certificate admin (one-to-one)
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ("chai", "certificate_number")


# Register models
admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)