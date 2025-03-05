from django.db import models

class Smartphone(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    memory = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='smartphone_images/')
    
    
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Smartphone'
    
    def __str__(self):
        return super().__str__()
    
    
    
    
    
