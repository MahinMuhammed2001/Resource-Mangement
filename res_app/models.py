from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from django.core.exceptions import ValidationError


# Create your models here.


class Master(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True,verbose_name="active")
    created_user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
   

class State(Master):
    state_name = models.CharField(max_length=100,unique=True)

    class Meta:
        verbose_name_plural='State'


    def __str__(self):
        return self.state_name
    
class District(Master):
    district_name = models.CharField(max_length=100,unique=True)
    state_name = models.ForeignKey(State, on_delete=models.CASCADE,limit_choices_to={"isactive":True})

    class Meta:
        verbose_name_plural ='District'



    def __str__(self):
        return self.district_name


class Branch(Master):
    branch_name=models.CharField(max_length=100,unique=True)
    branch_code=models.CharField(max_length=255,unique=True)
    address=models.CharField(max_length=255)
    location=models.CharField(max_length=100)
    contact_number=models.CharField(max_length=15)
    email=models.EmailField()
    pincode=models.CharField(max_length=10)
    state_name = models.ForeignKey(State, on_delete=models.CASCADE, limit_choices_to={"isactive": True})
    district_name = ChainedForeignKey(
        District,
        chained_field="state_name", 
        chained_model_field="state_name",  
        show_all=False,
        auto_choose=True,
        sort=True,
        limit_choices_to={"isactive": True}
    )
    
    class Meta:
        verbose_name_plural = 'Branch'

    def __str__(self):
        return self.branch_name


class ComptuerBrand(Master):
    brandname=models.CharField(max_length=100,unique=True)

    class Meta:
        verbose_name_plural="Computer Brands"
    
    def __str__(self):
        return self.brandname
    
class CourseName(Master):
    nameofcourse=models.CharField(max_length=100,unique=True)

    class Meta:
        verbose_name_plural="Course Name"
     
    def __str__(self):
         return self.nameofcourse
    





class OneTeamBatch(Master):
    branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE, limit_choices_to={"isactive": True})
    nameofcourse = models.ForeignKey(CourseName, on_delete=models.CASCADE, limit_choices_to={"isactive": True})
    start_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_year = models.PositiveIntegerField(editable=False, null=True)
    batch_name = models.CharField(max_length=100, unique=True, editable=False)  
    trainer_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Trainer", null=True, blank=False,
                                     related_name="Trainer", limit_choices_to={"is_active": True, "groups__name": 'Trainer'})
    is_closed = models.BooleanField(default=False, verbose_name="Closed")
    COURSE_TYPE_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]
    course_type = models.CharField(max_length=7, choices=COURSE_TYPE_CHOICES)

    class Meta:
        verbose_name_plural = "Batches"

    def save(self, *args, **kwargs):
        if not self.batch_name:
            self.batch_name = f"{self.start_year}-{self.trainer_name}-{self.start_date.strftime('%Y-%m-%d')}-{self.start_time.strftime('%H:%M')}-{self.course_type}-{self.branch_name.branch_name}-{self.nameofcourse.nameofcourse}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.batch_name


    

class System(Master):
    branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE, limit_choices_to={"isactive": True})
    CATEGORY_CHOICES = [
        ('laptop', 'Laptop'),
        ('desktop', 'Desktop'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    system_code = models.CharField(max_length=100, unique=True)
    RENTAL_OR_OWNER_CHOICES = [
        ('rental', 'Rental'),
        ('owner', 'Owner'),
    ]
    rental_or_owner = models.CharField(max_length=6, choices=RENTAL_OR_OWNER_CHOICES)
    brandname = models.ForeignKey(ComptuerBrand, on_delete=models.CASCADE, limit_choices_to={"isactive": True})
    serial_number = models.CharField(max_length=100, unique=True)
    trainer_name = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"is_active": True, "groups__name": "Trainer"})
    date_of_purchasing = models.DateField()
    date_of_return = models.DateField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Equipment'

    def __str__(self):
        return self.serial_number



    
class Room(Master):
    branch_name = models.ForeignKey('Branch', on_delete=models.CASCADE, limit_choices_to={"isactive": True})
    room_name = models.CharField(max_length=100)
    FLOOR_CHOICES = [
        ('ground', 'Ground Floor'),
        ('first', 'First Floor'),
        ('second', 'Second Floor'),
    ]
    floor = models.CharField(max_length=10, choices=FLOOR_CHOICES)
    ROOM_TYPE_CHOICES = [
        ('conference', 'Conference Room'),
        ('classroom', 'Class Room'),
    ]
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    number_of_seats = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return self.room_name
    



class RoomAllocation(Master):
    already_allocated = models.BooleanField(default=False)
    branch_name = models.ForeignKey('Branch', on_delete=models.CASCADE, limit_choices_to={"isactive": True})
    RESERVATION_TIME_CHOICES = [
        ('class', 'Class'),
        ('meeting', 'Meeting'),
    ]
    reservation_time = models.CharField(max_length=7, choices=RESERVATION_TIME_CHOICES)
    # batch_name = ChainedForeignKey(
    #     'OneTeamBatch',
    #     chained_field="branch_name",
    #     chained_model_field="branch",
    #     show_all=False,
    #     auto_choose=True,
    #     sort=True,
    #     limit_choices_to={"isactive": True}
    # )
    batch_name = models.ForeignKey('OneTeamBatch', on_delete=models.CASCADE, limit_choices_to={"isactive": True})
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # room_name = ChainedForeignKey(
    #     'Room',
    #     chained_field="branch_name",
    #     chained_model_field="Branch",
    #     show_all=False,
    #     auto_choose=True,
    #     sort=True,
    #     limit_choices_to={"isactive": True}
    # )
    room_name = models.ForeignKey('Room', on_delete=models.CASCADE, limit_choices_to={"isactive": True})
    PURPOSE_CHOICES = [
        ('class', 'Class'),
        ('project', 'Project'),
        ('interview', 'Interview'),
    ]
    purpose = models.CharField(max_length=10, choices=PURPOSE_CHOICES)

    class Meta:
        verbose_name_plural = 'Room Allocations'

    def clean(self):
        super().clean()

       
        overlapping_batch_allocations = RoomAllocation.objects.filter(
            batch_name=self.batch_name,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(id=self.id)

        if overlapping_batch_allocations.exists():
            raise ValidationError('This batch has an overlapping room allocation during the selected time.')

        overlapping_room_allocations = RoomAllocation.objects.filter(
            room_name=self.room_name,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(id=self.id)

        if overlapping_room_allocations.exists():
            raise ValidationError('This room is already allocated during the selected time.')

    def __str__(self):
        return self.purpose




    



    
