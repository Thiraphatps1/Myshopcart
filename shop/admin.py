from django.contrib import admin
from .models import Product ,Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display =['id','name','slug','image']
    list_editable=['name','slug','image']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display =['id','name','description','category','price','available','created','updated','image']
    list_editable=['price','name','description','category','available','image']
    prepopulated_fields={'slug':('name',)}
    list_per_page=20
admin.site.register(Product,ProductAdmin)