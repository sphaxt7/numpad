from numpad import MineSweeper, TicTacToe, Schulte
from blessed import Terminal
import sys
term = Terminal()


def main():
    """main function"""
    start_menu()



def print_options(options):
    """printing the menu for each game"""
    print(term.clear())
    print(term.bold(term.blue("Welcome to Numpad Games!\n"))
          + "Use your numpad to navigate\n")
    print(term.bold("Select an option:\n"))
    for i, (key, enabled) in enumerate(options.items(), start=1):
        check = '✔' if enabled else ' '
        print(f"{i}. [{term.green(check)}] {key}")
    print("\nPress '0' to Quit\nPress Enter to Confirm\n")
    


def start_menu() -> None:
    """starting menu"""
    options = {
        "MineSweeper": False,
        "TicTacToe": False,
        "Schulte": False,
    }

    with term.cbreak():
        while True:
            print_options(options)
            key = term.inkey()
            
            if key == '1':
                options['MineSweeper'] = True
                options['TicTacToe'] = False
                options['Schulte'] = False
            elif key == '2':
                options['MineSweeper'] = False
                options['TicTacToe'] = True
                options['Schulte'] = False
            elif key == '3':
                options['MineSweeper'] = False
                options['TicTacToe'] = False
                options['Schulte'] = True
            elif key in ('\r', '\n'):
                break
            elif key == '0':
                sys.exit()

    if options['MineSweeper']:
        game = 'mine'
    elif options['TicTacToe']:
        game = 'xo'
    elif options['Schulte']:
        game = 'sch'
    
    try:
        play(game)   # calls play with game chosen
    except UnboundLocalError:
        start_menu() # calls start_menu again incase of invalid input

def play(game: str):
    """game launcher"""

    games = {"sch": start_schulte, "xo": start_xo, "mine": start_mine} 
    games[game]() 
    

def start_schulte():
    """schulte launcher"""
    term = Terminal()
    options = {
        "Ascending": True,
        "Descending": False,
        "Shuffle": False
    }

    with term.cbreak():
        while True:
            print_options(options)
            key = term.inkey()
            if key == '1':
                options['Ascending'] = True
                options['Descending'] = False
            elif key == '2':
                options['Ascending'] = False
                options['Descending'] = True
            elif key == '3':
                options['Shuffle'] = not options['Shuffle']
            elif key in ('\r', '\n'):
                break
            elif key == '0':
                sys.exit()

    game_mode = 'Ascending' if options['Ascending'] else 'Descending'
    shuffle_enabled = options['Shuffle']
    game = Schulte(game_mode, shuffle_enabled)
    game.play_schulte()



def start_xo():
    """tictactoe launcher"""

    options = {
        "X": True,
        "O": False
    }
    with term.cbreak():
        while True:
            print_options(options)
            key = term.inkey()
            if key == '1':
                options['X'] = True
                options['O'] = False
            elif key == '2':
                options['X'] = False
                options['O'] = True
            elif key in ('\r', '\n'):
                break
            elif key == '0':
                sys.exit()

        symbol = 'X' if options['X'] else 'O'
        game = TicTacToe()
        game.play_xo(symbol)


def start_mine():
    """minesweeper launcher"""

    show_bomb = True
    game = MineSweeper(show_bomb)
    game.play_mine()




if __name__ == "__main__":
    main()