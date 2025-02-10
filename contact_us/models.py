from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    problem = models.TextField()

    class Meta:
        verbose_name_plural = "Contact Us"
    def __str__(self):
        return self.name