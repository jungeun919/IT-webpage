from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    @property
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()
