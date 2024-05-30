# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from res_app.models import OneTeamBatch, System
from studentdetail.models import Student

class SystemAllocation(models.Model):
    batch_name = models.ForeignKey(OneTeamBatch, on_delete=models.CASCADE, limit_choices_to={"isactive": True})
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    has_laptop = models.BooleanField(default=False)
    no_laptop_student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True, related_name='no_laptop_students')
    system_code = models.ForeignKey(System, on_delete=models.CASCADE, limit_choices_to={"isactive": True})

    class Meta:
        verbose_name_plural = 'System Allocations'

    def clean(self):
        super().clean()

        if self.start_date >= self.end_date:
            raise ValidationError('End date must be after start date.')

        overlapping_allocations = SystemAllocation.objects.filter(
            system_code=self.system_code,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date
        ).exclude(id=self.id)

        if overlapping_allocations.exists():
            conflicting_allocation = overlapping_allocations.first()
            raise ValidationError(f'This system is already allocated during the selected time: {conflicting_allocation}.')

    def __str__(self):
        return f'{self.system_code} allocated to {self.student_name} from {self.start_date} to {self.end_date}'


    
    
