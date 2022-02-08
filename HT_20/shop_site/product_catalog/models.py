from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        help_text='Enter the product category',
        verbose_name='Product category'
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        help_text='Enter the product name',
    )
    description = models.TextField(
        max_length=500,
        help_text='Enter the product description',
        verbose_name='Product description',
        null=True,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        help_text='Enter category product',
        verbose_name='Category product'
    )
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.name)])


class Status(models.Model):
    name = models.CharField(
        max_length=20,
        help_text='Enter product instance status',
        verbose_name='Product Instance Status',
        null=True
    )

    def __str__(self):
        return self.name


class ProductInstance(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        null=True
    )
    status = models.ForeignKey(
        'Status',
        on_delete=models.CASCADE,
        help_text='Change the state of an instance',
        verbose_name='Product Instance Status'
    )

    def __str__(self):
        return f'{self.product}, {self.status}'