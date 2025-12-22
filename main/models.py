from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDos(models.Model):
    owner=models.ForeignKey( User,on_delete=models.CASCADE,related_name='todos')
    
    class ExpAmount(models.IntegerChoices):
        low=15
        mid=25
        high=40

    exp = models.IntegerField(choices=ExpAmount.choices,default=ExpAmount.low)

    STATUS_CHOICES=[('waiting','Waiting'),
                    ('finished','Finished')]

    status=models.CharField(max_length=60,choices=STATUS_CHOICES,default='waiting')

    def __str__(self):
        return f"{self.owner.username} - {self.status} (+{self.exp}xp)"


class EXPS(models.Model):
    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name='exps')
    amount=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.owner.username}: {self.amount} XP"

