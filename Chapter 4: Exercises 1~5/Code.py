#Chapter 4: Exercises 1~5
#Exercise 1: Alien Colors.
#Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
alien_color="green"
#Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
if alien_color=="green":
    print("You earned 5 points!")
#Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
version1="green"
if version1=="green":
    print("You earned 5 points!")
version2="red"
if version2=="green":
    print("You earned 5 points!")
#Exercise 2: Alien Colors. Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain. If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien. If the alien’s color isn’t green, print a statement that the player just earned 10 points. Write one version of this program that runs the if block and another that runs the else block.
version1="green"
if version1=="green":
    print("You earned 5 points for shooting the green alien!")
else:
    print("You earned 10 points for shooting the non-green alien!")
version2="red"
if version2=="green":
    print("You earned 5 points for shooting the green alien!")
else:
    print("You earned 10 points for shooting the non-green alien!")
#Exercise 3: Alien Colors. Turn your if-else chain from Exercise 5-4 into an if-elifelse chain. Write three versions of this program, making sure each message is printed for the appropriate color alien.
version1="green"
#If the alien is green, print a message that the player earned 5 points.
if version1=="green":
    print("You earned 5 points!")
#If the alien is yellow, print a message that the player earned 10 points.
elif version1=="yellow":
    print("You earned 10 points!")
#If the alien is red, print a message that the player earned 15 points.
else:
    print("You earned 15 points!")
version2="yellow"
if version2=="green":
    print("You earned 5 points!")
elif version2=="yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")
version3="red"
if version3=="green":
    print("You earned 5 points!")
elif version3=="yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")
#Exercise 4: Stages of Life. Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age,
age=int(input("Enter your age: "))
#and then: If the person is less than 2 years old, print a message that the person is a baby.
if age <2 :
    print("The person is a baby.")
#If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
elif age>=2 and age<4:
    print("The person is a toddler.")
#If the person is at least 4 years old but less than 13, print a message that the person is a kid.
elif age>=4 and age<13:
    print("The person is a kid.")
#If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
elif age>=13 and age<20:
    print("The person is a teenager.")
#If the person is at least 20 years old but less than 65, print a message that the person is an adult.
elif age>=20 and age<65:
    print("The person is an adult.")
#If the person is age 65 or older, print a message that the person is an elder.
else:
    print("The person is an elder.")
#Exercise 5: Favorite Fruit. Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list. Make a list of your three favorite fruits and call it favorite_fruits.
favorite_fruits=["bananas","apples","tomatoes"]
#Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as: You really like bananas!
if "bananas" in favorite_fruits:
    print("You really like bananas!")
if "pumpkins" in favorite_fruits:
    print("You really like pumpkins!")
if "oranges" in favorite_fruits:
    print("You really like oranges!")
if "apples" in favorite_fruits:
    print("You really like apples!")
if "mangoes" in favorite_fruits:
    print("You really like mangoes!")
