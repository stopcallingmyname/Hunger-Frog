> INTRODUCTION

In this course project, the creation of the author's computer game "Hunger Frog" is implemented. A computer game is a computer program that serves to organize the game process (gameplay), communicate with game partners, or itself acts as a partner. This is a game in which the user, while playing, deals with a set of graphics,
images or even audio that make the game more interactive and interesting.
Playing computer games and creating them are two different things. Creating a game is a time-consuming process and often requires an entire development team to write.
If we are talking about small projects, for the implementation of which sometimes one developer is enough,
then Python is the ideal language for them. The only reason why there are few games in Python is that the professional game development industry almost exclusively uses C++ or C#, which in turn is due to a combination of performance issues and reliance on legacy code.
Programming is based on the use of programming languages ​​in which instructions for a computer are written. Modern applications contain many such instructions linked together. The purpose of this course work is to create a computer game "Hunger Frog" using the Python programming language.

> Terms of reference for the development and / or scenario of the game "Hunger Frog"

Hunger Frog is an author's game based on maintaining the so-called "satiation" of the frog. "Hunger Frog" is a 2D arcade game built around "eating" downed mosquitoes, thereby keeping the frog "satiated".
The random location and flight path of the opponents, combined with the time it takes to reduce hunger units by one unit every two seconds, makes the game more difficult than it seems at first glance, and to maintain interest in the game, the points system gives the user the opportunity to challenge himself.
The player can jump and move horizontally for a more comfortable "hunt" for mosquitoes. In order to hit the enemy, it is enough to hit him with the character's tongue, which is controlled by the left mouse button. Try to hit the mosquitoes with the tip of your tongue while holding LMB or "shoot" your tongue at each - it's up to you.
After hitting the target, the mosquito will begin to fall until it reaches the bottom of the ocean or the grass cover on the island, or is eaten by a frog. If at the same time the “prey” is not caught by the main character, the hunger unit will not increase, and only one point will be added to the score. In the case of a successful capture of "prey",
the player gets one hunger point and a nice bonus of ten points.
The game ends if the player fails to keep the frog's hunger normal or falls into the bottomless ocean. The player receives points for each downed or eaten mosquito, so his task is to hold out as long as possible,
in order to get as many points as possible.
The game cannot be won: the goal of the game is to get the maximum number of points.
Also, the game has a best result counter, which shows the best result for the entire time of the game, which encourages the player to improve himself.
The game ends then
when the number of hunger points is equal to zero or the character falls into the ocean.
 This game is designed for a children's audience, as it includes several developmental factors at once:
• Logic - the ability to analyze the situation and quickly apply appropriate solutions;
• Ability to calculate one's actions several steps ahead;
• Concentration - the ability to keep attention on solving a specific problem for a long time;
• Improving spatial skills;

> Modeling and software design

To implement this course project, such software modules as: sys, pygame, random, math and time were used.
Mostly in the course project, the pygame library was used, on the basis of which the project was written.
The random library is used to form the direction of movement of opponents when they appear.
The time library is used to animate "sprites" and also as a "hunger" counter.
The “Game” module contains all the classes used in the game: Player, Enemy, Background, Water, World, Button, Decorations.
The “Debug” module contains methods for rendering (drawing) the game interface.
The “HungerFrog” module is the main module that contains the main loop with the game logic.
Also in the project folder are folders: “SFX”, which contains all the sounds and music, the “Fonts” folder, which stores the fonts used in the game window, the “Sprites” folder,
which contains all the sprites of the game, as well as a text file that records the highest score in the game (TopScore.txt).
For a more detailed study of the structure of the program, a UML class diagram was compiled (see Picture 1).
[Picture 1]
![image](https://user-images.githubusercontent.com/56963796/200644200-9bd70dfa-2a13-40a0-962e-200a92924859.png)

> Software Implementation
As described earlier, we use 6 classes: "Player", "Enemy", "Background", "Water", "World", "Button" and "Decorations". Each class describes the corresponding methods for organizing the work of the application. Let's consider each method in more detail.
    Methods of the “World” class:
__init__() is a special method,
which is automatically executed when a new instance is created;
Reset () - responsible for resetting parameters for objects of this class;
Draw () - is responsible for drawing objects of the World class.

Methods of the “Water” class:
__init__ () is a special method that is automatically executed when a new instance is created;
Reset () - responsible for resetting parameters for objects of this class;
update_animation () - responsible for updating the animation of sprites;
Draw () - is responsible for drawing objects of the Water class.

Methods of the “Decorations” class:
__init__ () is a special method that is automatically executed when a new instance is created;
Reset () - responsible for resetting parameters for objects of this class;
Draw() - responsible for drawing objects of the Decorations class.

Methods of the "Background" class:
__init__ () is a special method that is automatically executed when a new instance is created;
Reset () - responsible for resetting parameters for objects of this class;
update_animation () - responsible for updating the animation of sprites;
Draw() - is responsible for drawing objects of the Background class.

Methods of the “Player” class:
__init__ () is a special method that is automatically executed when a new instance is created;
Reset () - responsible for resetting parameters for objects of this class;
update_animation () - responsible for updating the animation of sprites;
Draw() - responsible for drawing objects of the Player class.
update_tongue() - responsible for updating the animation of the character's language;
Update () - responsible for the movement of the character, checks for his collision with objects in the world and falling enemies.

Methods of the “Enemy” class:
__init__ () is a special method that is automatically executed when a new instance is created;
Reset () - responsible for resetting parameters for objects of this class;
move () - responsible for the movement of opponents;
ai () - is responsible for the direction of the side of movement of opponents;
update_animation () - responsible for updating the animation of sprites;
Update () - responsible for rendering objects of the Enemy class;
Collider () - responsible for checking the collision of objects of this class with the language of the character.

Methods of the "Button" class:
__init__ () is a special method that is automatically executed when a new instance is created;
Draw () - is responsible for drawing objects of the Button class and checks for a collision of the object with the mouse, it also contains the button animation logic.

When the application is launched, a game window appears, in the center of the screen there is a game menu (see Picture 2), in which the user can: start the game by pressing the “Play” button,
read a brief tour of the game in the information menu (see Picture 3), when you press the “Info” button, also from the information menu section, the user will have access to a button to start the game process. And finally, exit the game by pressing the “Exit” button.
Game process:
When starting the level, the user observes the island,
located in the center of the screen, the character (frog), which he will control in the future, as well as his opponents (mosquitoes), who move randomly at the top of the screen. Management is implemented using the A, D and space keys, to attack you must press the left mouse button (LMB).
The user interface is: a hunger counter, a points counter, and a counter for the best result for all time in the game. Interface elements are located in the upper left corner of the game window.

[Picture 2]
![image](https://user-images.githubusercontent.com/56963796/200644950-e224f156-276b-4986-87a4-588c5af40926.png)

[Picture 3]
![image](https://user-images.githubusercontent.com/56963796/200645032-14b7430e-35d2-4688-acd8-ac5e09e3a6ec.png)

> Software deployment and testing
The essence of the game is to get the most points, for which, in turn, it is necessary to maintain the "satiation" of the character, collecting defeated opponents during their fall, which, when they disappear, give us bonus points and one unit of "hunger" (see Picture 4). If the falling opponent was not caught, the unit of "hunger" is not replenished,
and only one point will be added to the score,
By pressing the A and D keys, the character moves left and right respectively, we can also jump by pressing the Space key.
When you start the gameplay, we see a small island in the ocean, the character himself and opponents in the form of mosquitoes flying randomly in the sky.
The upper left corner shows the number of current hunger units, the current score and the best result of passing the game all the time.

[Picture 4]
![image](https://user-images.githubusercontent.com/56963796/200645315-ef01c164-a0d4-469e-b001-aedbec28807c.png)

The highest score is recorded in the TopScore.txt file and is overwritten if the player manages to break this record by scoring more points.
When catching a defeated enemy, additional points are assigned (10 units), the SCORE and TOP SCORE values are changed, since the SCORE value is greater than the original TOP SCORE value.
Also, when you exit the game, the TopScore.txt file will be overwritten.

The game has no time limit and will continue until the player loses all "hunger" units or goes to feed the fish by falling into the ocean. At the end of the game, a window appears that prompts us to restart the game by pressing the “Play” button or exit to the main menu by pressing the “Menu” button. (See Picture 5).
[Picture 5]
![image](https://user-images.githubusercontent.com/56963796/200645925-1eab08ed-d9cc-4a4f-915f-fadbc39a3405.png)

> CONCLUSION

In the course project, a program was written and debugged, which is the game "Hunger Frog", written in Python using the Pygame module.
In the process of working and debugging the project, new methods of work related to the development of windows, fonts, and sounds were studied. The drawing of objects, the creation of a game window,
methods of working with the keyboard are considered in detail. Techniques for developing easily scalable code have been studied.
The game has been successfully tested.
This game is copyrighted, the mechanics of the game was developed and invented by me personally. All matches are random. The game can be optimized for any platform, as well as modernized at the request of the consumer, for example
, change the level design or the "skin" of characters, add additional difficulty levels, from which the timer for reducing "hunger" units will change, and create various additional conditions for a variety of gameplay.





