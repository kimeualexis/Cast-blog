from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=45)
	image = models.FileField()
	content = models.TextField()
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


class Comment(models.Model):
	comment = models.TextField()
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.comment
