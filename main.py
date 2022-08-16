import random

start = 1
end = 10

random_number = random.randint(start, end)

guessed = 0

while guessed != random_number:
    guessed = int(input(f"Guess a number between {start} and {end}: "))

    if guessed > random_number:
        print("too high")
    elif guessed < random_number:
        print("too low")

print("you guessed correct")


# computer guess
check_number = ''
start = 1
end = 10

while check_number != 'c':
    guessed_number = random.randint(start, end)
    print(f"computer is guessing the number to be : {guessed_number}")

    check_number = input("if correct 'c', if too high 'h', or if too low 'l' : ")
    if check_number == 'h':
        end = guessed_number - 1
    elif check_number == 'l':
        start = guessed_number + 1

print("computer guessed correct")
