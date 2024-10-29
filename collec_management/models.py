from django.db import models

# Create your models here.
class Collec  (models.Model ) :
    title = models.CharField ( max_length =100, null=False)
    description = models.TextField (null=False)
    date = models.DateTimeField (auto_now_add=True, null=False)

def __str__ (self) :
     return self . title