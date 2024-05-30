from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    exclude = ['created_user']
    list_display=['batch_name','student_name','has_laptop']
admin.site.register(Student,StudentAdmin)