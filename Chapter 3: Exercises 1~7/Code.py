#Chapter 3. Exercises 1~7
#Exercise 1: Names. Store the names of a few of your friends in a list called names.
names=["Slim","Shady","Joe","Biden"]
#Print each person’s name by accessing each element in the list, one at a time.
for name in names:
    print(name)
#Exercise 2: Greetings. Start with the list you used in Exercise 1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
for name in names:
    print("Greetings,",name,"how are you doing?")
#Exercise 3: Your Own List. Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples.
vehicle=["Honda car","Lamborghini car","Dirt bike"]
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
for i in vehicle:
    print("I would like to own a",i,"one day.")
#Exercise 4: Guest List. If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner.
guest=["Antonio","Miguel","Intal"]
#Then use your list to print a message to each person, inviting them to dinner.
for i in guest:
    print("Hello,",i+"! I would like to invite you to dinner!")
#Exercise 5. Change Guest List. You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite. Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it. Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
print("It's so sad",guest.pop(0),"couldn't make it. I will invite someone else on my list!")
guest.insert(0,"Jo")
#Print a second set of invitation messages, one for each person who is still in your list.
for i in guest:
    print("Greetings,",i+"! I would like to invite you to my dinner!")
#Exercise 6. Shrinking Guest List. You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests. Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner. Use pop() to remove guests from your list one at a time until only two names remain in your list.
print("My new dinner table couldn't arrive in time, so I can only have 2 guests for my dinner!")
#Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
print("I'm so sorry,",guest.pop(1)+", I can only host 2 guests for my dinner!")
#Print a message to each of the two people still on your list, letting them know they’re still invited.
for i in guest:
    print("Hello,",i+"! You're still invited to my dinner!")
#Use del to remove the last two names from your list, so you have an empty list.
del guest[0]
del guest[0]
#Print your list to make sure you actually have an empty list at the end of your program.
print(guest)
#Exercise 7. Seeing the world. Think of at least five places in the world you’d like to visit. Store the locations in a list. Make sure the list is not in alphabetical order.
places=["China","South Africa","Canada","Ireland","New Zealand"]
#Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
print(places)
#Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(places))
#Show that your list is still in its original order by printing it.
print(places)
#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(places,reverse=True))
#Show that your list is still in its original order by printing it again.
print(places)
#Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()
print(places)
#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
places.reverse()
print(places)
#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
places.sort()
print(places)
#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
places.sort(reverse=True)
print(places)
