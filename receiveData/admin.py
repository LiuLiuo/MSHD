from django.contrib import admin
from django.contrib import admin

# Register your models here.
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered  # 获取app:api下所有的model得到一个生成器

app_models = apps.get_app_config('receiveData').get_models()
for model in app_models:
    admin.site.register(model)