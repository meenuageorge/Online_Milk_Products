
from django.contrib import admin
from .models import Post,Vaccine,Eartag,NewEartag,MilkRecord,Customer,Product,Orders
class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)

class VaccineAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vaccine, VaccineAdmin)

class EartagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Eartag, EartagAdmin)

class NewEartagAdmin(admin.ModelAdmin):
    pass


admin.site.register(NewEartag, NewEartagAdmin)

class MilkRecordAdmin(admin.ModelAdmin):
    pass


admin.site.register(MilkRecord, MilkRecordAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Orders, OrderAdmin)