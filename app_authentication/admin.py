from django.contrib import admin
from .models import product_detail,attribute_product,company_detail
# Register your models here.

admin.site.register(company_detail)
admin.site.register(product_detail)
admin.site.register(attribute_product)
