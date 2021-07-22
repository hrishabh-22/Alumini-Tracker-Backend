from django.db import models

# Create your models here.


class Project(models.Model):
    author = models.EmailField(max_length=254)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='project/', blank=True, null=True)
    github_url = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
