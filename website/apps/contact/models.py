from django.db import models



class ContactData(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name