from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    question =  models.CharField(max_length=200)

    def __str__(self):
        return self.question + "-->" + ', '.join([c.choice for c in self.choices.all()])

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices')
    choice = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.question.question + "-->" + self.choice
