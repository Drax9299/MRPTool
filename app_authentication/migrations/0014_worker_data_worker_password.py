# Generated by Django 2.2.5 on 2020-04-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_authentication', '0013_job_assign_missed_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker_data',
            name='worker_password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
