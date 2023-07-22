from django.contrib import admin
from contact_us import models



class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'sent_time', 'checked']
    list_editable= ['checked']
    list_filter  = ['name', 'checked']
    sortable_by  = ['checked', 'sent_time']

admin.site.register(models.Message,MessageAdmin)