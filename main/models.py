from django.db import models

# Create your models here.
class SoftDeleteModel(models.Model):
    is_deleted=models.BooleanField(default=False)
    
    def soft_delete(self):
        self.is_deleted=True
        self.save()
    
    def restore(self):
        self.is_deleted=False
        self.save()
    
    class Meta:
        abstract=True


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class Users(SoftDeleteModel):
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.IntegerField(null=True)
    date_joined=models. DateField(null=True)
    objects=SoftDeleteManager()
    all_objects=models.Manager()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Family(models.Model):
    father=models.ForeignKey(Users,on_delete=models.SET_NULL,related_name="father_of_families",null=True,blank=True)
    mother=models.ForeignKey(Users,on_delete=models.SET_NULL,related_name="mother_f_families",null=True,blank=True)
    family_name=models.CharField(max_length=50)
    child=models.ManyToManyField(Users,related_name="child_of_families")
    
    def __str__(self):
        return self.family_name