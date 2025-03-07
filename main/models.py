from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.IntegerField(null=True)
    date_joined=models. DateField(null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Family(models.Model):
    father=models.ForeignKey(User,on_delete=models.CASCADE,related_name="father_of_families")
    mother=models.ForeignKey(User,on_delete=models.CASCADE,related_name="mother_f_families")
    family_name=models.CharField(max_length=50)
    child=models.ManyToManyField(User,related_name="child_of_families")
    
