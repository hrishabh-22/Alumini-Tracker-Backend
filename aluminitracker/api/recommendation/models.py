from django.db import models
from api.user.models import CustomUser

# Create your models here.


class Recommendation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, unique=True)
    java = models.IntegerField(default=0)
    python = models.IntegerField(default=0)
    javascript = models.IntegerField(default=0)

    def __str__(self):
        return self.user.email
