from django.contrib import admin
from .models import Gallery, AboutTour, Tour, Contact


admin.site.register(Gallery)
admin.site.register(AboutTour)
admin.site.register(Contact)


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost')
    list_editable = ('cost',)
    prepopulated_fields = {'slug': ('title',)}
