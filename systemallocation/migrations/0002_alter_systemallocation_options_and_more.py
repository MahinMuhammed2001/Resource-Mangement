# Generated by Django 4.2.6 on 2024-05-30 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('res_app', '0015_alter_roomallocation_batch_name_and_more'),
        ('systemallocation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='systemallocation',
            options={'verbose_name_plural': 'System Allocations'},
        ),
        migrations.AddField(
            model_name='systemallocation',
            name='system_code',
            field=models.ForeignKey(default=1, limit_choices_to={'isactive': True}, on_delete=django.db.models.deletion.CASCADE, to='res_app.system'),
            preserve_default=False,
        ),
    ]
