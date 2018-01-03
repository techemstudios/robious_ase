# Lucille Brown: Game Design - NextUp   

May be worthwhile to consider Hyperpad/Design Thinking lessons. In general, students want quick results and have a difficult time typing.  

Initial outline will hold a series of pygame walkthroughs, for individual arcade-style games written in Python; and general coding in Python walkthroughs. The [Python code walkthroughs](https://github.com/techemstudios/nextup_lucille/tree/master/game_design/python_walkthroughs) will help students understand core concepts in programming: Data Types, variables, loops, conditionals, functions, object-oriented design/programming, using modules/dependencies. All of which, and more are found in games developed with pygame.  

## Pygame Walkthroughs  

The handouts for the following Pygame walkthroughs can be found in the directory, [pygame_walkthroughs](https://github.com/techemstudios/nextup_lucille/tree/master/game_design/pygame_walkthroughs). In each repo, there is a python file with the name of game, where sections of code are missing (highlighted with comments to outline each section and what the section adds to the game). Intructors will walkthrough the missing code, explaining what to add and what the section(s) do for the game. Each repo has a source.py, which has the complete code for the game and can be used for referenece by the instructor if the student(s) code errors are to difficult to get past.  

### Pygame Repositories  
#### Complemented with Pygame Walkthroughs (Above)  

*Instructions*: clone the repo before class onto each chromebook/each student's directory. Use the printed out pdfs that walk through the missing sections of code for each. Print more if necessary from the "pygame_walkthroughs" directory (link above).  

* [wormy](https://github.com/joetechem/wormy_rasp)  
* [pong](https://github.com/joetechem/pong/tree/master/pong-pygame/pong)
* [frogger](https://github.com/joetechem/frogger)
* [pacman](https://github.com/joetechem/pacman-python-mirror)
* [spaceshooter](https://github.com/joetechem/pygame_tutorials)
* [alien invasion](https://github.com/joetechem/alien_invasion/tree/master/alien_invade)

### Introductions

* Name
* Age
* Grade
* Experience
  - Any programming/coding experience?  

*note* below is a simple Hello World program conducted with Pygame. Previously, this exercise has not been carried out in previous classes, but will be tested during the Fall 2017 session.  

# OOP  

Dice game, before pygame intro?  

## Starting Pygame  

Pygame is part of the Python framework including tools to create video games. What does Pygame have, that allows us to do create games? It is built on top of the Simple Direct Media Layer (SDL), a C framework which gives access to a range of graphics, sounds, keyboard handlers, and other input devices on various operating systems including Linux, MAC OS X, and Windows. -*Instant Pygame for Python Game Development, Ivan Idris*  

### Hello World! (Pygame Style)  

* Objectives  
  - Main Game Loop  
  - Render Text  
  - Surface Object  
  - Quit Event  

#### Dependencies  

#### Initialization  

#### The Main Game Loop  
```python    
# importing dependencies
import pygame, sys
from pygame.locals import *

# initialize
pygame.init()

# window width, height --> units = pixels
screen = pygame.display.set_mode((400, 300))

# window caption
pygame.display.set_caption('Hello World!')

# the main game loop
while True:
    sys_font = pygame.font.SysFont("None", 19)
    rendered = sys_font.render('Hello World', 0, (255, 100, 100))
    # the blit() method, draws items to the surface
    screen.blit(rendered, (100, 100))

    # the quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
```  

### Pygame Walkthrough: [Wormy](https://github.com/joetechem/wormy_rasp)  

Fill in the missing code. Explain dependencies, how we use pygame by `import`, discuss how computers handle and display, or represent colors, by using Red, Green, and Blue values (RGB). The retinas of our eyes have three types of photoreceptor cone cells that respond to frequencies of light, categorized into RGB. Similar to painting, we increase/decrease the amount of the three categories to have the computer represent different colors. After using one of the already defined colors as the background color (in Part Two of missing python code), challenge the class to registers their own unique color as a new variable and use as the background color.  

Check out some of the color representations below:   

| Red |Green|Blue | Color |
|-------------------------|
| 0   | 0   | 0   | black |
| 255 | 255 | 255 | white |
| 255 | 255 | 0   | yellow|
| 255 | 130 | 255 | pink  |
| 146 | 81  | 0   | brown |
| 157 | 95  | 82  | purple|
| 140 | 0   | 0   | maroon|  

#### Core Computer Science Concepts

* Computational Thinking
  * Decomposition
    - Decompose: break down: divide & conquer
    - Break down a problem into smaller problems
  * Generalize
    - Be able to see the big picture
    - See how the smaller tasks make up the larger task
  * Recognize Patterns
    - Look for familiar things
    - Be able to see parts that repeat
    - Don't Repeat Yourself --> **DRY**
  * Algorithm Design
    - Make a plan to tackle the problem
    - Carry out the plan


* Abstraction
  * Mental model, or way to think about something
    - Focus on what needs to be done in the moment
    - Leave only the information we need, to complete our goal


* Object Oriented Programming
  * OOP or OOD
    - Everything is an object having its own, or similar properties to other objects
    - Each object belongs to a *class*


* Development Process
**Write Simple Programs**
  * Take a systematic approach to create useful programs
    1. Analysis
    2. Specifications/guidelines
    3. Design it
    4. Implement it
    5. Test/debug it
    6. Maintain it

### How to Think
#### Like a Computer Scientist
*10 min*

Take a problem that at first, may seem overwhelming, or not "attackable" with a program, then break the problem into smaller manageable problems where we can use computation to solve. See how the smaller problems together make up the larger one. Think about computational thinking as useful ways to approach and solve problems using these steps: decomposition, generalization, recognize patterns, make plan (or algorithm) and carry it out.

Example, Clean the Whole House problem.

### What is Computer Science

Not just the study of computers. Really, it is the study of what can be computed. A major part of computer science is to design a solution, or step-by-step process for reaching a goal, design an algorithm, much like designing a recipe. And more...

### What are Computers?

Computers today, are devices that store and manipulate information and can do this because of programs. When we put info into a computer, it transforms the info into new, useful forms. Computer can then output or display the information we put into it.

### Quick Computer History

*10 min*

How far we've come. Early computers were tools (or mechanical devices) people used to help them calculate math problems. A modern computer is a device that can be programmed to perform a task. From Talley Sticks, to the Babbage Machine --end with Ada Lovelace, recognized as the first computer programmer.

Difference between hardware and software.

### What is a Computer Program?

*5 min*

Simply a set of instructions written by humans that causes the computer to perform some action. Coding and programming are synonymous.

Discuss difference between Hardware and Software.

### Out-of-Seat Programming Exercise

*5 - 10 min*

Pick four volunteers to form two groups. Each group has a designated programmer and robot. Have each group stand in same area of the classroom. Point out a place in the room to be a destination. Explain that the programmer needs to give their robot step-by-step to get to the destination by telling the robot to walk forward (x amount of steps) or turn (90 degrees, left or right). The robot can only follow the directions given by their programmer.

                  Go Forward 3 steps
                  Turn left 90 degrees
                  Go forward 5 steps
                  etc.

Ask the class, which group was more efficient (the least amount of steps).

***

## Code

*5 min*

Code lets you communicate! In general, *code* is a system for transferring information. People use code to communicate with another, and between a person and a machine. Examples:

* Morse
  - light (flashlights, sun & mirrors, etc.)
  - sound
  - dots & dashes (telegraph machines)
* Braille
* Human Languages
  - sign
  - speech
  - written
  - shorthand (stenography)
* Computer languages


### How Computers Manage Information

*10 min*

Computers *speak* using binary; where only the digits 0 and 1 are used. Zero is "coded" to mean OFF, one is "coded" to mean ON. Relate to a light switch.

Use the whiteboard to explain how computers translate numbers we use, decimal number system into the binary number system --by explaining the difference between the two by focusing on the place values.

Decimal numbers use a **Base 10** system, meaning it uses a total of ten digits:

                    0 1 2 3 4 5 6 7 8 9

Binary numbers use a Base 2 system, two digits:

                    0 1

### Binary Flashcards

*10 min*

An all class activity to visually see how the binary number system operates by practicing a method that converts decimal numbers to binary. Ask for five volunteers. Give each volunteer a big binary flashcard (dark side of cards facing the class). Arrange the students to be in correct place value order. Write the number one on the board, use the cards and input from the class to have each volunteer flip the correct cards (turn "ON") to collectively show the number, one in binary. Do this for the numbers, 2 - 10. The class should progressively get quicker.

### Python

There are tons of different programming languages out there. We will learn how to write code in the Python programming language, an easy to read, understand and write language.

| Py Concepts  |
|--------------|
| Data Types   |
| Variables    |
| Expressions  |
| Statements   |
| Functions    |
| Loops        |
| Conditions   |
| Objects      |
| Classes      |

***

### Getting Started with Chromebooks (trusty)

```bash
mkdir your_name
geany helloworld.py
```

#### HelloWorld.py

Go over data types: strings, integers (INT), floats (FLOAT), boolean (BOOL). *see notes.py*  

### Simple Calculator  

Finish creating a simple calculator in Python. Walking through step-by-step, starting with first variables with input:  

```python  
number1 = int(raw_input("Give me a number"))
number2 = int(raw_input("Give me another number"))

```  

### Random Number Game  

Go through a simple interactive random number game, starting with what is needed for this type of program, i.e. computer chooses from a range of numbers, place that random number into a variable, user-computer interaction (input), get the computer to check the user input to the random number chosen, keep the game alive with a simple while loop.  

### Pygame: Getting Started  

Creating a whole game using pygame can be daunting. First walkthrough creating a simple game from scratch, touching on the *bone structure* (or skeleton) to get a python program using pygame up and running. A first example can be execution of a simple pygame window, modify the background, display a picture object, have the picture object "bounce" around, then onto controlling the object with keystrokes. Reference the Development Process of the Intro to Computer Science Readme, found in this repo. The process can easily be tweaked to fit the initial specs for designing a simple pygame.  

### Pygame Walkthroughs  

Already-made games using pygame; however, with missing key points of code.  

### Computer System Layers
#### Abstraction

[Layers of Computer System Activity](https://github.com/techemstudios/nextup_lucille/blob/master/mini_lessons/computer_system_layers.pdf)

*15 - 20 min*

When we are working in one layer, we do not need to concern ourselves with the information in the surrounding layers. This way, we can just focus on what needs to be done in the moment. Think of abstraction as a mental model; a way to think about something. Have the unnecessary details hidden, so we can leave only the information we need to complete our goal.

Abstraction Examples:

* A Person Driving a Car
  - The only thing they need to focus on is the road ahead.
  - It is unnecessary to worry about details of how the engine or electronics of the car work.

* Fast Food Restaurant
  - At many restaurants, the names of meals have corresponding numbers.
  - The food prep has been trained to recognize the meal number, not worry about the full name.

### Object Oriented Programming

As we talked about decomposing (divide and conquer) and generalization (seeing the big picture) in computational thinking, object oriented in a nutshell is to look at the interaction of simple *objects*, as being part of a complex system. Each object does something, it has its own set of properties and attributes (things it can do) and belongs to a *Class*. Let's look at an example of a dog named, Scrappy. We can say, Scrappy is a specific individual in a larger class, Dogs. In Object Oriented terms, Scrappy is a particular *instance* of the dog class. Since Scrappy is part of the dog class, we can assume certain things about him. Scrappy most likely has four legs, a tail, a wet nose, an age, and can bark. Now take a dog named, Lassy. She will have similar characteristics, but may only differ in behavior, size, or color. So, every object is an instance of some class. The class describes the general characteristics (or properties) an instance will have. The instance of the class will hold more specific properties and attributes.
