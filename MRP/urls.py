"""MRP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.company_login_func,name = 'company_login'),
    path('register_company/',views.company_register_func,name = 'company_register'),
    path('admin_login/',views.admin_login_func,name='admin_login'),
    path('admin_register/',views.admin_register_func,name = 'admin_register'),
    path('worker_login/',views.worker_login_func,name='worker_login'),
    path('worker_register/',views.worker_register_func,name = 'worker_register'),
    path('productselection.html/',views.product_selection_func,name= 'product_selection'),
    path('dashboard/<str:pname>/',views.dashboard_func,name='dashboard'),
    path('create_product/',views.create_product_func,name='create-product'),
    path('product_selection/',views.product_selection_func,name='product-selection'),
    path('stock_analysis/',views.stock_analysis_func,name='stock-analysis'),
    path('demand_prediction/',views.demand_prediction_func,name='demand-prediction'),
    path('price_prediction/',views.price_prediction_func,name='price-prediction'),
    path('add_sales_data/',views.add_sales_data_func,name='add-sales-data'),
    path('inventory_status/',views.inventory_status_func,name='inventory-status'),
    path('create_job/',views.create_job_func,name='create-job'),
    path('actual_create_job/',views.actual_create_job_func,name='actual-create-job'),
    path('show_job/<str:_jid>/',views.show_job_func,name='show-job'),
    path('assign_job/',views.assign_job_func,name='assign-job'),
    path('actual_assign_job/<str:_jid>/',views.actual_assign_job_func,name = 'actual-assign-job'),
    path('worker_main/',views.worker_main_func,name = 'worker-main'),
    path('save/',views.worker_main_save_job_api,name = 'save-job-api')
]
