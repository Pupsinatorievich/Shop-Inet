from django.contrib import admin
from .models import Subscriber, SubscribersForms
# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
#    list_display = ["name", "email"]
    list_display = [fields.name for fields in Subscriber._meta.fields]
    fields = ["name"]
    list_filter = ["name","email"]
    search_fields = ["name"]
    
    
    class Meta:
        model = Subscriber

 
admin.site.register(Subscriber, SubscriberAdmin)















