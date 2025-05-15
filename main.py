import random

# generate the random number betwwn 1 to 100
n = random.randint(1,100)
guess = None
attemt = 0

print("Guess the number ")


while  (guess != n):
    try:
        guess = int(input("Enter the guess = "))
        attemt += 1
        
        
        if(guess > n):
            print("lower number..")
        elif(guess < n):
            print("Higher number...")
        else:
            print(f"You guess the right number in {attemt} attemp ")
        
        
        
    except ValueError:
        print("Enter the valid number please")