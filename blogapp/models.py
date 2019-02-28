from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=45)
	image = models.FileField()
	content = models.TextField()
	created = models.DateTimeField(default=timezone.now)

	def get_absolute_url(self):
		return reverse('blogapp:index')

	def __str__(self):
		return self.title


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment = models.TextField()
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.comment
