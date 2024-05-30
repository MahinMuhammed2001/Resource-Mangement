# Generated by Django 4.2.6 on 2024-05-26 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('res_app', '0006_oneteambatch_course_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('master_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='res_app.master')),
                ('category', models.CharField(choices=[('laptop', 'Laptop'), ('desktop', 'Desktop')], max_length=50)),
                ('system_code', models.CharField(max_length=100, unique=True)),
                ('rental_or_owner', models.CharField(choices=[('rental', 'Rental'), ('owner', 'Owner')], max_length=6)),
                ('serial_number', models.CharField(max_length=100, unique=True)),
                ('date_of_purchasing', models.DateField()),
                ('date_of_return', models.DateField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('branch_name', models.ForeignKey(limit_choices_to={'isactive': True}, on_delete=django.db.models.deletion.CASCADE, to='res_app.branch')),
                ('brandname', models.ForeignKey(limit_choices_to={'isactive': True}, on_delete=django.db.models.deletion.CASCADE, to='res_app.comptuerbrand')),
                ('trainer_name', models.ForeignKey(limit_choices_to={'groups__name': 'Trainer', 'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Equipment',
            },
            bases=('res_app.master',),
        ),
    ]