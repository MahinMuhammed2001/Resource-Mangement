from django.contrib import admin
from .models import *



class StateAdmin(admin.ModelAdmin):
    exclude = ['created_user']
    list_display = ('state_name', 'isactive')
    search_fields = ('state_name',)
admin.site.register(State, StateAdmin)

class DistrictAdmin(admin.ModelAdmin):
    exclude = ['created_user']
    list_display = ('district_name', 'state_name', 'isactive')
    search_fields = ('district_name', 'state_name__state_name')
admin.site.register(District, DistrictAdmin)

class BranchAdmin(admin.ModelAdmin):
    exclude = ['created_user']
    list_display = ('district_name', 'state_name', 'isactive')
    search_fields = ('district_name', 'state_name__state_name')
admin.site.register(Branch, BranchAdmin)

class ComptuerBrandAdmin(admin.ModelAdmin):
    exclude = ['created_user']
    list_display = ('brandname', 'isactive')
      
admin.site.register(ComptuerBrand, ComptuerBrandAdmin)

class CourseNameAdmin(admin.ModelAdmin):
    exclude = ['created_user']
    list_display = ('nameofcourse', 'isactive')
   
admin.site.register(CourseName, CourseNameAdmin)

class OneTeamBatchAdmin(admin.ModelAdmin):
    exclude = ['created_user']
    readonly_fields = ('batch_name',)
    list_display = ('batch_name', 'branch_name', 'nameofcourse','trainer_name', 'is_closed', 'course_type')
admin.site.register(OneTeamBatch, OneTeamBatchAdmin)
    

class SystemAdmin(admin.ModelAdmin):
    exclude = ['created_user']
    list_display=['branch_name','category','rental_or_owner','brandname','trainer_name']
admin.site.register(System,SystemAdmin)

class RoomAdmin(admin.ModelAdmin):
    exclude = ['created_user']
    list_display=['branch_name','room_name','room_type','number_of_seats','floor']
admin.site.register(Room,RoomAdmin)


class RoomAllocationAdmin(admin.ModelAdmin):
    exclude = ['created_user']
    list_display=['branch_name','room_name','already_allocated','reservation_time','start_time','end_time','purpose']
admin.site.register(RoomAllocation,RoomAllocationAdmin)

