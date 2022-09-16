from django.db import models

# Create your models here.
class Test(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="avatars", null=True, blank=True, verbose_name="Аватар")
