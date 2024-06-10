from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'action_taken','address' ]
    list_filter = ('category','action_taken',)
    