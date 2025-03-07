from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.IntegerField(null=True)
    date_joined=models. DateField(null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
