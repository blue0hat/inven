from django.contrib import admin
from .models import Part
from import_export.admin import ImportExportModelAdmin
# Register your models here.


admin.site.register(Part, ImportExportModelAdmin)