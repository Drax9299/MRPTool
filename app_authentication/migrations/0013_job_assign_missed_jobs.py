# Generated by Django 2.2.5 on 2020-04-14 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_authentication', '0012_worker_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_assign',
            name='missed_jobs',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
