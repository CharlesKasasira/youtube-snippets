import random

class TicTacToe:
    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append(" ")
            self.board.append(row)
    
    def show_board(self):
        for row in self.board:
            print("-------------")
            for i in range(len(row)):
                print("|", end=" ")
                print(row[i], end=" ")
                if(i == 2): 
                    print("|")
        print("-------------")

    def generate_first_player(self):
        return random.randint(0, 1)

    def swap_player(self, player):
        return 'X' if player == 'O' else 'O'


    def fix_spot_played(self, row, col, player):
        self.board[row][col] = player

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == " ":
                    return False
        return True

    def is_player_win(self, player):
        win = None
        length = len(self.board)

        # checking row
        for i in range(length):
            win = True
            for j in range(length):
                if self.board[i][j] != player:
                    win = False
                    break 
            if win:
                return win
        
        # checking col
        for i in range(length):
            win = True
            for j in range(length):
                if self.board[j][i] != player:
                    win = False
                    break 
            if win:
                return win


        # checking diagonals
        win = True 
        for i in range(length):
            if self.board[i][i] != player:
                win = False
                break

        win = True 
        for i in range(3):
            if self.board[i][2 - i] != player:
                win =  False
                break

        if win:
            return win

    def start(self):
        self.create_board()

        player = 'X' if self.generate_first_player() == 1 else 'O'

        while True:
            print(f"Player {player}'s turn")
            self.show_board()

            row, col = list(map(int, input("Enter row and column to fix spot: ").split()))
            print()


            self.fix_spot_played(row-1, col-1, player)

            if self.is_player_win(player):
                print(f"Player {player} wins")
                self.show_board()
                break 

            if self.is_board_filled():
                self.show_board()
                print("Draw")
                break

            player = self.swap_player(player)

tic_tac_toe = TicTacToe()
tic_tac_toe.start()