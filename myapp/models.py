from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    #typo but already saved model. will come back
    data = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
