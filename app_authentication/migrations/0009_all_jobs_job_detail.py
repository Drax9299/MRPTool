# Generated by Django 2.2.5 on 2020-03-21 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_authentication', '0008_history_sales_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='all_jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_username', models.CharField(max_length=20)),
                ('product_username', models.CharField(max_length=20)),
                ('job_id', models.CharField(max_length=20)),
                ('job_desc', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'all_jobs',
            },
        ),
        migrations.CreateModel(
            name='job_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_username', models.CharField(max_length=20)),
                ('product_username', models.CharField(max_length=20)),
                ('job_id', models.CharField(max_length=20)),
                ('attribute_id', models.SmallIntegerField()),
                ('attribute_name', models.CharField(max_length=40)),
                ('attribute_required_quantity', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'job_detail',
            },
        ),
    ]