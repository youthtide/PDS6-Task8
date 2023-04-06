def main_function():
    age = int(input("what's your age?"))
    if age < 18:
        print("sowwy:(")
    else:
        print("yay!")


import random


def test_function():
    flip = random.random()
    if flip < 0.5:
        print('Heads')
    else:
        print('Tales')
