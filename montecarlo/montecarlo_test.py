import unittest
import numpy as np
from montecarlo import Die, Game, Analyzer 

class TestMethods(unittest.TestCase):
    
        
    def test_init_die(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        self.assertTrue(type(die), Die)        
        

    def test_change_weight(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        die.change_weight(1, 2)
        self.assertEqual(die.die.loc[1]['weights'], 2)

    def test_roll_single(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        rolls = die.roll(100)
        self.assertEqual(len(rolls), 100)
        self.assertTrue(all(roll in faces for roll in rolls))
        
    def test_init_game(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        game = Game(die)
        self.assertTrue(type(game), Game)      

    def test_game_creation(self):
        faces1 = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces1)
        faces2 = np.array(['A', 'B', 'C'])
        die2 = Die(faces2)
        game = Game([die1, die2])
        self.assertEqual(len(game.dice), 2)

    def test_roll_double(self):
        faces1 = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces1)
        faces2 = np.array(['A', 'B', 'C'])
        die2 = Die(faces2)
        game = Game([die1, die2])
        game.roll(10)
        self.assertEqual(game.play_df.shape, (10, 2))

    def test_show_results_wide(self):
        faces1 = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces1)
        faces2 = np.array(['A', 'B', 'C'])
        die2 = Die(faces2)
        game = Game([die1, die2])
        game.roll(5)
        results = game.show_results(die_format='wide')
        self.assertEqual(results.shape, (5, 2))
        
    def test_init_analyzer(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        game = Game(die)
        analyzer = Analyzer(game)
        self.assertTrue(type(analyzer), Analyzer)           

    def test_analyzer(self):
        faces1 = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces1)
        faces2 = np.array(['A', 'B', 'C'])
        die2 = Die(faces2)
        game = Game([die1, die2])
        analyzer = Analyzer(game)
        self.assertEqual(analyzer.game, game)

    def test_jackpot(self):
        faces = np.array([1, 1, 1, 1, 1])
        die = Die(faces)
        game = Game([die])
        game.roll(10)
        analyzer = Analyzer(game)
        self.assertEqual(analyzer.jackpot(), 10)
        
    def test_combo(self):
        faces = np.array([1,1])
        die = Die(faces)
        game = Game([die])
        game.roll(1000)
        analyzer = Analyzer(game)
        self.assertEqual(len(analyzer.combo_count()), 1)
        
    def test_perms(self):
        faces = np.array([1,2])
        die = Die(faces)
        game = Game([die])
        game.roll(1000)
        analyzer = Analyzer(game)
        self.assertEqual(len(analyzer.perm_count()), 2)        
        
        


if __name__ == '__main__':
    unittest.main(verbosity = 3)
