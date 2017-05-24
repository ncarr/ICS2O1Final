# Turbulent Tailing
## ICS2O1 Final Project
#### Victor and Nicholas

## Proposal
We are making a car chase game where you avoid other cars, buildings, hydrants and occasional construction sites. The user will be able to accelerate and decelerate the car and have it change lanes. The car will stay in the same space at the bottom of the screen, but the background will move to make it look like the car is moving. There will be a main menu where the user can interact with the mouse or keyboard and it will have an option to learn to interact with the game. The user will interact in the game with the arrow keys. We will be using sprites in Pygame for graphics and the cars and obstacles will be randomly generated.

## Design
### Program Overview
Turbulent Tailing is a car chase game where the user must avoid obstacles such as oncoming traffic, traffic from intersecting roads and buildings along the side of the road. The user will be able to increase and decrease acceleration and steer with the arrow keys. The car will slowly decelerate and be captured if the user does not accelerate over time. The user could also become captured if they hit another car, veer off the road and crash, or run a red light. The game is kept interesting by randomly generated obstacles.

### Screen Layouts and Basic Input
We have a mockup of the basic application flow on [Adobe XD](https://xd.adobe.com/view/cea6190b-c634-4972-adbd-69d5ded2999b/).

### Description of Key Variables
#### Variables that keep track of the current game's state
timePassed - int - The number of frames that have been rendered in the current game. It will be used to calculate the score.

score - int - Number of points the user has in the current game.

speed - int - The number of pixels the background moves every frame.

cars - array - Keeps track of the co-ordinates of all the oncoming cars on the screen.

#### Each individual car object
x - The x coordinate of the car

y - The y coordinate of the car

### Program Plan
#### Show the main menu over a never-ending simulation of the game
 - Create the background and the cars
 - Display the text and buttons over the simulation
 - Read the high score from a file
 - Move cars slowly in the background
 - Occasionally move the car being chased, then don't display any oncoming cars in front of it

#### Display the help page


### Other Ideas
