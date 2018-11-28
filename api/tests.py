from django.test import TestCase
from .models import Score


# Test the Scoring Model

class ScoreModelTests(TestCase):

    def the_second_score_should_be_within_remaining_pins(self):
        """
        Some comment that further elaborates what we are testing
        """

    def pins_should_return_a_value_less_than_11(self):
        """
        Some comment that further elaborates what we are testing
        """

    def cummulative_score_should_be_cummulative(self):
        """
        Some comment that further elaborates what we are testing
        """

    def previous_scores_should_be_for_correct_player(self):
        """
        Some comment that further elaborates what we are testing
        """

    def strike_score_should_add(self):
        """
        Some comment that further elaborates what we are testing
        """

    def spare_score_should_add(self):
        """
        Some comment that further elaborates what we are testing
        """




    # def test_was_published_recently_with_future_question(self):
    #     """
    #     was_published_recently() returns False for questions whose pub_date
    #     is in the future.
    #     """
    #     time = timezone.now() + datetime.timedelta(days=30)
    #     future_question = Question(pub_date=time)
    #     self.assertIs(future_question.was_published_recently(), False)
