# Pygame_Project

Game Description:
‘Jewel Guardian’ is an arcade game where you play as a character in a racecar whose goal it is to protect a jewel located in the middle of the screen from being touched by invading zombies that come into the screen from all angles at spontaneous times. You protect the jewel by driving the race car toward and making contact with the zombies which makes them disappear before they can touch the jewel. While you go after the zombies, there will be random stray bullets that travel across the screen horizontally in opposite directions every two seconds and at random altitudes. Your other objective is to dodge these bullets while you protect the jewel. The way the point system works is that you get five points every ten seconds you survive or protect the jewel and you get three points for every zombie you demolish. The main aim of the game is to get as many points as possible before the game ends, which is when the zombie is in contact with the jewel or you get hit by the bullet. At the end screen, there will be a “Game Over” text and another text that shows your final score for a number of seconds till the game quits. 

Controls:
UP arrow: Moves the car upwards.
DOWN arrow: Moves the car downwards.
LEFT arrow: Moves the car left.
RIGHT arrow: Moves the car right.
Combined arrow keys allow for diagonal movement eg. holding the UP and LEFT keys at the same time moves the car in a northwest direction.

Game Objects:

Player: 
This is the object you control which moves in different directions to collide with the enemies before they reach the jewel whilst evading the stray bullets. 
Contains an update method that updates the movement of the player when specific keys are pressed eg. if K_LEFT is pressed then there is a negative change in the x axis and the object would move to the left and it takes up a new position.

Enemy:
Enemies are created spontaneously using the random package on python. 
The multiple enemies that are actively trying to get the jewel are managed using a list. 
They are deleted from the screen when the Player object is in contact with them and hence deleted from the list entity. 
 
Bullet:
Bullets are spawned and shot every two seconds horizontally from either the left or right side of the screen and at random heights using the random.randint method.  

Jewel:
A stationary object in the middle of the screen represented by a jewel image.
If an enemy that comes towards it makes contact with the jewel object, the game ends.

References:

Pygame Help Contents. Pygame Front Page - pygame v2.6.0 documentation. (n.d.). https://www.pygame.org/docs/
GeeksforGeeks. (2024a, August 14). Pygame tutorial. https://www.geeksforgeeks.org/pygame-tutorial/
