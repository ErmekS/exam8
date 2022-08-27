from django.contrib import admin


from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'category', 'product_description', 'created_time', 'updated_time', 'product_img']
    list_display_links = ['product_description']
    list_filter = ['product_name', 'category']
    search_fields = ['category']
    fields = ['product_name', 'product_description', 'category', 'created_time', 'updated_time', 'product_img']
    readonly_fields = ['created_time', 'updated_time']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
