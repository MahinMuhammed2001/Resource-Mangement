# Generated by Django 4.2.6 on 2024-05-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res_app', '0010_remove_oneteambatch_batch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='oneteambatch',
            name='batch_name',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
