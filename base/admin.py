from django.contrib import admin
from .models import todolist
# Register your models here.
@admin.register(todolist)
class todolistadmin(admin.ModelAdmin):
    list_display = ('id','title','is_completed')
    list_filter = ('is_completed',)
    search_fields = ('title',)
    list_per_page = 5
    list_editable = ('title','is_completed')
    
 # admin.site.register(todolist,todolistadmin)