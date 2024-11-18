import random, time
from blessed import Terminal




class TicTacToe:
    """TicTacToe game logic"""
    def __init__(self):
        """instance variables"""
        self.board = {i: ' ' for i in range(1, 10)} 
        self.player = None
        self.computer = None
        self.game_running = True
        self.term = Terminal()
        self.win_conditions = [
                [7, 8, 9], [4, 5, 6], [1, 2, 3],   # rows
                [7, 4, 1], [8, 5, 2], [9, 6, 3],   # columns
                [9, 5, 1], [7, 5, 3]]              # diagonals


    def print_board(self):
        """simulating a numpad"""
        print(self.term.clear())  # clearing the terminal
        n = self.board 
        print(self.term.green("---TicTacToe---"))  
        print("\n"
              f" {n[7]}  |  {n[8]}  |  {n[9]} \n" 
              f"----+-----+----\n"
              f" {n[4]}  |  {n[5]}  |  {n[6]} \n" 
              f"----+-----+----\n"
              f" {n[1]}  |  {n[2]}  |  {n[3]} \n" )   
        
    
    def check_winner(self, s):
        """checking win conditions"""
        lines = self.win_conditions
        for line in lines:
            if all(self.board[pos] == s for pos in line):   # s is 'X' or 'O' 
                return True
        return False    
    

    def check_draw(self):
        """checking draw conditions"""
        return all(self.board[pos] in (self.player, self.computer) for pos in range(1, 10))  # returns True if board is full
    

    def computer_move(self):
        """finds next move for the computer"""
        lines = self.win_conditions
        board = self.board
        player = self.player
        computer = self.computer

        """choose winning square"""
        for line in lines:
            if sum(1 for sqr in line if board[sqr] == computer) == 2 and \
            any(board[sqr] == ' ' for sqr in line):  
                return next(sqr for sqr in line if board[sqr] == ' ')
            
        """block the player"""
        for line in lines:
            if sum(1 for sqr in line if board[sqr] == player) == 2 and \
            any(board[sqr] == ' ' for sqr in line):
                return next(sqr for sqr in line if board[sqr] == ' ')
            
        """pick remaining empty squares"""
        empty = [sqr for sqr in range(1, 10) if board[sqr] == ' ']
        return random.choice(empty) if empty else None


    def play_xo(self, s):
        """starts the game"""
        board = self.board
        c = self.term
        self.player = c.blue(s)
        self.computer = c.red('O') if s == 'X' else c.red('X')
        P = self.player
        C = self.computer
        if s == 'O':      
            comp_move = self.computer_move()   # if player chose 'O', computer starts first
            self.board[comp_move] = C
        self.print_board()
        while self.game_running:
            with self.term.cbreak():
                key = self.term.inkey()
                if key.isnumeric():
                    move = int(key)
                    if 1 <= move <= 9 and self.board[move] == ' ':
                        self.board[move] = P
                        self.print_board()
                    elif move == 0:
                        self.game_running = False
                        break
                    else:
                        continue

                    """check for win or draw"""
                    if self.check_winner(P):
                        self.print_board()
                        print("You win!\n")
                        self.game_running = False  #if player wins game ends
                        break
                    elif self.check_draw():
                        self.print_board()
                        print("It's a draw!\n")
                        self.game_running = False  #if it's a draw game ends
                        break

                    """computer's turn"""
                    comp_move = self.computer_move()
                    if comp_move:
                        board[comp_move] = C
                        self.print_board()
                        print(f'You chose: {move}')
                        print(f'Computer chose: {comp_move}')
                        if self.check_winner(C):
                            self.print_board()
                            print('Computer wins!\n')
                            self.game_running = False
                        elif self.check_draw():
                            self.print_board()
                            print("It's a draw!\n")
                            self.game_running = False


class MineSweeper:
    """minesweeper logic"""
    def __init__(self, show_bomb=False):
        """variables"""
        self.bomb = random.randint(1, 9)
        self.numpad = {i: f'{i} ' for i in range(1, 10)}
        self.points = 0
        self.show_bomb = show_bomb
        self.term = Terminal()
        self.game_running = True

    def display_guesses(self):
        """prints numpad board"""
        print(self.term.clear())
        n = self.numpad
        print(self.term.red("--MineSweeper--"))
        print("\n"
              f" {n[7]} |  {n[8]} |  {n[9]} \n" 
              f"----+-----+----\n"
              f" {n[4]} |  {n[5]} |  {n[6]} \n" 
              f"----+-----+----\n"
              f" {n[1]} |  {n[2]} |  {n[3]} \n" )
        if self.show_bomb:
            print(f'bomb: {self.bomb}\n')   # shows bomb


    def play_mine(self):
        """starts minesweeper"""
        while self.game_running:
            self.display_guesses()
            print(f"Points: {self.points}\n")

            with self.term.cbreak():
                key = self.term.inkey()
                if key.isnumeric():
                    guess = int(key)

                    if guess in self.numpad and self.numpad[guess] != '# ': 

                        if guess == self.bomb:
                            self.numpad[guess] = "💥"
                            self.display_guesses()
                            print(f"You lose. \nPoints: {self.points}\n")
                            self.game_running = False
                        else:
                            self.numpad[guess] = "# "
                            self.points += 1
                            if self.points == 8:
                                self.numpad[self.bomb] = "💣"
                                self.display_guesses()
                                print(f"You win!! \nPoints: {self.points}\n")
                                self.game_running = False
                    elif guess == 0:
                        self.game_running = False


class Schulte:
    """schulte game logic"""
    def __init__(self, mode, shuffle):
        """variables"""
        self.nums = random.sample(range(1, 10), 9)
        self.board = {i+1: str(self.nums[i]) for i in range(9)}
        self.game_running = True
        self.mode = mode
        self.shuffle = shuffle
        self.next = 1 if self.mode == "Ascending" else 9   # next target starts at 1 if ascending or 9 if descending
        self.errors = 3
        self.hp = ["\u2665"] * self.errors  # simulates hp bar with 3 hearts
        self.term = Terminal()



    def print_board(self):
        """clear the screen and print the board with hp bar"""
        print(self.term.clear())
        n = self.board
        print(self.term.purple("----Schulte----"))
        print("\n"
              f" {n[7]}  |  {n[8]}  |  {n[9]} \n"
              f"----+-----+----\n"
              f" {n[4]}  |  {n[5]}  |  {n[6]} \n"
              f"----+-----+----\n"
              f" {n[1]}  |  {n[2]}  |  {n[3]} \n")
        print(f"HP: " + self.term.red(f"{''.join(self.hp)}"))

    def reshuffle(self):
        """reshuffling the numbers on the board"""
        self.nums = random.sample(range(1, 10), 9)
        self.board = {i+1: str(self.nums[i]) for i in range(9)}


    def play_schulte(self):
        """starts schulte"""
        self.print_board()
        start_time = time.time()
        while self.game_running:
            with self.term.cbreak():
                key = self.term.inkey()
                if key.isnumeric():
                    x = int(key)

                    if x == 0:
                        self.game_running = False
                    elif 1 <= x <= 9 and self.board[x] == f'{self.next}':
                    
                        self.board[x] = ' '  # clear the position
                        if self.shuffle:
                            self.reshuffle()

                        self.next += 1 if self.mode == "Ascending" else -1  
                        self.print_board()

                        # check for win condition 
                        if (self.mode == "Ascending" and self.next == 10) or (self.mode == "Descending" and self.next == 0):
                            elapsed_time = time.time() - start_time 
                            print(f"You win!\nTime: {elapsed_time:.2f}\n")
                            self.game_running = False
                    else:
                        # -1 hearts after each error
                        self.errors -= 1
                        self.hp[self.errors] = "\u2661"
                        self.print_board()

                        # check loss condition
                        if self.errors == 0:
                            print('You lose.')
                            self.game_running = False
