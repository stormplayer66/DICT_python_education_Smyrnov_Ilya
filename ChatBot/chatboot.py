print("Hello! My name is Bob")
print("I was created in 2022")
print("Please, remind me your name")
name = input("> ")

print("What a great name you have, {0}!".format(name))
print("Let me guess your age.\nEnter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print("Your age is {0}; that's a good time to start programming!".format(age))
print("Now I will prove to you that I can count to any number you want.")
number = int(input("> "))
i = 0
while i != number+1:
    print("{0}!".format(i))
    i = i + 1

print("Completed, have a nice day")
print("What does the git init command mean?")
print("1.Prints the specified message to the screen.")
print("2.Creates a new Git repository.")
print("3.Returns an integer from a given object or converts a number in a given base to a decimal")
print("4.Allows you to perform the same sequence of actions as long as the condition being checked is true")
number = int(input("> "))
while number != 2:
    print("Please,try again")
    number = int(input("> "))
    ...
print("Congratulations, have a nice day!")
