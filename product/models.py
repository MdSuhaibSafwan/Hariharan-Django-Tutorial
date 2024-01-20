from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductManager(models.Manager):

	def startswith(self, name):
		queryset = self.get_queryset()	
		return queryset.filter(name__istartswith=name)

	def get_top_rated_product_for_index(self):
		queryset = self.all()
		return queryset

	# create functions home



class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.FloatField()

	def __str__(self):
		return self.name

	objects = ProductManager()

