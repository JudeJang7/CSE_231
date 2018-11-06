###########################################################
# Programming Project #4
# Finite State Machine
#
# get_ch function:
# Prompts user to input character
# If character is valid, proceed to appropriate state
# If character is invalid, reprompt user to input a valid character
# Return character
#  
# find_state function:
# Starts at state 1
# If inputted character is "h", go to state 2, otherwise go to state 5
# If state is 2 and inputted character is "a" or "o", go to state 3
# otherwise, go to state 5
# If state is 3 and inputted character is "h" go to state 2
# If state is 3 and inputted character is "!" go to state 4
# otherwise go to state 5
# If state is 4, go to state 5
# Return state
#
# def_main function:
# Calls get_ch and find_state functions
# Concatenates characters until user inputs enter  
# If state is 4, user is laughing
# otherwise user is not laughing
###########################################################

# Function that prompts user to input a character
def get_ch():
    
    # Prompt user to input a character in a loop
    ch = "  "
    while len(ch) > 1:
        ch = input("Enter a character or press the Return key to finish: ")
    
        # If user enters a invalid input, prints an error message   
        if len(ch) > 1:
            print("Invalid input, please try again.")
        
    # Returns character 
    return ch

# Function that finds current state
def find_state(state, ch):
   
    # If state is 1
    if state == 1:
        # If inputted character is "h", proceed to state 2
        if ch == "h":
            state = 2
        # Otherwise, proceed to state 5    
        else:
            state = 5
       
    # If state is 2    
    elif state == 2: 
        # If inputted character is "a" or "o", proceed to state 3
        if ch == "a" or ch == "o":
            state = 3
        # Otherwise, proceed to state 5    
        else:
            state = 5
    
    # If state is 3        
    elif state == 3:
        # If inputted character is "h", proceed to state 2
        if ch == "h":
            state = 2
        # If inputted character is "!", proceed to state 4    
        elif ch == "!":
            state = 4
        # Otherwise, proceed to state 5    
        else:
            state = 5
       
    # If state is 4, proceed to state 5    
    elif state == 4:
        state = 5       
     
    # Returns state    
    return state

# Function that uses get_ch and find_state function and prints
def main():
    print("I can recognize if you are laughing or not.")
    print("Please enter one character at a time.")
    
    # Initialized variables
    string = ""
    state = 1
    
    # Loop that concatenates characters to empty string
    while True:
        ch = get_ch()
        string += ch
              
        # If user inputs enter, end program
        if ch == "":
            print("\nYou entered", string)
            # If state is 4, user is laughing
            if state == 4:
                print("You are laughing.")
            # Otherwise, user is not laughing    
            else:    
                print("You are not laughing.")
            break
        state = find_state(state, ch)

main()