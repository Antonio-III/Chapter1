#Chapter 5: Exercises 1~5.
#Exercise 1: Person. Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
person={'first_name':'Joe','last_name':'Biden','age':'42','city':'Washington D.C.'}
print(person)
#Exercise 2: Glossary. A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary. Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
pythonwords={'print':'is a function that displays the output of whatever is stored in its parenthesis.','sort':"is a function that sorts the list into an alphabetical or ascending order. This function is written as: exvariable.sort(). This function will make the variable's contents be replaced with the sorted ones.",'while':'is a keyword that will accept a condition, and if it is True, will execute its contents until the condition is False.','break':'will make the code exit out of the loop.','continue':'will skip the condition and return to the top of the loop.'}
#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
print("print\n",pythonwords['print'])
print("sort\n",pythonwords['sort'])
print("while\n",pythonwords['while'])
print("break\n",pythonwords['break'])
print("continue\n",pythonwords['continue']+"\n")
#Exercise 3: Glossary 2. Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.
pythonwords['sorted']="will sort the contents of a variable into an alphabetical or ascending order. Unlike the 'sort' keyword, it will only be done temporarily, so it is better to store this function in a variable like: newvar=sorted(exvar). It could also be done like: print(sorted(exvariable)) but the variable will still be same next time it's called."
pythonwords['reverse']="will reverse the order of the variable, which is the opposite of sort/sorted functions. It is done permanently and is written as: exvar.reverse()"
pythonwords['del']="will delete the entire variable that the next time it's called, it will no longer be defined."
pythonwords['clear']="will clear the content of a list-type variable, but only making it empty. It is written as: exvar.clear()"
pythonwords['keys']="will get the Key values of a dictionary variable. It is written as: exvar.keys(). Putting it in a variable like: newvar=exvar.keys() will cause the newvar variable have all the Key values in the dictionary. "
for key,value in pythonwords.items():
    print(key,value+"\n")
#Exercise 4: Rivers. Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'. Use a loop to print a sentence about each river, such as The Nile runs through Egypt. Use a loop to print the name of each river included in the dictionary. Use a loop to print the name of each country included in the dictionary.
rivers={"Amazon":"Peru","Yangtze":"China","Mississippi":"US"}
for key,value in rivers.items():
    print("The",key,"river runs through the country of",value+".")
#Exercise 5: Pets. Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
pet1={"animal":"dog","owner":"Bruh"}
pet2={"animal":"cat","owner":"Bruv"}
pet3={"animal":"crocodile","owner":"Matey"}
#Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
pets=[pet1,pet2,pet3]
for a in pets:
    print("The pet is an animal called a",a['animal']+". His owner is called",a['owner']+".")
