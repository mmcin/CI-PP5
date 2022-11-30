from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length = 254)
    phone_number = models.IntegerField()
    subject = models.CharField(max_length = 254)
    message = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name