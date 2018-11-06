###########################################################
#   Project 07
#
#   Prompts user for ip address location file
#   Prompts user for ip address attacks file
#   Prompts user for country codes file
#   Iterates through list of tuples of ip addresses
#   Stores ip address and corresponding country code
#   Appends ip address and country name to list
#   Counts how many times country has attacked
#   Sorts attacks by frequency 
#   Displays ip address of attack and country it originated from
#   Displays top ten countries with attack ip addresses
#   Plots top then countries with attack ip addresses
#   
###########################################################
    
import csv
import pylab
from operator import itemgetter

def open_file(message):
    """
    Opens file
    Prints error message if file name doesn't exist
    takes in a string
    message: input
    Returns: file
    """
   
    filename = input(message) # Prompt for file
    while True: # While loop
        try: # Try to:
            file = open(filename, "r") # Open file 
            return file # Return file
        except FileNotFoundError: # If FileNotFoundError:
            print("File is not found! Try Again!") # Print error message
            filename = input(message) # Reprompt for file
            
def read_ip_location(file): 
    """
    Iterate through line in file
    Appends start ip, end ip, and country code
    zfill(3) start ip and end ip
    Append tuples of start ip and end ip to list
    file: filename
    Returns: ip_list
    """
    ip_list = [] # Initialized list
    file = csv.reader(file) # Read csv file
   
    for line in file: # Iterate through each line in file
        start_ip_list = line[0].split(".") # Splits element at index 0 on .
        end_ip_list = line[1].split(".") # Splits element at index 1 on .
        country_code = line[2] # Country code at index 2
        
        start_ip = "" # Initialized string
        end_ip = "" # Initialized string
    
        for start_ele in start_ip_list: # Iterate through element in list
            start_ele = start_ele.zfill(3) # zfill(3) each element
            start_ip += start_ele # Append element to string
        start_ip = int(start_ip) # Integer type
        
        for end_ele in end_ip_list: # Iterate through element in list
            end_ele = end_ele.zfill(3) # zfill(3) each element
            end_ip += end_ele # Append element to string
        end_ip = int(end_ip) # Integer type

        ip_list.append((start_ip, end_ip, country_code)) # Append tuples 2 list

    return ip_list # Return list

def read_ip_attack(file):
    """
    Iterate through line in file
    Assign line to ip_str
    Iteratre through element in ip_int_str
    zfill(3) element
    Append element to ip_int
    Append ip_int and ip_str to list
    file: filename
    Returns: ip_attack_list
    """
    
    ip_attack_list = [] # Initialized list
    
    for line in file: # Iterate each line in file
        line = line.strip() # Strip whitespace
        ip_int_string = line.split(".") # Split each line on .
        ip_str = line # Assign line to ip_str
        ip_int = "" # Initialized string
        
        for int_ele in ip_int_string: # Iterate through element 
            int_ele = int_ele.zfill(3) # zfill(3) each element
            ip_int += int_ele # Append element to string
            
        ip_int += "000" # Append "000" string
        ip_int = int(ip_int) # Integer type      
        ip_str += ".xxx" # Append ".xxx" string
    
        ip_attack_list.append((ip_int, ip_str)) # Append tuples of ips to list
        
    return ip_attack_list # Return ip_attack_list

def read_country_name(file): 
    """
    Iterate through line in file
    Append country code and country name to list
    file: filename
    Returns: country_name_list
    """
    
    country_name_list = [] # Initialized list
        
    for line in file: # Iterate through line in file
        line = line.strip().split(";") # Strip whitespace and split on ;

        country_code = line[1] # Assign index 1 of each line to country_code
        full_name = line[0] # Assign index 0 of each line to full_name

        country_name_list.append((country_code, full_name)) # Append tuples
        
    return(country_name_list) # Return country_name_list

def locate_address(ip_list, ip_attack): 
    """
    Iterate through tuple in ip_list
    If ip_attack is found in list
    ip_list: list of ip addresses
    ip_attack: list of ip addresses that attacked
    Returns: tup[2]
    """
    
    for tup in ip_list: # Iterates through tuples in list
        if tup[1] > ip_attack >= tup[0]: # If ip address is between 2 addresses
        
            return tup[2] # Return tup[2]
    
def get_country_name(country_list, code): 
    """
    Iterate through tuple in country_list
    If country code is found in list
    country_list: list of countries
    code: list of country codes
    Returns: tup[1]
    """
    
    for tup in country_list: # Iterate through tuples in list
        if tup[0] == code: # If country code is found
            
            return tup[1] # Return country name

def bar_plot(count_list, countries):
    
    pylab.figure(figsize=(10,6)) 
    pylab.bar(list(range(len(count_list))), count_list, tick_label = countries)
    pylab.title("Countries with highest number of attacks")
    pylab.xlabel("Countries")
    pylab.ylabel("Number of attacks")
    
def main():
    """
    Prompt user for filename of ip locations
    Prompt user for filename of ip addresses of attacks
    Prompt user for filename of country names
    Iterate through tuple in list of ip addresses of attacks
    Assign country codes to list
    Assign country names to list
    Append ip strings to list
    Append country names to list
    If country code is not in list, append to list
    If country code is in list, add 1 to attack count
    Sort list of country codes in frequency
    Display data
    """
    file = open_file("Enter the filename for the IP Address location list: ")
    ip_data = read_ip_location(file) # Calls read_ip_location()
    
    file = open_file("Enter the filename for the IP Address attacks: ")
    attack_data = read_ip_attack(file) # Calls read_ip_attack()
    
    file = open_file("Enter the filename for the country codes: \n")
    country_data = read_country_name(file) # Calls read_country_name()
   
    attack_list = [] # Initialized list
    name_list = [] # Initialized list
    code_list = [] # Initialized list
    main_list = [] # Initialized list
    count_list = [] # Initialized list
    country_list = [] # Initialized list
    
    
    for tup in attack_data: # Iterate through tuples in list
        ip_attack = tup[0] # Ip integer
        ip_string = tup[1] # Ip string
        country_code = locate_address(ip_data, ip_attack) # Return country code
        country_name = get_country_name(country_data, country_code) # Name   
        attack_list.append(ip_string) # Append ip strings to list
        name_list.append(country_name) # Append country name to list
        
        if country_code not in code_list: # If country code not in list:
            code_list.append(country_code) # Append country code
            main_list.append([country_code, 1]) # Append country code and count
        else:
            for lst in main_list: # Iterate through list in list
                if country_code == lst[0]: # If code in list
                    lst[1] += 1 # +1 to counter
                    break # break from loop
    
    new_list = [] # Initialized list
    sorted_list = [] # Initialized list
    
    for el in main_list: # Iterate through list in list
        new_list.append(tuple(el)) # Append list to list           

    new_list.sort(key = itemgetter(1,0), reverse = True) # Sort list
    
    for ele in range(10): # Iterate through element 10 times
        sorted_list.append(new_list[ele]) # Append element in list to list
        country_list.append(new_list[ele][0]) # Append country code to list
        count_list.append(new_list[ele][1]) # Append attack count to list
        
    i = 0 # Initialized variable for index
    data_answer = input("Do you want to display all data? ") # Prompt for input
    if data_answer.lower() == "yes": # Accounts for lower and upper case
        for name in name_list: # Iterates through names in list
            print("The IP Address: {:18s} originated from {}"\
                  .format(attack_list[i], name_list[i]))
            i += 1 # Add 1 to variable
        print("\nTop 10 Attack Countries\nCountry  Count")
        
        for element in sorted_list: # Iterate through element in list
            print("{} {:11d}".format(element[0], element[1])) 
    if data_answer.lower == "no": # Accounts for upper and lower case
        for element in sorted_list: # Iterate through element in list
            print("{} {:11d}".format(element[0], element[1]))   
    
    answer = input("\nDo you want to plot? ") # Prompt for input
    if answer.lower() == "yes": # If input is yes
        bar_plot(count_list, country_list) # Calls bar_plot()
    if answer.lower() == "no": # If input is no
        pass # pass
      
if __name__ == "__main__":
    main() # Call main()
    
