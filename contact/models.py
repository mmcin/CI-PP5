from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length = 254)
    phone_number = models.IntegerField(max_length =30)
    subject = models.CharField(max_length = 254)
    message = models.CharField()

    def __str__(self):
        return self.name