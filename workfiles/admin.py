from django.contrib import admin
from .models import maindata, breakstime, fileimg

class BreakstimeInline(admin.TabularInline):
    model = breakstime
    extra = 1  # Number of extra forms to display

class FileimgInline(admin.TabularInline):
    model = fileimg
    extra = 1  # Number of extra forms to display

@admin.register(maindata)
class MaindataAdmin(admin.ModelAdmin):
    inlines = [BreakstimeInline, FileimgInline]
    list_display = ['name', 'natid', 'phone', 'addres_location', 'deg', 'work', 'frest_work_place', 'carant_work_place', 'work_starting_date', 'hospital_work_starting_date']

# Register the other models if needed
admin.site.register(breakstime)
admin.site.register(fileimg)
