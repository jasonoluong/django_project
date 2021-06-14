from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) #cascade means if user is deleted then delete profile, but delete profile will not delete user
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kawrgs): #creating our own save method to scale saved image, *args, **kawrgs
		super().save( *args, **kawrgs) #runs the parent save method

		img = Image.open(self.image.path)

		if img.height> 300 or img.width > 300: #resize if condition is met
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)