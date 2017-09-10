from django.contrib import admin
from .models import UpcomingEvents,SuccessfullEvents,SuccessfullEventsImages,ContactSection
# Register your models here.

# Register your models here.
@admin.register(UpcomingEvents)
class UpcomingEventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['date']


class SuccessfullEventsImagesInline(admin.StackedInline):
    model = SuccessfullEventsImages


@admin.register(ContactSection)
class ContactSectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['date']


@admin.register(SuccessfullEvents)
class SuccessfullEventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['date']

    inlines = [SuccessfullEventsImagesInline]
