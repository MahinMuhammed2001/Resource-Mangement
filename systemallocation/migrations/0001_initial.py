# Generated by Django 4.2.6 on 2024-05-26 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('res_app', '0009_roomallocation'),
        ('studentdetail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('has_laptop', models.BooleanField(default=False)),
                ('batch_name', models.ForeignKey(limit_choices_to={'isactive': True}, on_delete=django.db.models.deletion.CASCADE, to='res_app.oneteambatch')),
                ('no_laptop_student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='no_laptop_students', to='studentdetail.student')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentdetail.student')),
            ],
        ),
    ]
