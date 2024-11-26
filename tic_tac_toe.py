import random
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.sassy_comments = [
            "Oh, interesting choice... if you're into that sort of thing.",
            "Wow, didn't see that coming (actually, I did).",
            "Are you sure about that? Like, really sure?",
            "Bold strategy, Cotton. Let's see if it pays off.",
            "Your move is as predictable as a romantic comedy.",
            "That's... certainly a choice you just made there.",
            "I've seen better moves in a sloth race.",
            "Playing it safe, huh? How adventurous of you."
        ]
        
    def display_board(self):
        print("\n")
        print(f" {self.board[0]} │ {self.board[1]} │ {self.board[2]} ")
        print("───┼───┼───")
        print(f" {self.board[3]} │ {self.board[4]} │ {self.board[5]} ")
        print("───┼───┼───")
        print(f" {self.board[6]} │ {self.board[7]} │ {self.board[8]} ")
        print("\n")
        
    def is_winner(self, player):
        # Check rows
        for i in range(0, 9, 3):
            if all(self.board[i + j] == player for j in range(3)):
                return True
        # Check columns
        for i in range(3):
            if all(self.board[i + j] == player for j in range(0, 9, 3)):
                return True
        # Check diagonals
        if all(self.board[i] == player for i in [0, 4, 8]):
            return True
        if all(self.board[i] == player for i in [2, 4, 6]):
            return True
        return False
        
    def is_board_full(self):
        return ' ' not in self.board
        
    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False
        
    def get_computer_move(self):
        # First, try to win
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                if self.is_winner('O'):
                    self.board[i] = ' '
                    return i
                self.board[i] = ' '
                
        # Then, block player's win
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'X'
                if self.is_winner('X'):
                    self.board[i] = ' '
                    return i
                self.board[i] = ' '
                
        # Take center if available
        if self.board[4] == ' ':
            return 4
            
        # Take corners
        corners = [0, 2, 6, 8]
        available_corners = [i for i in corners if self.board[i] == ' ']
        if available_corners:
            return random.choice(available_corners)
            
        # Take what's left
        edges = [1, 3, 5, 7]
        available_edges = [i for i in edges if self.board[i] == ' ']
        if available_edges:
            return random.choice(available_edges)

def main():
    game = TicTacToe()
    
    print("🎮 Welcome to the Most Dramatic Tic Tac Toe Ever! 🎭")
    print("Where X's and O's have more personality than your favorite TV characters!")
    
    while True:
        game.display_board()
        
        # Player's turn
        while True:
            try:
                position = int(input("Your turn! Choose a position (1-9): ")) - 1
                if 0 <= position <= 8:
                    if game.make_move(position, 'X'):
                        print(random.choice(game.sassy_comments))
                        break
                    else:
                        print("That spot is taken! Are you even looking at the board? 🙄")
                else:
                    print("Um, that's not even on the board. Try again! 🤦")
            except ValueError:
                print("That's not a number! What are you even doing? 🤔")
                
        if game.is_winner('X'):
            game.display_board()
            print("🎉 You won! (Did you cheat? I'm watching you... 👀)")
            break
            
        if game.is_board_full():
            game.display_board()
            print("😐 It's a tie! (How anticlimactic...)")
            break
            
        # Computer's turn
        print("\n🤖 Computer is thinking", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print("\n")
        
        computer_move = game.get_computer_move()
        game.make_move(computer_move, 'O')
        
        if game.is_winner('O'):
            game.display_board()
            print("💻 Computer wins! (As if that's a surprise...)")
            break
            
        if game.is_board_full():
            game.display_board()
            print("😐 It's a tie! (How anticlimactic...)")
            break

if __name__ == "__main__":
    main()
    
    while True:
        play_again = input("\nWant to lose again? (y/n): ").lower()
        if play_again == 'y':
            print("\n" * 100)  # Clear screen
            main()
        elif play_again == 'n':
            print("Goodbye! Remember: it's just a game... or is it? 🤔")
            break
        else:
            print("That's a yes/no question. Not that complicated! 🙄")