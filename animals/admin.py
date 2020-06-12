from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from animals.models import Animals, Usuario
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Usuario, UserAdmin)
admin.site.register(Animals, DraggableMPTTAdmin)
