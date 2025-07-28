from django.contrib import admin

# Register your models here.
from employer.models import *

class Poop(admin.ModelAdmin):
    list_display=['nom','email','poste','salaire']
admin.site.register(Employer,Poop)