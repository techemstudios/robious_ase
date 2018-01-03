# Intro to Computer Science - NextUp  

### Introductions  

* Name  
* Age  
* Grade  
* Experience  
  - Any programming/coding experience?  

### Objectives  
##### What We'll Learn  

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

## Day One  

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

## Day Two  

Review content from day one. Explain how to handle user input by starting to create a simple calculator program. Before typing any code, ask what we want this program to do:  

1) We want to ask a user for two numbers and we want to store those numbers in a variable, so we can later use them.  

2) We need to get input from the user about which operation they want to perform on the two numbers.

3) We'll need to check their text input to what operation symbol it matches with.

4) Finally, we want to return the answer to the user.  

```python  
number1 = int(raw_input("Give me a number: "))
number2 = int(raw_input("Give me another number: "))
# with the raw_input() function, Python automatically thinks the text
# from the user is a string. We add int() to convert the string to an integer
# This will allow us to "mathematically" add the two numbers given by the user.

operation raw_input("What operation would you like me to perform?")

# our first condition statement (if this, then this)
if operation == "+":
  answer = number1 + number2

print(answer)
```  

## Day Three  

### Basic Calculator Program  

Finish the calculator program by adding multi-way decision pattern, in other words `if-elif-else`.  

[One way to finish a basic calculator program](https://github.com/techemstudios/nextup_lucille/blob/master/intro_to_computer_science/python_code/calculator.py)  

***  

## Day Four  

### Logic Gates  

Review binary, value of 1 and zero and representations of each: 1 = On, True, Yes, etc.; 0 = Off, False, No, etc.  

Devices that perform basic operation on electrical signals.  

### NOT, AND, OR  

How they operate, three ways we can represent them. Combine gates to form circuits.  


***  

## Day Five  

see notes.py  

### Random Number Game  

#### Binary Search Tree  

How a computer efficiently searches an ordered (sorted) list, ordered from lowest to highest. Think about the random number game. A person picks a number between a range of numbers and asks you to guess the number they picked. Each time the you guess, the person will tell you if your guess is higher or lower, compared to the number they picked.  

Let's say the person picked a number between 1 and 100. Our logical first guess could be 50. If the person told you the number is higher, then the range of possible numbers is cut in half, 50-100. If you guess 75 (the middle of the range), you once again narrow the range of possible numbers. This is a systematic search approach called *binary search*. We know that binary means two. Looking back, each guess you made divided the remaining numbers into two parts.  

Let's make the random number game a program in Python. Just as with the calculator program, we'll start with a systematic approach to developing our simple program. Determine the specifications ("specs" for short): 1) Have the computer choose a random number from a range of numbers, and store the number in a variable. 2) Clearly inform the user what the computer is asking of them 3) Determine a decision based on the user's input. That's it.  

#### Program Design  

Translate the specs into program form.  

```python  
# In order to use random methods, we need to import the random module
import random

# Spec #1:
# Create a variable whos value is a randomly chosen number, from a range a numbers
number = random.randint(1, 100)

# Spec #2:
print("I'm thinking of a number between 1-100")
# Create a variable whose value is the number guessed by the user
guess = int(raw_input("Guess a number between 1-100: "))

# Spec #3:
# Set up a few condition statements to compare the user's guess to the randomly picked number
if guess > number:
  # what happens when the user's guess is higher than number picked
  print("Your guess is too high!")
elif guess < number:
  # What happens when the user's guess is lower than the number picked
  print("Your guess is too low!")
elif guess == number:
  # what happens when the user guesses the number picked
  print("You guessed correctly!")
```  

Our next step in our development process is to test the program. Our program works; however, if the user guesses too high or too low, the program ends. We can easily fix this by inserting a `while` loop. First, we'll add a flag,  `GameRunning` (or call it anything you want). This will act as a signal to the program which checks whether or not the game should keep running. As long as the flag is set to `True`, the program will continue; otherwise, the program will stop running when we set the flag's value to `False`. You can relate how a while loop works to the statement, "as long as...". A flag is one of a few methods to stop a while loop.  

```python
GameRunning = True
while True:
    guess = int(raw_input("Guess a number between 1-100: "))

    if guess > number:
        print("Your guess is too high!")
    elif  guess < number:
        print("Your guess is too low!")
    elif guess == number:
        print("You guessed correctly!")
        # Since the user guessed correctly, set the flag to False
        GameRunning = False
        raw_input("\n\nPress enter key to exit ")
        exit()
```  



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


### Write Code like you Write a Story  

Very important; make your code easy to read and understand. Write your program like you are writing a story about something. Stories are created for others to easily read and understand; otherwise, what is the point!? Heavily use comments in your code. This helps you and whoever is looks at your program, understand what's happening and how it's happening.  

### Object Oriented Programming  

As we talked about decomposing (divide and conquer) and generalization (seeing the big picture) in computational thinking, object oriented in a nutshell is to look at the interaction of simple *objects*, as being part of a complex system. Each object does something, it has its own set of properties and attributes (things it can do) and belongs to a *Class*. Let's look at an example of a dog named, Scrappy. We can say, Scrappy is a specific individual in a larger class, Dogs. In Object Oriented terms, Scrappy is a particular *instance* of the dog class. Since Scrappy is part of the dog class, we can assume certain things about him. Scrappy most likely has four legs, a tail, a wet nose, an age, and can bark. Now take a dog named, Lassy. She will have similar characteristics, but may only differ in behavior, size, or color. So, every object is an instance of some class. The class describes the general characteristics (or properties) an instance will have. The instance of the class will hold more specific properties and attributes.  

### Development Process  

#### Write SIMPLE Programs  

*Zelle, John M. Python Programming: an Introduction to Computer Science. Franklin, Beedle & Associates, 2010*  

**Analyze the Problem**  
Figure out exactly what the problem is. What needs to be done.  
**The Specs**  
Determine the goals. Try out physically writing down or typing up comments/docstrings about what your program will do, what problem it will solve, the overall goal. Think abstraction; leave out the details about *how* your program will work, focus instead on *what* it will accomplish. For simple programs, just describe the inputs/outputs and how they relate.  
**Design/Implement**  
Lay out the program structure. Now you can focus on the *how*. As in computational thinking (mentioned earlier), design the algorithm or plan that will tackle the problem then, carry out the plan.  
**Test/Debug**  
Test out all parts of the program. Making a checklist may help. Does your program work as you expect it would? Don't worry, errors will be expected. Fix the errors, or debug the program.  
**Maintain**  
The more you continue developing the program, the more efficient it will be. Remember, engineers are concerned with building things to be the more and more efficient. Refactoring can come into play here. Getting user feedback will help in maintaining your program.  
