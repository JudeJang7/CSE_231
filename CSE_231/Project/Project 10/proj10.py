###########################################################
# Project 10: Nine Men’s Morris
#
# If command is "R", restart the game
# If command is "H", display menu of commands
# If command is "Q", quit the game
#     
# Phase 1:
# Place players pieces at inputted point
# If mill is created, remove other players piece
#
# Phase 2:
# Move players pieces from origin to destination    
# If mill is created, remove other players piece  
# If the other player has less than three pieces, current player wins
###########################################################

import NMM #This is necessary for the project


BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
  _   _ _              __  __            _       __  __                 _     
 | \ | (_)_ __   ___  |  \/  | ___ _ __ ( )___  |  \/  | ___  _ __ _ __(_)___ 
 |  \| | | '_ \ / _ \ | |\/| |/ _ \ '_ \|// __| | |\/| |/ _ \| '__| '__| / __|
 | |\  | | | | |  __/ | |  | |  __/ | | | \__ \ | |  | | (_) | |  | |  | \__ \
 |_| \_|_|_| |_|\___| |_|  |_|\___|_| |_| |___/ |_|  |_|\___/|_|  |_|  |_|___/
                                                                                        
    The game is played on a grid where each intersection is a "point" and
    three points in a row is called a "mill". Each player has 9 pieces and
    in Phase 1 the players take turns placing their pieces on the board to 
    make mills. When a mill (or mills) is made one opponent's piece can be 
    removed from play. In Phase 2 play continues by moving pieces to 
    adjacent points. 
    
    The game is ends when a player (the loser) has less than three 
    pieces on the board.

"""


MENU = """

    Game commands (first character is a letter, second is a digit):
    
    xx        Place piece at point xx (only valid during Phase 1 of game)
    xx yy     Move piece from point xx to point yy (only valid during Phase 2)
    R         Restart the game
    H         Display this menu of commands
    Q         Quit the game
    
"""
        
def count_mills(board, player):
    """
        board: board methods gets list of mill points and dictionary of points
        player: mill points are compared to player
        Returns: Number of mills
    """
    
    mills = board.MILLS
    points = board.points
    count = 0
    
    for mill in mills:
        
        p1 = mill[0] # Point 1
        p2 = mill[1] # Point 2
        p3 = mill[2] # Point 3
        
        # Mill Counter
        if points.get(p1) == player and points.get(p2) == player \
            and points.get(p3) == player:
            count += 1
            
    return count
            
def place_piece_and_remove_opponents(board, player, destination):
    """
        board: board methods gets dictionary of points
        player: used in various functions
        destination: used in various functions
    """
    
    points = board.points  
    
    # Raise RuntimeErrors if specific conditions are met
    # If no RuntimeErrors are raised, assign piece to destination
    # If mill was created, remove piece from other player
    if destination not in points:
        raise RuntimeError("Invalid command: Not a valid point")
    if points.get(destination) != ' ': 
        raise RuntimeError("Invalid command: Destination point already taken")
    else:
        count_before = count_mills(board, player) 
        board.assign_piece(player, destination)   
        count_after = count_mills(board, player) 
        if count_after > count_before:
            print("A mill was formed!")
            other_player = get_other_player(player)
            remove_piece(board, other_player)
     
def move_piece(board, player, origin, destination):
    """
        board: board methods gets dictionary of points and dictionary of adjacent points
        player: used in various functions
        origin: used in various functions
        destination: used in various functions
    """
    
    points = board.points   
    adjacency = board.ADJACENCY
    
    # Raise RuntimeErrors if specific conditions are met
    # If destination is adjacent to origin, move piece
    if points.get(origin) != player:
        raise RuntimeError("Invalid command: Origin point does not belong to player")
    if destination not in points:
        raise RuntimeError("Invalid command: Not a valid point")
    else:
        if destination in adjacency[origin]:
            points[origin] = ' '
            place_piece_and_remove_opponents(board, player, destination)
        else:
            raise RuntimeError("Invalid command: Destination is not adjacent")
            
def points_not_in_mills(board, player):
    """
        board: board methods gets dictionary of points and list of mill points
        player: values in dictionary and mill points compared to player
        Returns: set of occupied points not in mills
    """
    
    points = board.points
    mills = board.MILLS
    occupied_points = set() 
    occupied_mill_points = set() 
    
    # If players piece is at point, add point to set of occupied points
    for point, man in points.items():
        if man == player:
            occupied_points.add(point)
            
    for mill in mills:
        
        p1 = mill[0] # Point 1
        p2 = mill[1] # Point 2
        p3 = mill[2] # Point 3
        
        # If players piece form a mill, add points to set of mill points
        if points[p1] == player and points[p2] == player \
            and points[p3] == player:
                occupied_mill_points.update(mill)
                
    # Finds points that are occupied, but also not in mills  
    not_in_mill_points = occupied_points - occupied_mill_points   
    return not_in_mill_points        

def placed(board,player):
    """
        board: board methods gets dictionary of points
        player: values in dictionary compared to player
        Returns: list of points occupied by player
    """
    
    points = board.points
    occupied_points = []
    
    # If players piece is at point, add point to list of occupied points
    for point, man in points.items():
        if man == player:
            occupied_points.append(point)
            
    return occupied_points        
    
def remove_piece(board, player):
    """
        board: used in various functions and clear_place method used
        player: used in varius functions
    """
    
    print(board)
    not_in_mill_points = points_not_in_mills(board, player)
    
    # If only occupied points are points in mills, mill points are the only points
    if len(not_in_mill_points) == 0:
        not_in_mill_points = placed(board,player)
    
    # Raise RuntimeErrors if specific conditions are met 
    # Remove piece if no RunTimeErrors were raised
    while True:
        try:
            remove = input("Remove a piece at :> ").strip().lower()
            if remove not in board.points:
                raise RuntimeError("Invalid command: Not a valid point")              
            if board.points[remove] != player:
                raise RuntimeError("Invalid command: Point does not belong to player")          
            if remove not in not_in_mill_points:
                raise RuntimeError("Invalid command: Point is in a mill")
                
            board.clear_place(remove)       
            return
    
        except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
        
def is_winner(board, player):
    """
        board: used in various functions
        player: used in various functions
        Returns: boolean
    """ 

    other_player = get_other_player(player)
    
    # If other player has less than three pieces, player is winner
    if len(placed(board, other_player)) < 3:
        return True
    else:
        return False        
    
def get_other_player(player):
    """
    Get the other player.
    """
    return "X" if player == "O" else "O"
    
def main():
    
    #Loop so that we can start over on reset
    while True:
        
        #Setup stuff.
        print(RULES)
        print(MENU)
        board = NMM.Board()
        print(board)
        player = "X"
        placed_count = 0 # total of pieces placed by "X" or "O", includes pieces placed and then removed by opponent
        
        # PHASE 1
        print(player + "'s turn!")
        #placed = 0
        command = input("Place a piece at :> ").strip().lower()
        print()

        #Until someone quits or we place all 18 pieces...
        while command != 'q' and placed_count != 18:
            try:       
                
                # If input is "r", reset the game
                if command.strip().lower() == "r":
                    break
                
                # If input is "h", print Menu
                if command.strip().lower() == "h":
                    print(MENU)
                    command = input("Place a piece at :> ").strip().lower()
                    continue
                
                # If input is valid, place piece at input
                # Add 1 to placed pieces counter
                # Prompt other player
                else:
                    place_piece_and_remove_opponents(board, player, command)              
                    placed_count += 1
                    player = get_other_player(player)      
                
            #Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
                
            #Prompt again
            print(board)
            print(player + "'s turn!")
            if placed_count < 18:
                command = input("Place a piece at :> ").strip().lower()
            else:
                print("**** Begin Phase 2: Move pieces by specifying two points")
                command = input("Move a piece (source,destination) :> ").strip().lower()
            print()
        
        #Go back to top if reset
        if command == 'r':
            continue
        
        # PHASE 2 of game
        while command != 'q':
            # commands should have two points
            command = command.split()
            try:
                
                # If origin and destination are valid
                # Move piece from origin to destination
                if len(command) == 2:       
                    
                    origin = command[0]
                    destination = command[1]
                    
                    move_piece(board, player, origin, destination)
                    
                    # If other player has less than 3 pieces, player is winner
                    if is_winner(board,player) == True:
                        print(BANNER)
                        return
                    
                    # Prompt other player
                    player = get_other_player(player)
                
                # If origin and destination are not valid
                else:
                    print("Invalid number of points")
                    print("Try again.")
                
            #Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))  
                
            #Display and reprompt
            print(board)
            #display_board(board)
            print(player + "'s turn!")
            command = input("Move a piece (source,destination) :> ").strip().lower()
            print()
            
        #If we ever quit we need to return
        if command == 'q':
            return

            
if __name__ == "__main__":
    main()