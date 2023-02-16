from django.contrib import admin
from pgms_app.models import *
# Register your models here.
class adminview_model_register(admin.ModelAdmin):
	list_display=['uname','phone_number','address','registered']

admin.site.register(model_register,adminview_model_register)

class adminview_model_rent(admin.ModelAdmin):
	list_display=['uname','phone_number','amount','paid']

admin.site.register(model_rent,adminview_model_rent)