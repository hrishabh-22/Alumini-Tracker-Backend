from django.core.exceptions import RequestAborted
from django.db import models

# Create your models here.


class AllMessage(models.Model):
    sender = models.EmailField(max_length=254)
    receiver = models.EmailField(max_length=254)
    description = models.TextField()
    image = models.ImageField(upload_to='message/', blank=True, null=True)

    def __str__(self):
        return self.sender
