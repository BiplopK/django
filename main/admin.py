from django.contrib import admin
from .models import Users,Family
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','phone','date_joined']
admin.site.register(Users,UserAdmin)
admin.site.register(Family)
