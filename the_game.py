from sys import exit
import time

class Character:

    die = "Dead"

    def __init__(self,gender,name,age,status):
        self.gender = gender
        self.name = name
        self.status = status
        self.age = age

    def kill_char(self):
        self.status = self.die
        return f"{self.name} is now dead."

print("Enter your chosen name: ")
username = input("> ")
print("Enter your desired gender(female or male): ")
playergender = input("> ")

player = Character(playergender,username,"Alive","15")
gov_assasin = Character("male","The Serpent","Alive","37")
friend1 = Character("female","Sabrina","Alive","17" )
friend2 = Character("male","Nate","Alive","15")

characters = [player, gov_assasin,friend1, friend2]

time.sleep(1)
print("Project Lily")
time.sleep(1)
print("\n")
print("....Loading....")
time.sleep(3)
print("\n")

input(f"""At 11:58 p.m., {friend1.name}, {friend2.name} and you leave the movie theatre after watching 'Vanishing on 7th Street'. 
\nLeft paranoid by the movie, you guys stay near the street lights at all times on the way to {friend1.name}'s house. Just in cAsE.
""")
input("You guys decide to head there because her parents are gone for the weekend. \nRight after watching a horror movie though? Smh")
input(f"\nYou guys stop on the way to get pizza at 12:05 a.m. because you can and soon arrive at {friend1.name}'s house.")
input(f"""After hours of fun and 'teen rebellion(staying up til 3)', all of you finally succumb to sleep. 
\nPassed out on the couches of the {friend1.name}'s family home. Classy.""")
Character.kill_char(friend2)

time.sleep(5)

input(f"You and {friend1.name} wake up at the early hour of 11:00 a.m. . Nice job,guys.")
input(f"{friend2.name} is seemingly not around when you guys wake up but you don't think much of it at first.")
time.sleep(1)
input("Well until you do and try to call him.")
input("You dial and immediately get an error saying that his number does not exist.")
input("You dial again. Still nothing.")
input("You're perplexed because you swear you saved his number right. So you try agai")
input("And again. And again...and again.")
input(f"At this point, concern takes over you and you let {friend1.name} know what's going on and try to call him with her cell.")
input("You guys decide to wait it ")

