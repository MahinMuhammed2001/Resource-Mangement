# Generated by Django 4.2.6 on 2024-05-26 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res_app', '0005_remove_oneteambatch_course_type_oneteambatch_batch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='oneteambatch',
            name='course_type',
            field=models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], default=1, max_length=7),
            preserve_default=False,
        ),
    ]