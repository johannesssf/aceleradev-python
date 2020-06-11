from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from products.models import Product, Category


class CategoryModelAdmin(admin.ModelAdmin):

    def products(self, obj):
        href = reverse('admin:products_product_changelist') + f'?category={obj.pk}'
        return format_html(f'<a href="{href}">{ obj.products.count()} </a>')

    list_display = ('name', 'description', 'products')
    products.short_description = 'Produtos da Categoria'

class ProductModelAdmin(admin.ModelAdmin):
    
    def queryset(self, request, queryset):
        category = request.GET.get('category')
        if category:
            return queryset.filter(category__id=category)

        return category
    
    def formatted_price(self, obj):
        return f'{obj.price} R$'
    
    formatted_price.short_description = 'Preço'

    def link_category(self, obj):
        href = reverse('admin:products_category_change', args=(obj.category.pk,))
        return format_html(f'<a href="{href}">{obj.category.name}</a>')
    
    link_category.short_description = 'Categoria'
    
    list_display = ('name', 'formatted_price', 'description', 'link_category')


admin.site.register(Product, ProductModelAdmin)
admin.site.register(Category, CategoryModelAdmin)