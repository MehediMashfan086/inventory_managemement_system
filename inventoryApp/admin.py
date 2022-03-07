from django.contrib import admin

from inventoryApp.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Laptop, Desktop, Mobile)
class ViewAdmin(ImportExportModelAdmin):
    pass
