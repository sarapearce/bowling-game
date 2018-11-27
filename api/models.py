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
    player = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    function getLastTurn(self, player):
        # get the last turn number, given the player

    function getLastScore(self, turn, player):
        # get the last score given a player

    function getCummulative(self, turn, player):
        # get the cummulative score for the previous turn

    function getLastPins(self, turn, player):
        # get the number of pins that were knocked down previous turn

    function updateScore(self, turn, player, score, cummulative_score):
        # take a score model object and update the database

def __str__(self):
        return '%s %s' % (self.turn, self.pins, self.cummulative_score)
