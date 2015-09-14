__author__ = 'daniel.neumann'

# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    loopcounter = 10
    mult = 2.0
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(loopcounter):
        x = mult * x * (1 - x)
        print(x)

main()
