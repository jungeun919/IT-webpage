from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    

class Choice(models.Model):
    q = models.ForeignKey(Question, on_delete=models.CASCADE)
    select = models.CharField(max_length=100)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.q, self.select