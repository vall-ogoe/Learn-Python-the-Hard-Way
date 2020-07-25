from sys import exit

class Character:

    die = "Dead"

    def __init__(self):
        self.gender = gender
        self.name = name
        self.status = status
        self.age = age

    def kill_char(self):
        self.status = self.die
        return f"{self.name} is now dead."

print("Enter your chosen name: ")
username = input("> ")
print("Enter your desired gender: ")
playergender = input("> ")

player = Character(playergender,username,"Alive","15")

characters = [username, ]

