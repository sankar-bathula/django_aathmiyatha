from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
class Post(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(default='default.jpg', upload_to='home_posts')
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author =models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-details', kwargs={'pk':self.pk} )

	def save(self, force_insert=False, force_update=False, using=None):#got typeError while inserting register data
		"""This method is to resize the profile pic image"""
		super().save()
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
