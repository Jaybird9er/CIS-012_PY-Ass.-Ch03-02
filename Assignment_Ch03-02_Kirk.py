print("Enter [R]ock, [P]aper, or [S]cissor")
player1 = input("Player 1: ")
print("Enter [R]ock, [P]aper, or [S]cissor")
player2 = input("Player 2: ")

print("\n")
if player1 == 'r' or player1 == 'R':
    if player2 == 'p' or player2 == 'P':
        print("Paper covers rock.")
        print("Player 2 WINS!")
    elif player2 == 's' or player2 == 'S':
        print("Rock smashes scissor.")
        print("Player 1 WINS!")
    else:
        print("Nobody WINS!")
elif player1 == 'p' or player1 == 'P':
    if player2 == 's' or player2 == 'S':
        print("Scissor cuts paper.")
        print("Player 2 WINS!")
    elif player2 == 'r' or player2 == 'R':
        print("Paper covers rock.")
        print("Player 1 WINS!")
    else:
        print("Nobody WINS!")
else:
    if player2 == 'r' or player2 == 'R':
        print("Rock smashes scissor.")
        print("Player 2 WINS!")
    elif player2 == 'p' or player2 == 'P':
        print("Scissor cuts paper.")
        print("Player 1 WINS!")
    else:
        print("Nobody WINS!")
