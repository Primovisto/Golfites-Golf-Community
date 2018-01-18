from django.contrib import admin
from .models import Equipment, EquipmentGallery


class ImagesInline(admin.TabularInline):
    model = EquipmentGallery


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
  ]


admin.site.register(Equipment, ProductAdmin)


