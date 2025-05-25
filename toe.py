board = [' '] * 9

def show(): print(f"{board[0]}|{board[1]}|{board[2]}\n-+-+-\n{board[3]}|{board[4]}|{board[5]}\n-+-+-\n{board[6]}|{board[7]}|{board[8]}")
def win(p): b = board; return any(b[i]==b[j]==b[k]==p for i,j,k in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])

player = 'X'
for _ in range(9):
    show()
    move = int(input(f"Player {player}, choose (0-8): "))
    if board[move] == ' ':
        board[move] = player
        if win(player):
            show()
            print(f"Player {player} wins!")
            break
        player = 'O' if player == 'X' else 'X'
    else:
        print("Spot taken, try again.")
else:
    show()
    print("It's a draw!")
