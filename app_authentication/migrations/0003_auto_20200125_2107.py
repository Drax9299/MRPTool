# Generated by Django 2.2.5 on 2020-01-25 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_authentication', '0002_auto_20200125_2106'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='company_details',
            new_name='company_detail',
        ),
    ]