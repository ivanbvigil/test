from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
	image = models.ImageField(upload_to ='images/')
	title = models.CharField(max_length = 200)
	pub_date = models.DateTimeField()
	body = models.TextField(max_length = 1000)
	state = models.CharField(max_length = 6)
	author = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')
		