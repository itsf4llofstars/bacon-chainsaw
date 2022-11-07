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
        self.boxcars = 0
        self.points = 0
        self.point = 0

    def __str__(self):
        return f'{self.dice1} {self.dice2} {self.total}\n{self.come_win = }\n{self.come_loss = }\n{self.craps = }\n{self.points = }\n{self.point = }'

    def roll_dice(self):
        self.dice1 = random.choice(self.outcome)
        self.dice2 = random.choice(self.outcome)

    def total_dice(self):
        self.total = self.dice1 + self.dice2

    def check_come_roll(self):
        if self.total == 2:
            self.snake_eyes += 1
            self.craps += 1
            self.come_loss += 1
        elif self.total == 3:
            self.ace_duece += 1
            self.come_loss += 1
            self.craps += 1
        elif self.total == 7:
            self.come_seven += 1
            self.come_win += 1
        elif self.total == 11:
            self.yo += 1
            self.come_win += 1
        elif self.total == 12:
            self.boxcars += 1
            self.craps == 1
            self.come_loss += 1
        else:
            self.points += 1
            self.point = self.total


def main(argvs):
    craps = CrapsTable()

    for _ in range(int(argvs[1])):
        craps.roll_dice()
        craps.total_dice()
        craps.check_come_roll()

    print(craps)


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))

