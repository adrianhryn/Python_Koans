#!/usr/bin/env python
# -*- coding: utf-8 -*-

# EXTRA CREDIT:
#
# Create a program that will play the Greed Game.
# Rules for the game are in GREED_RULES.TXT.
#
# You already have a DiceSet class and score function you can use.
# Write a player class and a Game class to complete the project.  This
# is a free form assignment, so approach it however you desire.
import random
from runner.about_scoring_project import score


class Game:
    WINNING_SCORE = 3000

    def __init__(self):
        self.players = []
        self._is_game = None
        self.pause = False

    def add_player(self, player):
        self.players.append(player)

    def is_player_won(self):
        for i in self.players:
            if i.my_score >= self.WINNING_SCORE:
                return True
        return False

    def is_game(self, command=""):
        if self.pause:
            return False

        if command == "start":
            return True

        if command == "end":
            return False

        if self.is_player_won():
            return False
        else:
            return True

    def __str__(self):
        representation_of_the_game = ""
        for i in self.players:
            print(i)

        return ""


class Player:

    def __init__(self, name):
        super().__init__()
        self.trials = []
        self._score = 0
        self.name = name

    @property
    def my_score(self):
        self._score = self.__count_player_score()
        return self._score

    def roll(self):
        trial = [random.randint(1, 6) for _ in range(5)]
        if self.score_of_one_roll(trial) > 300:
            self.trials.append(trial)
        else:
            self.trials.append([])

        self._score = self.__count_player_score()

    def score_of_one_roll(self, roll):
        return score(roll)

    def __count_player_score(self):
        result = 0
        for i in self.trials:
            result += self.score_of_one_roll(i)

        return result

    def __str__(self):
        return "Player: {}, score: {}".format(self.name, self._score)


if __name__ == "__main__":

    game = Game()
    me = Player("Adrian")
    computer = Player("Computer")
    
    game.add_player(me)
    game.add_player(computer)

    count = 0
    play_game = game.is_game("start")
    while play_game:
        count += 1
        print(count, " ROLL")
        for i in game.players:
            i.roll()
            play_game = game.is_game()
            if not play_game:
                print("Player {} has {}, so the game continues for one last round".format(i.name, i.my_score))
                break

        if play_game:
            print("GAME STATS AFTER {} ROLL: ".format(count))
            print(game)
            print("___________________________________")

    for i in game.players:
        i.roll()
    print("")
    print("Stats after the final round: ")
    print(game)
    game.players.sort(key=lambda x: x.my_score, reverse=True)
    winner = game.players[0]
    print("winner is ", winner)

