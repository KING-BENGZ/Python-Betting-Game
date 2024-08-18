import random

CashBal = 10000
print("Let's stake something. I'll give you a starting amount of 10k.")


def RandomGuess():
    return random.randint(1, 5)  # Generate a random number between 1 and 10

def StartBet(CashBal):
    print("Input an amount you want to stake out of 10k:")
    Stake = int(input())  # Convert input to integer

    if Stake > 8000:
        print("Going high, I see!")
    else:
        print("That's a bit low, big boy.")

    print("Your bet doubles the amount you have always. Pick a number between 1 and 5:")
    PickedNumber = int(input())  # Convert input to integer

    ComputerGuess = RandomGuess()
    if ComputerGuess == PickedNumber:
        NewBal = CashBal + (Stake * 2)
        print("You're lucky! Your new balance is:", NewBal)
    else:
        NewBal = CashBal - Stake
        print("Sorry, my guy. That's", Stake, "gone. Your new balance is:", NewBal)
    
    return NewBal  # Return the updated balance

# Betting loop
while CashBal > 1:
    CashBal = StartBet(CashBal)
    if CashBal <= 1:
        print("You're out of cash! Game over.")
        break
