from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class CustomUser(AbstractUser):
    play_num = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    win_num = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    lose_num = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    draw_num = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    win_rate = models.FloatField(default=0.0)

    # Counts for each hand type
    stone_num = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    scissors_num = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    paper_num = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    # User profile image
    image = models.ImageField(upload_to='img/')

    def play(self, player_hand, com_hand):
        # Define the rules in a dictionary to improve readability and maintainability
        rules = {
            'stone': 'scissors',
            'scissors': 'paper',
            'paper': 'stone',
        }

        # Calculate the result
        if player_hand == com_hand:
            self.draw_num += 1
            result = 'draw'
        elif rules[player_hand] == com_hand:
            self.win_num += 1
            result = 'win'
        else:
            self.lose_num += 1
            result = 'lose'

        # Increment hand type count
        if player_hand in rules:
            setattr(self, f"{player_hand}_num", getattr(self, f"{player_hand}_num") + 1)

        # Update the play number and win rate
        self.play_num += 1
        if self.play_num > 0:
            self.win_rate = self.win_num / self.play_num * 100

        # Save the changes to the database
        self.save()

        return result