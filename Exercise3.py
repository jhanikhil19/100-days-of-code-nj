#Guess number game
#total number of guesses - 9
#print no of guesses left after each turn
#print game over if all guesses ends


n=18
# print("enter a number of your guess")
# guess=int(input())
i=9
while (i>=0):
    guess=int(input("Enter a number of your guess: "))
    if guess<n:
        print("Guessed number is smaller than the MAGIC NUMBER")
        print("Number of guesses left",i-1)
        i=i-1
        continue
    elif (guess==n):
        print("**********CONGRATULATIONS***************")
        print("Guessed number",guess,"and the MAGICAL NUMBER",n,"matched.")

        break
    elif (guess>n):
        print("Guessed number is bigger than the MAGIC NUMBER")
        print("Number of guesses left", i - 1)
        i=i-1
        continue
print("..........GAME OVER.........")
