# Generated by Django 4.2.6 on 2024-05-30 04:41

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('res_app', '0015_alter_roomallocation_batch_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='district_name',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state_name', chained_model_field='state_name', limit_choices_to={'isactive': True}, on_delete=django.db.models.deletion.CASCADE, to='res_app.district'),
        ),
    ]
