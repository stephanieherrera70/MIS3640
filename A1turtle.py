#With the help of the designated commands within the packages, the turtle commands helped calculate the distance for a person.
#Given this, this problem solves 3 and 4 of the assignment.

#Calling the packages that contains the commands within the packages. 
import turtle
import random 

def drunkard_walk(ind_distance, turns): #Defininf the function, the individual distance the "drunkward" takes with the amount of turns.
    '''The whole function is figuring out the location it takes from the starting point. The person continues to randomly select which direction
    they want to go to. The function calculates the distance it travels after their amount of steps and turns. '''
    distance = 0 #Given that the individual will have a starting point of 0 distance because they have not moved. I am trying to figure out how long they went from 0 movement.
    for i in range(turns): #This is a loop that will continuosly run each movement in the amount of turns the individual person takes.
        turtle.setheading(90 * random.randint(0, 3)) #Turtle allows the computer to draw the indidvidual's walk. 
        #Setheading allows the individual to choose where he would want to go, with a given angle. The person has an orentation of 90 degree times the direction one takes. If it is 0, then it will be on the x-axis from left to right or right to left.
        turtle.forward(ind_distance) #This allows the person to move on the screen and go forward by a spcificed distance, in the direction the turle is headed.
        distance = distance + ind_distance #This calculates the distance the person took through his "drunken" walk after one turn and then another turn. With the loop, it calculates the distance in steps and continues to add the turns and steps the person took through the whole entire time until the turns are completed. 
    return distance #This will give you the entire distance of the "drunken" wlak.


print(drunkard_walk(30,17)) #You turned 17 time and everytime you turned, you would take 30 steps. This print function, will allow the whole function to run.  