

## Tripat Panesar
###  Project Classes for the dies, games, and analysis

import pandas as pd
import numpy as np


class Die:
    '''
    This class represents a single die
    
    Attributes:
    Takes in a np.array and creates a die
    If not specified, the weights will default to 1
    Can change or update the weights
    Returns a df of faces as the index and column of weights
    After die is intialized and created, die can be rolled
    Die can be shown with the most recent roll
    '''
    
    def __init__(self, faces):
        '''
        Initializes the die and takes in faces as np array
        Checks that the faces inputted are np array
        Checks that faces are either integers or strings
        Die will be created with weight defaulting to 1
        Die returns as a pandas dataframe
        '''
        
        # array of sides must be np array
        if not isinstance(faces, np.ndarray):
            raise TypeError('Must be an Numpy Array')
            
        if not (np.issubdtype(faces.dtype, np.number) or 
                np.issubdtype(faces.dtype, np.str_)):
            raise TypeError("Array must be numbers or strings")
        
           
        # create self variables for faces and weights    
        self.faces = faces    
        self.weights = np.full(len(faces),1)
        
        # create the die df
        self.die = pd.DataFrame({'weights': self.weights}, index = self.faces)
                
        
    # change weight of a certain face
    def change_weight(self, face, updated_weight):
        '''
        Takes in updated weight and the face that needs the update
        Checks that the face inputted is present on the die
        Will update the weight and update the die
        '''
        
        # see if face is in faces
        if face not in self.faces:
            raise IndexError('Face Value not found')
            
        index = np.where(self.faces == face)#[0][0]
        index_num = int(index[0])
        self.weights[index_num] = updated_weight
        self.die = pd.DataFrame({'weights': self.weights}, index = self.faces)
        

        
    def roll(self, rolls = 1):
        '''
        The created die will run a 1 time (as default)
        Number of rolls can be specified at input
        Will return outcomes as a list
        '''
        
        roll = np.random.choice(self.faces, rolls, 
                                   p = self.die['weights'] / np.sum(self.die['weights']))
        final_outcome = roll.tolist()
        return final_outcome
    
    
    def show_die(self):
        ''' 
        Will return a copy and the state of the die 
        '''
        
        die_copy = self.die.copy()
        return die_copy



class Game:
    '''    
    This class represents a game
        
    Attributes:
    Takes in a die or multiple die objects as a list
    Can roll a number of times, defaults to 1 roll
    Will show results when called upon, defaults to wide format, can specify for narrow
    Returns game object as a pandas dataframe
    '''
        

    def __init__(self, dice):
        ''' 
        Initializes dice
        Creates empty pandas dataframe to store rolls and plays
        '''
        
        self.dice = dice
        self.play_df = pd.DataFrame()

    def roll(self, num_rolls = 1):
        ''' 
        Rolls the dice, defaults to 1 roll
        Stores the results in a private pandas dataframe
        '''
        
        results = {}
        for index, die in enumerate(self.dice):
            results[f"Die_{index}"] = die.roll(num_rolls)
        
        self.play_df = pd.DataFrame(results)
                
    def show_results(self, die_format = 'wide'):
        ''' 
        Takes in the previous data frame from roll function
        Returns the dataframe to the user
        Defaults to wide but can be specified for narrow
        '''
        
        if die_format == 'wide':
            wide_df = self.play_df.copy()
            return wide_df
        
        elif die_format == "narrow":
            return self.play_df.melt(ignore_index=False, var_name="Die", value_name="Outcome")



class Analyzer:
    '''
    This class represents an Analyzer class
    
    Attributes:
    Takes in a game object from the game class
    Checks to make sure object is of the game class
    When specified, will count the total number of jackpots for a game
    Calculates the total number of instances of each face for a game
    Calculates total combinations of a game
    Calculates total permutations of a game
    '''
    
    def __init__(self, game):
        ''' 
        Initializes game
        Checks to make sure inputted game is of game object
        '''
        
        if not isinstance(game, Game):
            raise ValueError("Input must be a game object")
        self.game = game
        
    def jackpot(self):
        '''
        Counts the number of jackpots present in the game
        A jackpot is when all faces in a given roll are the same
        Returns to the user the total number of jackpots
        '''
        
        jackpots = 0
        for _, row in self.game.play_df.iterrows():
            if row.nunique() == 1:
                jackpots += 1
        return jackpots
        
    def face_counts_per_roll(self):
        ''' 
        Calculuates the number of times a face is rolled in a game
        Runs through using a lambda function
        returns the number of counts per face as an integer
        '''
        
        face_counts = self.game.play_df.apply(lambda x: x.value_counts()).fillna(0)
        face_counts = face_counts.astype(int)
        return face_counts

    def combo_count(self):
        ''' 
        Calculates the total number of combinations in a game
        Runs through using a lambda function
        Returns the combos as a pandas dataframe with a column of counts
        '''
        
        combos = self.game.play_df.apply(lambda x: tuple(sorted(x))).value_counts().reset_index()
        return combos

    def perm_count(self):
        ''' 
        Calculates the total number of permutations in a game
        Runs through using a lambda function
        Returns the perms as a pandas dataframe with a column of counts
        '''
        
        perms = self.game.play_df.apply(lambda x: tuple(x.tolist())).value_counts().reset_index()
        return perms






























