from django.db import models
#from api.user.models import CustomUser

# Create your models here.


class Article(models.Model):
    author = models.EmailField(max_length=254)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='article/', blank=True, null=True)
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
