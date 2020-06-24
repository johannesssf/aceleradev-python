from django.db import models
from django.db.models import Q


class ProductManager(models.Manager):
    def with_text(self, text):
        queryset = self.get_queryset().filter(name__contains=text)
        return queryset

    def expensive_products(self):
        return self.get_queryset().filter(price__gte=100)

    def cheap_category(self):
        return self.get_queryset().filter(
            category__name='Category1 updated',
            price__lte=100
        )

    def category_or_expensive(self):
        query_filter = Q(category__name='Category1 updated') | Q(price__gte=100)
        queryset = self.get_queryset().filter(query_filter)
        print(queryset.query)
        return queryset


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')

    def __str__(self):
        return f"{self.name} - {self.products.count()}"


class Product(models.Model):
    objects = ProductManager()
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.deletion.DO_NOTHING,
        related_name='products')

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField('Nome do cliente', max_length=100)
    payment = models.CharField('Meio Pagamento', max_length=50)
    products = models.ManyToManyField(Product)

    @property
    def total_amount(self):
        total = sum([prod.price for prod in self.products.all()])
        print(">>>>>", total)
        return total

    def __str__(self):
        return f"{self.name} - {self.total_amount}"
