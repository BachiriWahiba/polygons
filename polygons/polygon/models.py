from django.db import models
from django.core.validators import RegexValidator
from django.db.models.deletion import CASCADE
# from polygons.custom_fields import languageField , currencyField

# Create your models here.



class GeneralFields(models.Model):

    """ All the models below heritate from this model which contains the two common fields """

    created_at = models.DateTimeField(auto_now_add=True ,null=True, verbose_name="creation date")
    modified_at = models.DateTimeField(auto_now=True ,null=True, verbose_name="modification date")
    
    class Meta:
        abstract = True


class Provider(GeneralFields):

    """ Provider model  """

    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    CURRENCY_CHOICES = (
        ('DZD', 'DZD'),
        ('EUR', 'EUR'),
        ('USD', 'USD')
    )
    CURRENCY_DEFAULT = 'EUR'

    provider_name = models.CharField(max_length=50 , unique=True , blank=False , null=False ,verbose_name="provider name")
    email = models.EmailField(max_length=70 , blank=False , null=False , verbose_name="email")
    phone_number = models.CharField(max_length = 16 , unique=True ,validators=[phoneNumberRegex] , verbose_name="phone number")
    # language = models.CharField(max_length=100 , null=False , blank=False , verbose_name="Currency")
    currency = models.CharField(max_length=100 , choices=CURRENCY_CHOICES , default=CURRENCY_DEFAULT , null=False , blank=False , verbose_name="Currency")
    
    def __str__(self):
        return self.provider_name
    
