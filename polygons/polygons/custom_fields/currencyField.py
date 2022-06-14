from django.db import models

class currencyField(models.CharField):

    def __init__(self, *args, **kwargs):

        CURRENCY_CHOICES = (
        ('DZD', 'DZD'),
        ('EUR', 'EUR'),
        ('USD', 'USD')
        )
        CURRENCY_DEFAULT = 'EUR'
        
        kwargs['max_length'] = 3
        kwargs['choices'] = CURRENCY_CHOICES
        kwargs['default'] = CURRENCY_DEFAULT
        
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs