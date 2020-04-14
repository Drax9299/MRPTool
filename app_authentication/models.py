from django.db import models

# Create your models here.

# Create your models here.
class company_detail(models.Model):
    company_username = models.CharField(max_length = 20, primary_key = True)
    company_realname = models.CharField(max_length = 50)
    company_password = models.CharField(max_length = 20)

    class Meta:
        db_table = 'company_detail'

class admin_detail(models.Model):
    company_username = models.CharField(max_length=20)
    admin_username = models.CharField(max_length=20)
    admin_password = models.CharField(max_length=20)
    admin_realname = models.CharField(max_length=50)

    class Meta:
        db_table = 'admin_detail'

class worker_detail(models.Model):
    company_username = models.CharField(max_length=20)
    worker_username = models.CharField(max_length=20)
    worker_password = models.CharField(max_length=20)
    worker_realname = models.CharField(max_length=50)

    class Meta:
        db_table = 'worker_detail'

class product_detail(models.Model):
    company_username = models.CharField(max_length = 20)
    product_username = models.CharField(max_length = 20)
    product_realname = models.CharField(max_length = 50)
    product_description = models.CharField(max_length = 100)

    class Meta:
        db_table = 'product_detail'

class attribute_product(models.Model):
    company_username = models.CharField(max_length = 20)
    product_username = models.CharField(max_length = 20)
    attribute_id = models.SmallIntegerField()
    attribute_name = models.CharField(max_length = 40)
    attribute_required_quantity = models.PositiveIntegerField()
    attribute_current_quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'attribute_product'

class history_sales_data(models.Model):
    company_username = models.CharField(max_length = 20)
    product_username = models.CharField(max_length = 20)
    month = models.SmallIntegerField()
    year = models.CharField(max_length = 4)
    unit_sold = models.PositiveIntegerField()
    unit_produced = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    class Meta:
        db_table = 'history_sales_data'

class all_jobs(models.Model):
    company_username = models.CharField(max_length = 20)
    product_username = models.CharField(max_length = 20)
    job_id = models.CharField(max_length = 20)
    job_desc = models.CharField(max_length = 100)

    class Meta:
        db_table  = 'all_jobs'

class job_detail(models.Model):
    company_username = models.CharField(max_length = 20)
    product_username = models.CharField(max_length = 20)
    job_id = models.CharField(max_length = 20)
    attribute_id = models.SmallIntegerField()
    attribute_name = models.CharField(max_length = 40)
    attribute_required_quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'job_detail'

class job_assign(models.Model):
    company_username = models.CharField(max_length = 20)
    product_username = models.CharField(max_length = 20)
    job_id = models.CharField(max_length = 20)
    worker_username = models.CharField(max_length=20)
    e_start_time = models.DateTimeField()
    e_end_time = models.DateTimeField()
    a_start_time = models.DateTimeField()
    a_end_time = models.DateTimeField()
    number_jobs = models.SmallIntegerField()
    numer_jobs_done = models.SmallIntegerField()
    instruction = models.CharField(max_length = 50)
    missed_jobs = models.SmallIntegerField()

    class Meta:
        db_table = 'job_assign'

class worker_data(models.Model):
    company_username = models.CharField(max_length=20)
    worker_username = models.CharField(max_length=20)
    jobs_done = models.PositiveIntegerField()
    jobs_assigned = models.PositiveIntegerField()
    efficiency = models.FloatField()
    tasks_done = models.PositiveIntegerField()
    tasks_assigned = models.PositiveIntegerField()

    class Meta:
        db_table = 'worker_data'
