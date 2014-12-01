from django.db import models

# Create your models(classes) here.
class Poll(models.Model):
	question = models.CharField(max_length=200)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    answer_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
