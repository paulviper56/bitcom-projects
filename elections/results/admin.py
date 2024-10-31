from django.contrib import admin
from django.apps import apps
from . import models

# Register your models here.
app = apps.get_app_config('results')
for model in app.get_models():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass