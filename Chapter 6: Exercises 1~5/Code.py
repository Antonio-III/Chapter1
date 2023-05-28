#Chapter 6: Exercises 1~5
#Exercise 1: Pizza Toppings. Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.
while True:
    topping=input("Enter a pizza topping or enter 'quit' to stop: ")
    if topping=="quit":
        break
    else:
        print("You have entered",topping,"as a pizza topping!")
#Exercise 2: Movie Tickets. A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
while True:
    age=int(input("Enter your age. Your movie ticket will be based on how old you are. Enter '0' to stop: "))
    if age==0:
        break
    else:
        if age<3:
            print("Your movie ticket costs free.")
        elif age>=3 and age<12:
            print("Your movie ticket costs $10.")
        else:
            print("Your movie ticket costs $15.")
#Exercise 3: Infinity loop. Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)
a=0
while True:
    a+=1
    print(a)
#Exercise 4: Deli. Make a list called sandwich_orders and fill it with the names of various sandwiches.
sandwich_orders=['Tuna sandwich','Grilled cheese','Ham sandwich','Chicken sandwich','Egg sandwich']
#Then make an empty list called finished_sandwiches.
finished_sandwiches=[]
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
while True:
    print("Here are the sandwiches in my recipe:",sandwich_orders, "enter 'quit' to exit.")
    typer=input("Enter your order in my recipe\n")
    if typer in sandwich_orders:
        print("I made your",typer+".")
#As each sandwich is made, move it to the list of finished sandwiches.
        finished_sandwiches.append(typer)
        sandwich_orders.remove(typer)
#After all the sandwiches have been made, print a message listing each sandwich that was made.
        if len(sandwich_orders)==0:
            typer=input("You entered all the sandwiches in my recipe! Enter 'y' to try again, any key to exit.\n")
            if typer=='y':
                sandwich_orders=finished_sandwiches
                finished_sandwiches=[]
                continue
            else:
                break
    elif typer in finished_sandwiches:
        print("I already made that sandwich! Try again!")
    elif typer=='quit':
        break
        
    else:
        print("That's not in my recipe! Try again!")
#Exercise 5: No Pastrami. Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
sandwich_orders=['Pastrami sandwich','Pastrami sandwich','Pastrami sandwich','Tuna sandwich','Grilled cheese','Ham sandwich','Chicken sandwich','Egg sandwich']
finished_sandwiches=[]
print("The deli has run out of pastrami sandwich! Sad!")
while sandwich_orders.count('Pastrami sandwich')>0:
    sandwich_orders.remove('Pastrami sandwich')
    print("Here are the sandwiches in my recipe:",sandwich_orders)
    print("Finished sandwiches:",finished_sandwiches)
