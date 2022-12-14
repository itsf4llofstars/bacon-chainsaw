#!/usr/bin/env python3
"""A roll of the dice simulator show outcomes
of dice used in a standard Vegas style craps game
"""
import random
import sys


class CrapsTable:
    def __init__(self, k_index: int = 1000):
        self.dice1 = 0
        self.dice2 = 0
        self.total = 0
        self.outcome = [1, 2, 3, 4, 5, 6]
        # self.dice_outcomes = random.choices(
        #     [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        #     [1 / 36, 1 / 18, 1 / 12, 1 / 9, 5 / 36, 1 / 6, 5 / 36, 1 / 9, 1 / 12, 1 / 18, 1 / 36],
        #     k=k_index)
        self.rolls = k_index
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
        return f'Rolls: {self.rolls} \
            \nCome out wins: {self.come_win}: {round(self.come_win / self.rolls, 3)} \
            \nSevens: {self.come_seven}: {round(self.come_seven / self.rolls, 3)} \
            \nYo 11\'s {self.yo}: {round(self.yo / self.rolls, 3)} \
            \nCome out Losses: {self.come_loss}: {round(self.come_loss / self.rolls, 3)} \
            \nCraps: {self.craps}: {round(self.craps / self.rolls, 3)} \
            \nSnake eyes: {self.snake_eyes}: {round(self.snake_eyes / self.rolls, 3)} \
            \nAce duece: {self.ace_duece}: {round(self.ace_duece / self.rolls, 3)} \
            \nBoxcars: {self.boxcars}: {round(self.boxcars / self.rolls, 3)} \
            \nPoints set: {self.points}: {round(self.points / self.rolls, 3)}'

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
    if not 1 < len(argvs) < 3:
        print('A single command line argument of the number of dice rolls to make must be passed.\n'
              'ex: python3 craps.py 10000\n')
        sys.exit()

    craps = CrapsTable(int(argvs[1]))

    try:
        for _ in range(int(argvs[1])):
            craps.roll_dice()
            craps.total_dice()
            craps.check_come_roll()
    except Exception as e:
        print(f'Log: {e}')
    else:
        print(craps)

    # print(craps.dice_outcomes)


if __name__ == '__main__':
    sys.exit(main(sys.argv))

