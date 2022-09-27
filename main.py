# username= input("What is your name?: ")
#
# while username == "Ricky":
#     print("Username accepted")
# elif username ==
# else:
#     print("Who the fuck are you.")

# name = input("Enter your name: ")
#
# while len(name) == 0:
#     name = input("Enter your name: ")
# else:
#     print("Welcome,"+ name)

# name = None
#
# while not name:
#     name = input("Enter your name: ")
# print("Welcome," + name)
#
# num = int(input(""))
# while not num == 0:
#     num = num -1
#     print(num)

# for num in range(10,100+1,3):
#     print(num)

# for w in "Wongwww":
#     print(w)

# import time
#
# for seconds in range(10,-1,-1):
#     print(seconds)
#     time.sleep(1)
# print("fuck")

# print("Rectangle maker.")
#
# width = int(input("What would be the width of the rectangle?: "))
# height = int(input("What would be the height of the rectangle?: "))
# symbol = input("Symbol to use: ")
#
# for i in range(width):
#     for j in range(height):
#         print(symbol, end="")
#     print("")

# while True:
#     name = input("Username?:")
#     if name != "":
#         break

# phone_num = "123-456-789"
#
# for i in phone_num:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1,11):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

# food = ["bing chilin","apple","banana","chips","fries"]
# food.append("ice cream")
# food.remove("apple")
# food.pop(1)
# food.insert(2,"cake")
# food.sort()
# food.clear()
#
# for i in food:
#     print(i)

# drinks = ["cola","water,soup","pepsi"]
# fruit = ["apple","banana","orange",]
# snack = ["kit kat","chocolate","sugar"]
#
# food = [drinks,fruit,snack]
#
# print(food[1][0])

# student = ("ricky",20,"male")
#
# print(student.count(20))
# print(student.index("male"))
#
# for x in student:
#     print(x)
#
# if 20 in student:
#     print("this nigga is 20")

# fruit = {"banana","coconut","apple","pepsi"}
# drinks = {"cola","water","pepsi"}

# fruit.add("grapes")
# fruit.remove("banana")
# fruit.clear()
# fruit.update(drinks)
# food = fruit.union(drinks)

# print(fruit.difference(drinks))
# print(fruit.intersection((drinks)))

# for i in food:
#     print(i)

# capitals = {"USA":"Washington",
#             "China":"Shang hai",
#             "India":"Dehli"}

# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"somewhere"})
# capitals.pop("China")
# capitals.clear()
# print(capitals["USA"])
# print(capitals.get("germany"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for i,k in capitals.items():
#     print(i)

# name = "ricky wong"

# if (name[0].islower()):
#     name = name.capitalize()

# first_name = name[:5].capitalize()
# last_name = name[6:].capitalize()
# print(last_name)

# def hello(name, last,age):
#     print("hi " + name, last)
#     print("your age is "+str(age))
#     print("have a nice day")
#
# my_name = "jason"
#
# hello("my_name","wong",21)

# def multiply(num1,num2):
#     result = num1*num2
#     return result
# num1 = int(input("What is the first number you want to multiply?:"))
# num2 = int(input("the sencond one?: "))
#
# ans=multiply(num1,num2)
# print(ans)

# name = "Wong Hin Chun"
# def display_name():
#     name = "Ricky"
#     print(name)
#
# display_name()
# print(name)

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# print(add(1,2,3,4))

# def hello(**kwargs):
#     print("Hello ",end="")
#     print("Hello ",kwargs["first"],kwargs["last"])
#     for key,value in kwargs.items():
#         print( value, end=" ")
#
# hello(first="ricky",last="wong",middle="nigga",)

# animal = "cow"
# item = "log"

# print("A "+animal+" jumped over a "+item)
# print("The {fi} jumped over the {sec}".format(sec=animal,fi=item))

# text = "the {} jumped over the {}"
# print(text.format(animal,item))

# name = input("what is your name?: ")
# print("Hello, your name is {:^10}. Nice to meet you.".format(name))
# pi = 3.1415
# print("The number pi is {:.2f}".format(pi))

# import random
#
# x = random.randint(1,6)
# y = random.random()
# print(y)
#
# mylist =["rock","paper","scissors"]
# rps = random.choice(mylist)
# print(rps)
#
# cards = [*range(2,10),"J","K","Q","A"]
# random.shuffle(cards)
# print(cards)

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("nigga u divide by 0")
# except ValueError as e:
#     print(e)
#     print("Enter only number plz")
# except Exception as e:
#     print(e)
#     print("Something went wrong")
# else:
#     print(result)
# finally:
#     print("This will always execute.")

# import os
#
# path = "C:\\Users\\hk\\Desktop\\test.txt"
#
# if os.path.exists(path):
#     print("That location exists")
#     if os.path.isfile(path):
#         print("That is a file.")
#     elif os.path.isdir(path):
#         print("It is a directory")
# else:
#     print("That location doesn't exists")
# try:
#     with open("C:\\Users\\hk\\Desktop\\test.txt") as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print(e)
#     print("File is not found")

# text = "123\n123\ntest"
# with open("test.txt","r+") as file:
#     file.write(text)
#     print(file.read())
# with open("test.txt") as file:
#     print(file.read())

# import shutil
#
# shutil.copyfile("test.txt","C:\\Users\\hk\\PycharmProjects\\HelloWorld\\test folder\\testcopy.txt")

# import os
#
# source = "test.txt"
# destination = "C:\\Users\\hk\\PycharmProjects\\HelloWorld\\test folder\\test.txt"
#
# try:
#     if os.path.exists(destination):
#         print("There is already a file in that location")
#     else:
#         os.replace(source,destination)
#         print(source+" was moved")
#
# except FileNotFoundError as e:
#     print(e)
#     print("File not found.")

# import os
# import shutil
#
# path = "test folder"
#
# try:
#     os.remove(path)
#     print("File removed")
#     os.rmdir(path)
#     shutil.rmtree(path)
# except FileNotFoundError as e:
#     print(e)
#     print("File not found.")
# except PermissionError as e:
#     print(e)
#     print("Ain't got no permission to do so.")
# else:
#     print("File successfully removed")

# import messages as msg
#
# msg.hello()
#
# help("modules")

# mock_data = ['value 1', 'value 2', 'value 3', 'value 4', 'value 4', 'value 2', 'value 2', 'value 4']
# previous_value = ''
#
# for value in mock_data:
#     if value == previous_value:
#         print(value)
#     else:
#         print('no match')
#     previous_value = value

# def all_equal(a):
#     ls = sorted(a)[::-1]
#     if sorted(a) == ls:
#         print(True)
#         return True
#     else:
#         print(False)
#         return False
# def all_equal(items):
#     for item1 in items:
#         for item2 in items:
#             if item1 != item2:
#                 print(False)
#                 return False
#     print(True)
#     return True

# import random
# def rbs():
#     choices = ["rock", "paper", "scissors"]
#     computer = random.choice(choices)
#     player = input("Rock, paper or scissors?: ").lower()
#     while player.lower() not in choices:
#         print("Insert only rock, paper or scissors.")
#         player = input("Rock, paper or scissors?: ").lower()
#     print("Computer: ", computer)
#     print("player: ", player)
#     if player == computer:
#         print("Tie!")
#     elif player == "rock":
#         if computer == "scissors":
#             print("Player Wins!")
#         else:
#             print("Computer Wins!")
#     elif player == "scissors":
#         if computer == "paper":
#             print("Player Wins!")
#         else:
#             print("Computer Wins!")
#     elif player == "paper":
#         if computer == "rock":
#             print("Player Wins!")
#         else:
#             print("Computer Wins!")
#     again = input("Want to play again?: Yes/No: ").lower()
#     yn = ["yes", "no"]
#     while again not in yn:
#         print("Insert only yes or no")
#         again = input("Want to play again?: Yes/No: ").lower()
#     if again == "yes":
#         rbs()
#     else:
#         print("Thank you for playing.")
#
# rbs()

# def new_game():
#     option = ["A", "B", "C", "D"]
#     guesses = []
#     correct_guesses = 0
#     question_num = 1
#     for key in questions:
#         print("----------------------------------")
#         print(key)
#         for i in options[question_num-1]:
#             print(i)
#         guess = input("Enter (A,B,C,D): ").upper()
#         while guess not in option:
#             print("Enter only (A,B,C,D)")
#             guess = input("Enter (A,B,C,D): ").upper()
#         guesses.append(guess)
#
#         correct_guesses += check_answer(questions.get(key),guess)
#         question_num+=1
#
#     display_score(correct_guesses,guesses)
#     play_again()
# def check_answer(answer, guess):
#
#     if answer == guess:
#         print("CORRECT!")
#         return 1
#     else:
#         print("WRONG")
#         return 0
# def display_score(correct_guesses,guesses):
#     print("-------------------------------")
#     print("RESULTS")
#     print("-------------------------------")
#
#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print()
#
#     print("Guesses: ", end="")
#     for i in guesses:
#         print(i, end=" ")
#     print()
#
#     score = int(correct_guesses/len(questions)*100)
#     print("Your score is:"+ str(score)+"%")
# def play_again():
#     response = input("Do you want to play again?: (Yes/No)").lower()
#     while response not in ("yes","no"):
#         print("Enter only yes or no")
#         response = input("Do you want to play again?: (Yes/No)").lower()
#     if response == "yes":
#         new_game()
#     else:
#         print("Thanks for playing.")
#
# questions = {"Whats the answer of 1+1?: ":"A",
#             "Whats the answer of 1+2?: ":"B",
#             "Whats the answer of 1+3?: ":"C",
#             "Whats the answer of 9+10?: ":"D",}
# options = [["A. 1","B. 2","C. 3","D. 4"],
#            ["A. 1","B. 2","C. 3","D. 4"],
#            ["A. 1","B. 2","C. 3","D. 4"],
#            ["A. 1","B. 2","C. 3","D. 21"],]
# new_game()

# from car import car
#
# car_1 = car("Chevy","Chorvette",2021,"blue")
# car_2 = car("Chiron","Bugatti",2021,"blue")
# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)
# car.wheels = 2
# print(car_1.wheels)
# print(car_2.wheels)
# car_2.drive()
# car_2.stop()
# print(car.wheels)

# class Animals:
#
#     alive = True
#     def eat(self):
#         print("This animal is eating")
#
#     def sleep(self):
#         print("This animal is sleeping")
#
# class Rabbit(Animals):
#     def jump(self):
#         print("This rabbit is jumping")
# class Fish(Animals):
#     def swim(self):
#         print("This fish is swimming")
# class Hawk(Animals):
#     def fly(self):
#         print("This hawk is flying")
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# print(rabbit.alive)
# fish.eat()
# rabbit.jump()
# fish.swim()
# hawk.fly()

# class Organism:
#     alive = True
#
# class Animals(Organism):
#     def eat(self):
#         print("This animals eats")
#
# class Dog(Animals):
#     def bark(self):
#         print("This dog is barking")
#
# dog = Dog()
# print(dog.alive)
# dog.eat()

# class Predator:
#     def hunt(self):
#         print("This animal hunts")
#
# class Prey:
#     def flee(self):
#         print("This animal flees")
#
# class Rabbit(Prey):
#     pass
# class Hawk(Predator):
#     pass
# class Fish(Prey, Predator):
#     pass
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# fish.flee()
# fish.hunt()
# hawk.hunt()

# class Animal:
#     def eat(self):
#         print("This animal eats")
#
# class Rabbit(Animal):
#     def eat(self):
#         print("This rabbit is eating a carrot")
#
# rabbit = Rabbit()
#
# rabbit.eat()

# class Car:
#     def turn_on(self):
#         print("You start the engine")
#         return self
#
#     def drive(self):
#         print("You drive the car")
#         return self
#
#     def brake(self):
#         print("You step on the brakes")
#         return self
#
#     def turn_off(self):
#         print("You turn off the engine")
#         return self
#
# car = Car()
#
# car.turn_on().drive().brake().turn_off()
#
# car.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()

# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass
#
# class Car(Vehicle):
#     def go(self):
#         print("You drive the car")
#
# class Motorcycle(Vehicle):
#     def go(self):
#         print("You drive the motorcycle")
#
# vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()
#
# car.go()
# motorcycle.go()

# class Car:
#     color = None
#
# class Motorcycle:
#     color = None
#
# def color_change(vehicle,color):
#     vehicle.color = color
#
# car1 = Car()
# car2 = Car()
# car3 = Car()
#
# bike1 = Motorcycle()
#
# color_change(car1,"red")
# color_change(bike1,"brown")
#
# print(car1.color)
# print(bike1.color)

# class Duck:
#     def walk(self):
#         print("This duck is walking")
#
#     def talk(self):
#         print("This duck is quacking")
#
# class chicken:
#     def walk(self):
#         print("This chicken is walking")
#
#     def talk(self):
#         print("This chicken is clucking")
#
# class Person():
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter")
#
# duck = Duck()
# chicken = chicken()
# person = Person()
#
# person.catch(duck)
# person.catch(chicken)

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food =="quit":
#         break
#     foods.append(food)

# foods = list()
# while food := input("What food do you like?: ") != "quit":
#     foods.append(food)

# def hello():
#     print("Hello")
# hi = hello
# hi()
#
# say = print
# say("Hello World")

# def loud(text):
#     return text.upper()
#
# def quiet(text):
#     return text.lower()
#
# def hello(text,func):
#     print(func(text))
#
# hello("Hello",quiet)

# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend

# double = lambda x:x*2
# print(double(10))
# full_name = lambda first_name, last_name: first_name + " "+last_name
# age_check = lambda age:True if age >= 18 else False
# print(full_name("RIcky","WOng"))
# print(age_check(10))

# test = [("abc","b",3),("bac","c",1),("cba","a",2)]
# a = lambda test:test[2]
# def index_1(x):
#     return x[1]
# test.sort(key=index_1)
# print(test)

# store = [("shirt",20.00),
#          ("pants",25.00),
#          ("jacket",50.00),
#          ("socks",10.00)]
# to_hkd = lambda x:(x[0],x[1]*10)
# print(list(map(to_hkd,store)))

# factorial = [1,2,3,4,5]
# result = 1
# for i in factorial:
#     result *= i
# print(result)

# if __name__ == "__main__":
#     print("running module directly")
# else:
#     print("running module indirectly")

# def Hello():
#     print("Hello!")
#
# if __name__ == "__main__":
#     Hello()

class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None
    def __init__(self,data):
        self.data = data