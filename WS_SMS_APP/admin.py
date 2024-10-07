from django.contrib import admin
from .models import RoomModel
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    
    class Meta:
        model = RoomModel
        
admin.site.register(RoomModel,RoomAdmin)