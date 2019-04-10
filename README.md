# README project Combinatorial Game Theory
This project is the Implementation of GUI, Player and NegaMaxSolver for the Connect-4 Game.
Any harm is credited to the user not the creators

## Prerequisites
You have to install pygame library First to install pygame use the following command : 
```
python3 -m pip install -U pygame --user

```

## Running The code 
You have to Run the "world_vis.py" to Play the game.
To run the solver use "solver.py" or you can use "testbed.py" for directly solving your game position. 
Note that. 

```
First Player move number (Red DISK )   == 1
Second Player move number(Yellow DISK) == 2
Empty == 0

```
## world_vis.py
This python module handles the visualization of the Connect-4 game and also Player implementation. You should run this python program to play the game. 
note that you can change the depth of the Negamax player by changing the "solver_depth" variable. 

## Solver.py
This python module is used to solve the game positions. to use this you should first create a solver class. and then use the function to solve the board position. For Example : 

```
slvr = solver()
slvr.solve(board_mesh, 2, 7)
end = time.time()

```
or you can use "testbed.py". and just change the board_mesh and depth variable and player to evaluate number. 
## testbed.py 
This module is to test the solver. just change the board_mesh and depth variable and player to evaluate number.Remember that it takes a lot of time as the depth increases. 

## Built With
* [pygame](https://www.pygame.org/wiki/about) - Library is used to develope the GUI.

## Game ScreenShots

Picture Below Represents the Gameplay. 
![alt text](https://github.com/omidhajihassani/Connect-Four-Player-Solver-GUI/blob/master/Photos/Game.png)
In this game we have 4 kinds of players :   
1- Manual Player .  
2- Random Player .  
3- Greedy Player .  
4- Negamax Player ( depth = 10 ) .  
The players are shown in the following picture. 
![alt text](https://github.com/omidhajihassani/Connect-Four-Player-Solver-GUI/blob/master/Photos/Mode.png)
