from django.apps import AppConfig
import random
from .models import Score

class ApiConfig(AppConfig):
    name = 'api'


class ScoreConfig(AppConfig):
    name = 'score'

    def getPlayer(self):
        # return the value of an input??

    def checkForStrikeSpare(self, turn, player, pins):
        # find if there was a strike or spare in the previous frame

        # We had a strike in the last frame, adjust the score
        if pins === 10:
            # confirm with rules that you get additional 20
            bonus_score = 20

        # Need to write a case for a spare

        return bonus_score

    def Bowl(self):
        player = self.getPlayer()
        turn = int(Score.getLastTurn(player)) + 1
        previous_turn_pins = Score.getLastScore(turn, player)

        # Odd turns are the first of the frame
        if turn % 2 !== 0 && turn !== 23:
            pins = random.randint(1, 10)

            if previous_turn_pins === 10:
                bonus_score = self.checkForStrikeSpare(turn, player)

        # Even turns are the second of the frame, along with the bonus 3rd turn on the 10th frame
        if turn % 2 === 0 || turn === 23:
            # if turn === 23:
                #confirm the previous two throws add up to 10
                # then continue, if not, throw a message
            if previous_turn_pins === 10:
                score = 0

            remaining_pins = random.randint(1, (10-previous_turn_pins))

            # We have a spare, this is not handled yet
            if previous_turn_pins + remaining_pins === 10:
                score = remaining_pins

        if turn > 23:
            # message about how they played a good game

        # need to update the view with the number of pins
        current_cummulative = Score.getCummulative(turn, player)
        cummulative_score = current_cummulative + score

        Score.updateScore(turn, player, score, cummulative_score)
