from django.db import models

class Product(models.Model):
   title       = models.CharField(max_length=120)
   slug        = models.SlugField(unique=True) 
   stock       = models.IntegerField(blank=False)
   feature_1   = models.CharField(max_length=220, null=True, blank=True)
   feature_2   = models.CharField(max_length=220, null=True, blank=True)
   feature_3   = models.CharField(max_length=220, null=True, blank=True)
   content     = models.TextField(null=True, blank=True)
   price       = models.DecimalField(max_digits=6, decimal_places=2)

   def __str__(self):
          return self.title

   def get_absolute_url(self):
          return f"{self.slug}"
   
