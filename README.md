# **Fall_Intensive_New_Version**

# What is this Cellular Automata?

This program is an example of a Cellular Automaton, a computational model that reflects complex patterns from simple rules and inputs, reflective of the process of evolution and other patterned phenomenon. 

## Installation Steps
1. Install the application by first installing pygame which can be done as: 

    pip install pygame 

This action is done in terminal

2. Download the files attached to the Github repository titled "Fall_Intensive_New_Version"

3. Open the files under VSCode as a python file

4. Press run once the code is displayed

5. To operate, press "R" to randomize the grid and provide a new automata. Press "S" to stop and continue the generations. Press "Q" to quit the program


## Program Steps

First, we imported sys, pygame, pygame.draw, and random to carry all the required functions for our code.  

Second, we begin by making a class which will carry the whole function of the application. 

This was done as:

    class CellularAutomata
    
Beneath it, we begin by defininig __init__ as an initialization of my pygame module, with all our required parameters. 
These parameters include:

    self, grid width, grid height, cell size, cell color when alive, cell color when dead, and maximum fps for refresh of generations
    
I as well initialized the grid within the __init__ function, and divided it into two grids: active and inactive

Next, I defined the function create_grid to generate randomly generated rows and columns to create a truly randomized pattern found in Cellular Automata

The following function, set_grid, allowed the zerioing of the grid, and helped determine according to rows and columns whether the grid was "active" or "inactive" 

The function afterwards, draw_grid, drew the cells onto the screen, previously cleared after each iteration (generation). These cells were represented as purple circles. 

Afterwards, clear_screen was defined to get rid of the previous game display. 

Get_cell function was created to find the state of the cell during the active grid, its properties found through Stack Overflow. This, cobined with cell_neighbors, retrieved the number of alive and dead neighbors to determine the "path" of the next generation according to the rules of Conway's Game of Life, which are as follows:

    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    
Update_generation was created to inspect the current active generation and update the inactive grid to store the next generation before looping out. This was aided by a helper function, inactive_grid, which indexed the active grids, and changed the active and inactive grids using algebra. 

Then, handle_events was defined to create inputs, such as "S" to stop and continue the game, "R" to randomize the grid, "Q" to quit. This was done using keydown, a component of pygame. 

Lastly, to pull it all together in the main game loop, simply defined as run, we created a clock ticker to set the maximum fps for the iterations, and a while loop to update the generations on the draw grid functions should game_over or paused ("S" or "Q") not be pressed. 





