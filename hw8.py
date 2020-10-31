
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
a = randrange(5)

def get_user_input():
    user_input = int(input("INTEGER DIVISIONS\n"))
    while user_input > 5 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input


def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(" = "))
    return result


def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Correct.")
        return count
    else:
        print("Incorrect.")
        return count

def main():
    
    option = get_user_input()
    total = 0
    correct = 0
    while option != 5:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()

    display_separator()
    display_result(total, correct)

main()