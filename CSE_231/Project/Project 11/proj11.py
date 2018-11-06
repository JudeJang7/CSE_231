###########################################################
# Project #11
#
# Prompts for row and column
# Places current players piece
# Switches player
# Places switched players piece
# Repeats until a player has pieced 5 of their pieces in a row
###########################################################
    
class GoPiece(object):
    ''' Methods for board Piece'''
    
    def __init__(self, color = "black"):
        ''' color: if color is not black or white, raise MyError'''
        
        if color != "black" and color != "white":
            raise MyError("Wrong color.")
        else:
            self.__color = color
    
    def __str__(self):
        ''' If color is black, return black piece
            If color is white, return white piece
            Returns: ● or ○ '''

        if self.__color == "black":
            return ' ● '
        if self.__color == "white":
            return ' ○ '
    
    def get_color(self):
        ''' Returns: black or white'''
        
        return self.__color
    
    def __repr__(self):
        return self.__str__()
            
class MyError(Exception):
    
    def __init__(self,value):
        self.__value = value
        
    def __str__(self):
        return self.__value

class Gomoku(object):   
    ''' Methods for Gomoku game'''
    
    def __init__(self, board_size = 15, win_count = 5, current_player = "black"):
        ''' board_size: size of board
            win_count: number of pieces in a row needed to win
            current_player: player currently playing'''

        # If specific conditions are not met, raise errors
        if type(board_size) == int: 
            self.__board_size = board_size
        else:
            raise ValueError             
        if type(win_count) == int:
            self.__win_count = win_count
        else:
            raise ValueError                
        if current_player != "black" and current_player != "white":
            raise MyError("Wrong color.")
        else:
            self.__current_player = current_player

        # Creates a list of lists. Rows are the inner lists, columns are the index
        self.__go_board = [ [ ' - ' for j in range(self.__board_size)] for i in range(self.__board_size)]  
            
    def assign_piece(self, piece, row, col):
        ''' piece: piece gets assigned at specific row and column
            row: horizontal 
            col: vertical'''
        
        # If inputted row and column do not exist, raise error
        # If inputted row and column are valid, assign piece at coordinates
        if row < 1 or row > self.__board_size:
            raise MyError('Invalid position.')
        elif col < 1 or col > self.__board_size:
            raise MyError('Invalid position.')
        elif self.__go_board[row-1][col-1] != ' - ':
            raise MyError('Position is occupied.')  
        else:    
            self.__go_board[row-1][col-1] = piece
            
    def get_current_player(self):
        ''' Returns: current player'''
        
        return self.__current_player
    
    def switch_current_player(self):
        '''Switches current player internally '''
 
        if self.__current_player == "black":
            self.__current_player = "white"
        else:
            self.__current_player = "black"
        
    def __str__(self):
        
        s = '\n'
        for i,row in enumerate(self.__go_board):
            s += "{:>3d}|".format(i+1)         
            for item in row:
                s += str(item)
            s += "\n"
        line = "___"*self.__board_size
        s += "    " + line + "\n"
        s += "    "       
        for i in range(1,self.__board_size+1):
            s += "{:>3d}".format(i)
        s += "\n"
        s += 'Current player: ' + ('●' if self.__current_player == 'black' else '○')
        
        return s
        
    def current_player_is_winner(self):
        ''' Keeps track of same colored pieces in a consecutive row
            horizontally, vertically, and diagonally.'''

        # Iterates through list of lists
        # If any inner list has 5 same colored pieces consecutively,
        # Returns True
        hori_count = 0 # Horizontal Count
        for row in self.__go_board:
            for point in row:
                if str(point) == str(GoPiece(self.__current_player)):
                    hori_count += 1
                    if hori_count >= 5:
                        return True
                else:
                    hori_count = 0            
        
        # Iterates through list of lists
        # Recreates list of lists using index
        # If any inner list in the new list of lists has 5 same colored pieces
        # consecutively, Returns True            
        vert_count = 0
        for i in range(0, self.__board_size):
            vert_list = [row[i] for row in self.__go_board]
            for point in vert_list:
                if str(point) == str(GoPiece(self.__current_player)):
                    vert_count += 1
                    if vert_count >= 5:
                        return True
                else:
                    vert_count = 0
        
        # Finds diagonal streaks with a negative slope
        n_d_count = 0
        for row in range(0, self.__board_size - self.__board_size +1):
            for col in range(self.__win_count - 1, self.__board_size):
                for k in range(0, self.__win_count):
                    if str(self.__go_board[row+k][col-k]) == str(GoPiece(self.__current_player)):
                        n_d_count += 1
                        if n_d_count >= 5:
                            return True
                    else:
                        n_d_count = 0
        
        # Finds diagonal streaks with a positive slope                
        p_d_count = 0
        for row in range(0, self.__board_size - self.__win_count +1):
            for col in range(0, self.__board_size - self.__win_count +1):
                for k in range(0, self.__win_count):
                    if str(self.__go_board[row+k][col+k]) == str(GoPiece(self.__current_player)):
                        p_d_count += 1
                        if p_d_count >= 5:
                            return True
                    else:
                        p_d_count = 0              
                    
        return False
        
def main():

    board = Gomoku()
    print(board)
    play = input("Input a row then column separated by a comma (q to quit): ")
    while play.lower() != 'q':
        play_list = play.strip().split(',')
        
        try: 
            
            # Checks to see if 2 inputs were entered
            # Else, raise error
            if len(play_list) == 2:
                pass
            else:
                raise MyError("Incorrect input.")
                
            # Checks to see if inputs are integers
            # Else, raise error
            try:
                int(play_list[0])
                int(play_list[1])
            except ValueError:
                raise MyError("Incorrect input.")             
            
            
            # Places piece at row and coordinate
            current_player = board.get_current_player()
            piece = GoPiece(current_player)       
            board.assign_piece(piece, int(play_list[0]), int(play_list[1]))

            # If current player has 5 consecutive pieces, they win
            if board.current_player_is_winner() == True:
                print(board)
                print("{} Wins!".format(board.get_current_player()))
                break
            
            # Switches player
            board.switch_current_player()

        except MyError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))
        print(board)
        play = input("Input a row then column separated by a comma (q to quit): ")

if __name__ == '__main__':
    main()