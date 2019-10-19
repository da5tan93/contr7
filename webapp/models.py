from django.db import models

class Question(models.Model):
    poll = models.TextField(max_length=200, null=False)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    def __str__(self):
        return self.poll

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Answer(models.Model):
    quest = models.ForeignKey(Question, on_delete=models.CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)
    var_ch = models.ForeignKey(Choice, on_delete=models.CASCADE)