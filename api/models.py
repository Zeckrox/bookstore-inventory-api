from django.db import models
from django.core.validators import MinValueValidator
from api.custom_validators import validate_isbn
# Create your models here.
class Book(models.Model):
    title = models.CharField()
    author = models.CharField( )
    isbn = models.CharField( max_length=17, validators=[validate_isbn], unique=True )
    cost_usd = models.DecimalField( max_digits=4, decimal_places=2, validators=[MinValueValidator(0.01)] )
    selling_price_local = models.DecimalField( max_digits=4, decimal_places=2, null=True )
    stock_quantity = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.CharField( )
    supplier_country = models.CharField( )
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now=True )

    class Meta:
        ordering=["id"]

    def __str__(self):
        return f"{self.id} | {self.title}"