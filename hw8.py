##1.

class Animal:
    hints = {
        'elephant':['I have exceptional memory','I am the largest land-living mammal in the world','I have big ears'],
        'tiger':['I am the biggest cat','I come in black and white or orange and black','I am the king of the forest'],
        'bat':['I use echo-location', 'I can fly', 'I see well in dark']
    }
    def __init__(self, name):
        self.name = name
        self.index_hint = 0

    def guess_who_am_i(self):
        print('I will give you 3 hints, guess what animal I am\n')
        while self.index_hint < 3:
            print(self.hints[self.name][self.index_hint])
            self.index_hint += 1
            guess = input("Who am I?:" )
            if guess == self.name:
                print("You got it! I am {}\n".format(self.name))
                return
            print('Nope, try again!\n')

        print("I'm out of hints! The answer is: {}\n".format(self.name))


e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")
e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()




##2. 

from random import randrange

print("INTEGER DIVISIONS")

while True:
    a = randrange(5)
    b = randrange(5)

    #user_input = in(input(a/b))
    try:

        print(str(a)+"/"+str(b)+"=")
        c = int(input())

        if(c==a//b):
            print("CORRECT!")
        else:
            print("INCORRECT!")
    except ValueError:
        print("Please enter an integers Only!")
    except:
        print("There are errors in program , please reenter")
