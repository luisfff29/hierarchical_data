from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from animals.models import Animals


# Register your models here.
admin.site.register(Animals, DraggableMPTTAdmin)
