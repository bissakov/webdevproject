from django.contrib import admin
from store.models import Consumer,Category,Product,Order,OrderProduct

class ConsumerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Consumer,ConsumerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product,ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order,OrderAdmin)

class OrderProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(OrderProduct,OrderProductAdmin)