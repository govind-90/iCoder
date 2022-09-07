from django.db import models
# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email

class handleSignup(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=15)
    pass1 = models.CharField(max_length=20)
    fname = models.CharField(max_length=10)
    lnamne = models.CharField(max_length=10)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
