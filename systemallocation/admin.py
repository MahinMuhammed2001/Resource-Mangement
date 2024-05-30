from django.contrib import admin
from .models import SystemAllocation

# Register your models here.
class SystemAllocationAdmin(admin.ModelAdmin):
    exclude = ['created_user']
    list_display=['batch_name','student_name','has_laptop','no_laptop_student']
admin.site.register(SystemAllocation,SystemAllocationAdmin)

