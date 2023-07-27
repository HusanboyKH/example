from django.contrib import admin
from .models import TodoModel
from .forms import ToDoForms
class TodoAdmin(admin.ModelAdmin):
    form = ToDoForms
    list_display = ('task','note')
    search_fields = ('task',)
# Register your models here.
admin.site.register(TodoModel,TodoAdmin)

