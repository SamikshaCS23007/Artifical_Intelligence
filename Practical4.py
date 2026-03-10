board = [" "] * 10   # index 0 ignore karenge

def print_board():
    print(f"\n {board[1]} | {board[2]} | {board[3]}")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print("---+---+---")
    print(f" {board[7]} | {board[8]} | {board[9]}\n")

def check_win(mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or
            (board[4]==mark and board[5]==mark and board[6]==mark) or
            (board[7]==mark and board[8]==mark and board[9]==mark) or
            (board[1]==mark and board[4]==mark and board[7]==mark) or
            (board[2]==mark and board[5]==mark and board[8]==mark) or
            (board[3]==mark and board[6]==mark and board[9]==mark) or
            (board[1]==mark and board[5]==mark and board[9]==mark) or
            (board[3]==mark and board[5]==mark and board[7]==mark))

def board_full():
    return " " not in board[1:]

player = "X"

print("Welcome to Tic Tac Toe!")

while True:
    print_board()
    pos = int(input(f"Player {player}, choose position (1-9): "))
 
    if board[pos] == " ":
        board[pos] = player
    else:
        print("Already filled! Try again.")
        continue

    if check_win(player):
        print_board()
        print(f"🎉 Player {player} wins!")
        break

    if board_full():
        print_board()
        print("😐 It's a tie!")
        break

    # switch player
    if player == "X":
        player = "O"
    else:
        player = "X"
