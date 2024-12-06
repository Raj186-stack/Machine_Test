# clients/admin.py
from django.contrib import admin
from .models import Client, Project

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'created_at', 'created_by')
    search_fields = ('client_name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'client', 'created_at', 'created_by')
    search_fields = ('project_name', 'client__client_name')
    filter_horizontal = ('users',)