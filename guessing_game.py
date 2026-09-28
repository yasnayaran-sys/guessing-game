import random

number = random.randint(1, 100)

print("بازی حدس عدد!")
print("یک عدد بین ۱ تا ۱۰۰ حدس بزن.")

while True:
    guess = int(input("حدس تو: "))

    if guess < number:
        print("عدد بزرگتر از حدس توعه!")
    elif guess > number:
        print("عدد کوچکتر از حدس توعه!")
    else:
        print("درست حدس زدی!")
        break
