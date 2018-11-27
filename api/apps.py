from django.apps import AppConfig
import random
from .models import Score

class ApiConfig(AppConfig):
    name = 'api'


class ScoreConfig(AppConfig):
    name = 'score'

    function Bowl():
        # look at the table to see what the last turn was
        # need to write a function that does getLastTurn
        turn = int(Score.getLastTurn()) + 1
        # Odd turns are the first of the frame
        if turn % 2 !== 0 && turn !== 23:
            pins = random.randint(1, 10)
            # need to display the number of pins
            # store the value of the pins for the turn
            # update cummulative_score

        # Even turns are the second of the frame, along with the bonus 3rd turn on the 10th frame
        if turn % 2 === 0 || turn === 23:
            if turn === 23:
                #confirm the previous two throws add up to 10
                # then continue, if not
            prev_pins = Score.getLastScore(turn)
            remaining_pins = random.randint(1, (10-prev_pins))
            # need to display the number of pins
            # store the value of the remaining_pins for the turn
            # update cummulative_score
        if turn > 23:
            # message about how they played a good game
