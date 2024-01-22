from django.db import models

# django.contrib.auth.models

from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser


class UserManager(BaseUserManager):
	
	def _create_user(self, email, password):
		email = self.normalize_email(email)  # normalizing our email
		user = self.model(email=email)  # User(username=aasdasd, email=asas)
		user.set_password(password)  # it hashes our password from 1234 to hash
		user.save(using=self._db)  # when creating an instance from any manager we use using=self._db

		return user

	def create_user(self, email, password):
		user = self._create_user(email, password)
		# user.is_superuser = True
		user.is_active = True
		# user.is_admin = True
		user.save()
		return user		

	def create_superuser(self, email, password):
		user = self.create_user(email, password)
		user.is_superuser = True
		user.is_active = True
		user.is_admin = True
		user.save()
		return user


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True, )
	first_name = models.CharField(max_length=100, null=True)
	middle_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=100, null=True)
	address = models.TextField(null=True)
	phone_number = models.CharField(max_length=16, null=True)

	is_superuser = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	USERNAME_FIELD = "email"  # user can log in with this field
	REQUIRED_FIELD = "email"
	EMAIL_FIELD = "email"

	def __str__(self):
		return self.email

	objects = UserManager()

	@property
	def is_staff(self):  # it's an attribute but not a function
		return self.is_admin
	



