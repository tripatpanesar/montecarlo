# montecarlo
For DS 5100 final project
Creates muliple classes to simulate dies and die roll

## Installation
Use pip install to download the package and use it within your Python IDE.

## Usage
This package is to be used for personal use for the simulation of dice.

## Classes
There are 3 classes present: Die, Game, and Analyzer.

The Die class creates a die object and needs a NumPy array that describes the faces of a die. Die faces must be an integer or string. After the die is initialized, the weights of a certain face can be changed and updated. The die can be rolled within this class.

The Game class takes in one or multiple Die objects and plays a game. The Game class can roll any number of dies in a given number of rolls or plays. The game is then stored within a pandas data frame. This data frame can be called upon by the user to show the most recent roll

The Analyzer class takes in a Game object and runs analysis tests on it which is specified by the user. The class contains mulitple functions that can return jackpots, combinations, permutations, and face counts. Jackpots are defined as when the same face is rolled amongst multiple dice. Combinations and permutations are intuitive. Face counts returns the face and the respective number of counts for the game that is inputted within the class.

## Methods

For the Die class, there are 4 methods:  
```
    __init__(self, faces)  
        Initializes the die and takes in faces as np array.   
        Checks that faces are either integers or strings.   
        Die will be created with weight defaulting to 1.   
        Die returns as a pandas dataframe      
    change_weight(self, face, updated_weight)  
        Takes in updated weight and the face that needs the update.   
        Checks that the face inputted is present on the die  
        Will update the weight and update the die   
    roll(self, rolls=1)  
        The created die will run a 1 time (as default)  
        Number of rolls can be specified at input  
        Will return outcomes as a list  
    show_die(self)  
        Will return a copy and the state of the die
```  

For the Game class, there are 3 methods: 
```
    __init__(self, dice)  
        Initializes dice  
        Creates empty pandas dataframe to store rolls and plays    
    roll(self, num_rolls=1)  
        Rolls the dice, defaults to 1 roll  
        Stores the results in a private pandas dataframe   
    show_results(self, die_format='wide')  
        Takes in the previous data frame from roll function  
        Returns the dataframe to the user  
        Defaults to wide but can be specified for narrow
```  

For the Analyzer class, there are 5 methods: 
```
    __init__(self, game)  
        Initializes game  
        Checks to make sure inputted game is of game object  
    combo_count(self)  
        Calculates the total number of combinations in a game  
        Runs through using a lambda function  
        Returns the combos as a pandas dataframe with a column of counts  
    face_counts_per_roll(self)  
        Calculuates the number of times a face is rolled in a game  
        Runs through using a lambda function  
        returns the number of counts per face as an integer  
    jackpot(self)  
        Counts the number of jackpots present in the game  
        A jackpot is when all faces in a given roll are the same  
        Returns to the user the total number of jackpots   
    perm_count(self)  
        Calculates the total number of permutations in a game  
        Runs through using a lambda function  
        Returns the perms as a pandas dataframe with a column of counts
```

## Calling on Classes
Classes can be called. An example of a full run through is below:
```
die = Die(np.array([1,2,3,4,5,6]))  
game = Game([die, die, die, die])  
game.roll(1000)  
analysis = Analyzer(game)  
analysis.face_counts_per_roll()  
analysis.jackpot()  
  ```      

## Examples
This package and its functions can be used to simulate gambling games

## Contact Information
This was created as the final project for UVA Masters of Data Science - DS 5100. This project was created by Tripat Panesar (UVA MSDS 2024). Email: tp6mt@virginia.edu.


