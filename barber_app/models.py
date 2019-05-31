from django.db import models

# Create your models here.
class Member(models.Model):
	member_id = models.CharField(max_length=10)
	name = models.CharField(max_length=10)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text