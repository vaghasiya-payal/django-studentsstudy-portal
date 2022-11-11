from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Notes)
class NotesModelAdmin(admin.ModelAdmin):
    list_display= ['user','title','description']

@admin.register(Homework)
class HomeworkModelAdmin(admin.ModelAdmin):
    list_display =['user','subject','title','description','due','is_finished']

@admin.register(Todo)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['user','title','is_finished']    