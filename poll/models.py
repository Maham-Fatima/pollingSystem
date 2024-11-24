from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(("Publication date"))
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(("Choice"), max_length=100)
    votes = models.IntegerField(("Vote Count"))
    def __str__(self):
        return self.choice_text
    

class Voter(models.Model):
    name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=12)   
    def __str__(self):
        return self.name

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    models.BooleanField(("submitted"),default=False)
    def __str__(self):
        return f"{self.voter.name} voted on {self.question.question_text}"