from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField('date published')

class Choice(models.Model):
    #on_delete=models.CASCADE  để khi xóa 1 question thì các choice liên quan cũng bị xóa
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)