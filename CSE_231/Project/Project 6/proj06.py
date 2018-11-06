###########################################################
# Programming Project 06
#
# Prompts user for file name
# If file name not found, prints error message
#
# Prompts user for state code
# If state code is invalid, prints error message
#
# Reads file  
# Collects data for state
#
# Extracts data for state
# Calculates county, population, total water, per person water
#
# Prints data for state
# Asks user to plot data
# If input is yes, plots data for state
###########################################################
    
import pylab

STATES = {'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
          'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
          'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
          'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN',
          'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY'}
USERS = ["Public", "Domestic", "Industrial", "Irrigation","Livestock"]

def open_file(): # open_file function
    ''' Prompts user for file name. If file name is invalid,
        print error message and reprompt user.
        Returns fp. '''
    
    user_input = input("Input a file name: ") # Prompts user for file name   
    while True: # Loops while true
        try: # Try to:
            fp = open(user_input) # Open user inputted file
            return fp # Return filepointer   
        except FileNotFoundError: # If FileNotFoundError:
            print("Unable to open file. Please try again.") # Error message
            user_input = input("Input a file name: ") # Reprompt user
    
def read_file(fp): # read_file function
    ''' Calls fp from open_file().
        Reads header. Loops through each line in file. 
        Strips whitespace and splits elements on ",". 
        Keeps track of index and element.
        If value is missing, value becomes 0.
        Collects data for state, county, population, fresh water, salt water,
        public water usage, domestic water usage, industrial water usage, 
        irrigation water usage, livestock water usage.
        Appends variables to tup() then tup() to data_list[]. '''
    
    data_list = [] # Initialized data_list
    
    fp.readline() # Reads header
    for line in fp: # Loops through each line in file
        line = line.strip().split(",") # Strips whitespace and splits on ","  
        for index, element in enumerate(line): # Remembers index and element
            if element == "": # If element is an empty string
                line[index] = "0" # Element is now "0"

        state = line[0] # State is at line 0
        county = line[2] # County is at line 2
        population = float(line[6]) * 1000 # Population is at line 6
        fresh_water = float(line[114]) # Fresh water is at line 114
        salt_water = float(line[115]) # Salt water is at line 115
        public = float(line[18]) # Public is at line 118
        domestic = float(line[26]) # Domestic is at line 26
        industrial = float(line[35]) # Industrial is at line 35
        irrigation = float(line[45]) # Irrigation is at line 45
        livestock = float(line[59]) # Livestock is at line 59
            
        tup = (state, county, population, fresh_water, salt_water, # Appends
        public, domestic, industrial, irrigation, livestock) # variables to tup
        
        data_list.append(tup) # Appends tuple to data_list
        
    return data_list # Returns data_list
          
def extract_data(data_list, state): # extract_data function
    ''' Calls data_list[] and state from read_file(). 
        Loops through each element in data_list[]. 
        If state code is found, append to tup().
        If state code is all, append all states to tup().
        If state code is quit, return state list.
        Return state_list[]. '''
    
    state_list = [] # Initialized state_list
    
    for tup in data_list: # Loops through each element in data_list
        state_tup = tup[0] # state_tup is equal to element at index 0
        if state_tup == state: # If state_tup is equal to state
            state_list.append(tup) # Append element to state_list
        if state.upper() == "ALL": # If input is all:
            state_list.append(tup) # Appends all states to state_list
        if state.upper() == "QUIT": # If input is quit:                
            return state_list # Returns state_list    
    return state_list # Returns state_list       

def compute_usage(state_list): # compute_usage function
    ''' Calls state_list[] from extract_data().
        Loops through each element in state_list[].
        County is at index 1 of state_list[].  
        Population is at index 2 of state_list[].
        Fresh water is at index 3 of state_list[].
        Salt water is at index 4 of state_list[].
        Calculates total water using salt water and fresh water.
        Calculates per person water using fresh water and population.
        Appends variables to tup(), then tup() to usage_list[]. '''

    usage_list = [] # Initialized usage_list 
    
    for tup in state_list: # Loops through each element in state_list
        
        county = tup[1] # County is at index 1
        population = tup[2] # Population is at index 2
        fresh_water = tup[3] # Fresh water is at index 3
        salt_water = tup[4] # Salt water is at index 4
        
        total_water = salt_water + fresh_water # Total = salt + fresh
        per_person_water = fresh_water / population # Person = fresh / pop.
        
        tup = (county, population, total_water, per_person_water) # Tuple
        
        usage_list.append(tup) # Appends tuple to usage_list
    
    return usage_list # Returns usage_list

def display_data(state_list, state): # display_data function
    ''' Calls state_list and state from extract_data().
        Prints title and header.
        Loops through each element in usage_list().
        Formats and prints data for state. '''
    
    usage_list = compute_usage(state_list) # Calls compute_usage function
    
    title = "Water Usage in " + state + " for 2010" # Title
    header = "{:22s} {:>22s} {:>22s} {:>22s}".format("County", \
    "Population", "Total (Mgal/day)", "Per Person (Mgal/person)") # Header
    
    print("{:^88s}".format(title)) # Formats title
    print(header) # Prints header
    
    for tup in usage_list: # Loops through each element in usage_list
        print("{:22s} {:>22,.0f} {:>22.2f} {:>22.4f}".format(tup[0], \
        tup[1], tup[2], tup[3])) # Prints county, population, fresh, salt

def plot_water_usage(state_list, state): # plot_water_usage function
    '''
       Creates a list "y" containing the water usage in Mgal/d of all counties.
       Y should have a length of 5. The list "y" is used to create a pie chart
       displaying the water distribution of the five groups.
    '''

    # accumulate public, domestic, industrial, irrigation, and livestock data
    y =[ 0,0,0,0,0 ]

    for item in state_list: # Loops through each element in state_list

        y[0] += item[5] # Public
        y[1] += item[6] # Domestic
        y[2] += item[7] # Industrial
        y[3] += item[8] # Irrigation
        y[4] += item[9] # Livestock data

    total = sum(y) # Total of water usage
    y = [round(x/total * 100,2) for x in y] # Computes the percentages.

    color_list = ['b','g','r','c','m'] # Colors graph
    pylab.title(state) # Formats title
    pylab.pie(y,labels=USERS,colors=color_list) # Graph
    pylab.show() # Plot 
    pylab.savefig("plot.png") # Saves graph
    
def main(): # main function
    ''' Calls open_file().
        Calls read_file().
        Prompts user to input statecode.
        While the state code is not "quit",
        call state_list(), compute_usage(), display_data().
        If state code is invalid, print error message and reprompt.
        Asks user to plot, if yes, plot graph. 
        Prompt user for state code. '''
    print("Water Usage Data from the US and its States and Territories.") 
    
    fp = open_file() # Opens file
    data_list = read_file(fp) # Reads file
    
    state = input("Enter state code or 'all' or 'quit': ").upper().strip()
    
    while state != "QUIT": # If input is not quit
        
        while state not in STATES and state != "ALL": # If state code not found
                                                      # and input is not all
            print("Error in state code.  Please try again.") # Error message
            state = input("Enter state code or 'all' or 'quit': ")\
            .upper().strip() # Reprompt user for input
    
        state_list = extract_data(data_list, state) # Calls extract_data()
        compute_usage(state_list) # Calls compute_usage()
        display_data(state_list, state) # Calls display_data()
    
    
        answer = input("Do you want to plot? ").upper().strip() # Prompt answer
        if answer == "YES": # If input is yes
            state = "Water Usage in " + state + " for 2010 (Mgal/day)" # Format
            plot_water_usage(state_list, state) # Calls plot_water_usage()
        
        state = input("Enter state code or 'all' or 'quit': ").upper().strip()
    
if __name__ == "__main__": # if name == "main"
    main() # calls main function