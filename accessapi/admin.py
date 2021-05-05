from django.contrib import admin
from .models import check
# Register your models here.
@admin.register(check)
class CheckAdmin(admin.ModelAdmin):
    class Meta:
        model = check
