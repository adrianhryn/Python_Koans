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

from runner.koan import *
from runner.about_dice_project import *
from runner.about_scoring_project import score


class Game:

    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def is_game(self):
        pass

    def __str__(self):
        representation_of_tha_game = ""
        for i in self.players:
            representation_of_tha_game += i + "\n"

        return representation_of_tha_game


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
        self.trials.append([random.randint(1, 6) for _ in range(5)])

    def score_of_one_roll(self, roll):
        return score(roll)

    def __count_player_score(self):
        result = 0
        for i in self.trials:
            result += self.score_of_one_roll(i)

        return result

    def __str__(self):
        return "Player: {}, score: {}".format(self.name, self._score)


class AboutExtraCredit(Koan):
    # Write tests here. If you need extra test classes add them to the
    # test suite in runner/path_to_enlightenment.py
    def test_game_class_created(self):
        game = Game()
        self.assertTrue(game)

    def test_game_add_player(self):
        game = Game()
        self.assertEqual(game.players, [])
        player = Player("Adrian")

        game.add_player(player)
        self.assertEqual(len(game.players), 1)

    def test_player_class(self):
        player = Player("Adrian")
        player.roll()
        player.my_score

    def test_scoring_function(self):
        """Scoring function from about_scoring_project.py"""

        player = Player("Adrian")

        self.assertEqual(0, player.score_of_one_roll([]))
        self.assertEqual(50, player.score_of_one_roll([5]))
        self.assertEqual(100, player.score_of_one_roll([1]))
        self.assertEqual(300, player.score_of_one_roll([1, 5, 5, 1]))
        self.assertEqual(0, player.score_of_one_roll([2, 3, 4, 6]))
        self.assertEqual(1000, player.score_of_one_roll([1, 1, 1]))
        self.assertEqual(200, player.score_of_one_roll([2, 2, 2]))
        self.assertEqual(300, player.score_of_one_roll([3, 3, 3]))
        self.assertEqual(400, player.score_of_one_roll([4, 4, 4]))
        self.assertEqual(500, player.score_of_one_roll([5, 5, 5]))
        self.assertEqual(600, player.score_of_one_roll([6, 6, 6]))
        self.assertEqual(250, player.score_of_one_roll([2, 5, 2, 2, 3]))
        self.assertEqual(550, player.score_of_one_roll([5, 5, 5, 5]))
        self.assertEqual(1150, player.score_of_one_roll([1, 1, 1, 5, 1]))
        self.assertEqual(300, player.score_of_one_roll([1, 2, 2, 2]))
        self.assertEqual(350, player.score_of_one_roll([1, 5, 2, 2, 2]))

    def test_count_player_score(self):
        player = Player("Adrian")

        player.trials = [[1, 5, 5, 1], [2, 3, 4, 6], [1, 1, 1], [2, 2, 2], [3, 3, 3]]
        self.assertEqual(player.my_score, 1800)


if __name__ == "__main__":

    game = Game()
    me = Player("Adrian")
    computer = Player("Computer")
    
    game.add_player(me)
    game.add_player(computer)

    print(game)
