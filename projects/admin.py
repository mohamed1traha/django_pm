from django.contrib import admin
from . import models 

# Register your models here.

admin.site.register(models.Category)

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['title','projectstatus','user','category','update_at']
    list_select_related=['category','user']
    list_editable=['projectstatus']

admin.site.register(models.Task)
