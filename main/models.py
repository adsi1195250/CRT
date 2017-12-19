from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Registrado(models.Model):
	nombre = models.CharField(max_length=100,blank=True,null=True)
	email=models.EmailField()
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__(self):

		return self.email
<<<<<<< HEAD
class asfsdfdfsRegistrado(models.Model):
=======
class Registrado(models.Model):
>>>>>>> be5201d19cb32ff6e7c75d2913996fe0aedfd2c5
	nombre = models.CharField(max_length=100,blank=True,null=True)
	email=models.EmailField()
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
