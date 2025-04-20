import random
def logic(num):
    if number==3:
        return "fizz fizz"
    elif number==36:
        return "fizz fizz buzz"
    if num % 3 == 0 and num % 4 == 0:
        return "fizzbuzz"
    elif num % 3 == 0 or num ==6 or num==13:
        return "fizz"
    elif num % 4 == 0 or num==14:
        return "buzz"
    elif num == 36:
        return "fizz fizz buzz"
    else:
        return str(num)

Score = 0
for x in range(5):
    number = random.randint(1,100)
    print(number)
    answer = input("What do you say? - fizz, buzz or fizzbuzz?")

    correct_answer = logic(number)

    if answer==correct_answer:
        print("Correct")
        Score=Score+1
    else:
        print("Incorrect, loser")
    

print(f"You're score is {Score} out of 5")
