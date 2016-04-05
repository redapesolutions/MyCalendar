from django.db import models

class Plans(models.Model):

	GENERAL = "ge"
	IMPORTANT = "im"
	
	possible = (
		(GENERAL, 'general'),
		(IMPORTANT, 'important'),
		)
		
	date = models.DateField()
	activity = models.CharField(max_length=128)
	description = models.TextField()
	significance = models.CharField(max_length=9, choices=possible, default = GENERAL)

	def __str__(self):
		return str(self.date)
