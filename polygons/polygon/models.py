from django.db import models
from django.core.validators import RegexValidator
from django.db.models.deletion import CASCADE


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
    CURRENCY_DEFAULT = 'USD'

    LANGUAGE_CHOICES = (
        ('arabic', 'arabic'),
        ('english', 'english'),
        ('french', 'french'),
        ('spanish', 'spanish')
    )
    LANGUAGE_DEFAULT = 'english'

    provider_name = models.CharField(max_length=50 , unique=True , blank=False , null=False ,verbose_name="provider name")
    email = models.EmailField(max_length=70 , blank=False , null=False , verbose_name="email")
    phone_number = models.CharField(max_length = 16 , unique=True ,validators=[phoneNumberRegex] , verbose_name="phone number")
    language = models.CharField(max_length=10 , choices=LANGUAGE_CHOICES , default=LANGUAGE_DEFAULT , null=False , blank=False , verbose_name="language")
    currency = models.CharField(max_length=3 , choices=CURRENCY_CHOICES , default=CURRENCY_DEFAULT , null=False , blank=False , verbose_name="Currency")
    
    def __str__(self):
        return self.provider_name
    
class ServiceArea(GeneralFields):

    """ Service Area model  """  
    service_area_name = models.CharField(max_length=50, unique=True ,blank=False , null=False ,verbose_name="service area name")
    price = models.DecimalField(max_digits=10 , decimal_places=2 ,null=True, blank=True , verbose_name="Price")
    provider = models.ForeignKey(Provider , null=True , related_name="service_provider" ,on_delete=CASCADE , verbose_name="provider foreign key")
    geoinformation = models.JSONField()
    
    def __str__(self):
        return self.service_area_name



