def welcome_statement():
    print('''
  _______ _        _______           _______         
 |__   __(_)      |__   __|         |__   __|        
    | |   _  ___     | | __ _  ___     | | ___   ___ 
    | |  | |/ __|    | |/ _` |/ __|    | |/ _ \ / _ \\
    | |  | | (__     | | (_| | (__     | | (_) |  __/
    |_|  |_|\___|    |_|\__,_|\___|    |_|\___/ \___|''')
    print("Welcome to my text-based TicTacToe.")


class Board:
    def __init__(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

    def show_board(self):
        print('      -----')
        for line in self.board:
            print('     |',
                  end='')  # end parameter makes that there is no new line in the code, so we can make nice grid
            print(' '.join(line), end='')
            print('|')
        print('      -----')

    def check_horizontal(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
        else:
            return False

    def check_vertical(self, player):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        else:
            return False

    def check_diagonal(self, player):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        else:
            return False

    def check_full_board(self):
        # if returns False game is still going other way True
        if any(' ' in short_list for short_list in self.board):
            return False
        else:
            return True

    def check_occupied_cell(self, col, row):
        if self.board[row][col] != ' ':
            return True


class Game(Board):
    def __init__(self):
        super().__init__()
        self.current_player = "X"
        self.other_player = "O"
        self.winner = None

    def player_move(self):
        try:
            print(f"It is the turn of player {self.current_player}")
            row, col = map(int, input("Enter row and column numbers with a space between to fix spot: ").split())
        except ValueError:
            print("You should enter two numbers!")
        else:
            if row < 1 or row > 3 or col < 1 or col > 3:
                print('Coordinates should be between 1-3!')
            elif self.check_occupied_cell(col - 1, row - 1):
                print("This cell is occupied! Choose another one!")
            else:
                self.board[row - 1][col - 1] = self.current_player
                self.swap_player()

    def swap_player(self):
        self.current_player, self.other_player = self.other_player, self.current_player

    def check_win(self):
        players = [self.current_player, self.other_player]
        for player in players:
            if self.check_vertical(player) or self.check_horizontal(player) or self.check_diagonal(player):
                self.winner = player
                return True
        return False


def play_game():
    welcome_statement()
    game = Game()
    while True:
        game.show_board()
        if game.check_full_board():
            print('Draw')
            break
        elif game.check_win():
            print(f'Game is over!!! The winner is whoever played {game.winner}! Thanks for playing!')
            break
        else:
            game.player_move()

    play_again = input('Do you want to play again? (y/n)').lower()
    while play_again not in ['y', 'n']:
        play_again = input('Invalid input. Do you want to play again? (y/n)').lower()

    if play_again == 'y':
        play_game()
    else:
        print('Thanks for playing!')


play_game()
