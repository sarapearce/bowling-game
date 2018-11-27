from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return '%s %s' % (self.name, self.message)


class Score(models.Model):
    turn = models.CharField(max_length=200)
    pins = models.CharField(max_length=200)
    cummulative_score = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return '%s %s' % (self.turn, self.pins, self.cummulative_score)
