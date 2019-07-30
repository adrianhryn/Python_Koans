from koans.game.about_extra_credit import *
from runner.koan import *


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