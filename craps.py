#!/usr/bin/env python3
"""A roll of the dice simulator show outcomes
of dice used in a standard Vegas style craps game
"""
import random


class CrapsTable:
    def __init__(self, k_index: int = 1000):
        self.dice1 = 0
        self.dice2 = 0
        self.total = 0
        self.outcome = [1, 2, 3, 4, 5, 6]
        self.dice_outcomes = random.choices(
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            [1 / 36, 1 / 18, 1 / 12, 1 / 9, 5 / 36, 1 / 6, 5 / 36, 1 / 9, 1 / 12, 1 / 18, 1 / 36],
            k=k_index)
        self.outcomes = []
        self.snake_eyes = 0
        self.ace_duece = 0
        self.come_win = 0
        self.yo = 0
        self.craps = 0
        self.come_loss = 0
        self.come_seven = 0
        self.points = 0
        self.point = 0

    def roll_dice(self):
        self.dice1 = random.choice(self.outcome)
        self.dice2 = random.choice(self.outcome)

    def total_dice(self):
        self.total = self.dice1 + self.dice2

