from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError

def validate_isbn(isbn):
    #Validamos si tiene el formato valido de 10 o 13 caracteres sin contar las "-".
    allowed_lengths = [10, 13]
    no_dashes = "".join(c for c in isbn if c != "-")
    if len(no_dashes) not in allowed_lengths:
        raise ValidationError(("Invalid format for isbn"))
    
    #Validamos que sea unico en la BDD sin importar los "-".
    regex = r''.join(f'{c}[-]?' for c in isbn)
    # Revisamos si existe un isbn con los mismos digitos que no sea el mismo.
    if(Book.objects.filter(isbn__iregex=regex).exclude(isbn=isbn).count() > 0):
        raise ValidationError(("book with this isbn already exists."))

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    author = models.CharField( )
    isbn = models.CharField( max_length=17, validators=[validate_isbn], unique=True )
    cost_usd = models.FloatField( validators=[MinValueValidator(0.01)] )
    selling_price_local = models.FloatField( null=True )
    stock_quantity = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.CharField( )
    supplier_country = models.CharField( validators=[MinLengthValidator(2), MaxLengthValidator(2)] )
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now=True )

    class Meta:
        ordering=["id"]

    def __str__(self):
        return f"{self.id} | {self.title}"



