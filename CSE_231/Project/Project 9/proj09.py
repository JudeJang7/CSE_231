###########################################################
# Programming Project #5
# 
# Prompts user for valid file
# Calculates the top three hashtags tweeted overall
# Calcualtes the top three hashtags tweeted by individuals
# Prints list of usernames
# Prompts for two valid users
# Calculates number of similar hashtags by month
# Prompts user to plot
# Prints data in graph format
#
###########################################################

import string, calendar, pylab
from operator import itemgetter

MONTH_NAMES = [calendar.month_name[month] for month in range(1,13)]

def open_file():
    '''Returns: filepointer'''
    
    filename = input("Input a filename: ")
    
    # Prompts for file and tries to open
    # If file does not exist, print error message and reprompt for file
    while True:
        try:
            fp = open(filename, "r")
            return fp
        except FileNotFoundError:
            print("Error in input filename. Please try again.")
            filename = input("Input a filename: ")

def validate_hashtag(s):
    '''s: tweet where valid hashtags get collected'''
    # Initializes a list of punctuation excluding #
    invalidchar = set(string.punctuation.replace("#",""))
    
    # Validates hashtag
    if any(char in invalidchar for char in s):
        return False
    elif len(s[1:]) == 1:
        return False
    else:
        return True

def get_hashtags(s):
    '''s: tweet where hashtags are found
        Returns: list of valid hashtags'''
    
    valid_hashtags = []
    s += " "
    beginning = s.find('#')
    end = s.find(' ', beginning)
    
    # Finds the beginning and end of each hashtag in a tweet
    while(beginning != -1):
        boolean = validate_hashtag(s[beginning:end])
        if boolean == True:
            valid_hashtags.append(s[beginning:end])
            beginning = s.find('#', end)
            end = s.find(' ', beginning) 
        if boolean == False:
            beginning = s.find('#', end)
            end = s.find(' ', beginning) 
            
    return valid_hashtags        

def read_data(fp):
    '''fp: filepoints
        Returns: data, a list of usernames, months, hashtags'''
    
    data = []
    
    # Initalizes a list for each line in file
    # Initializes variables depending on index of list
    for line in fp:
        line = line.strip().split(",")
        username = line[0]
        month = int(line[1])
        hashtags = (get_hashtags(line[2]))
        tweet_data = [username, month, hashtags]
        data.append(tweet_data)

    return data    
    
def get_histogram_tag_count_for_users(data, usernames):
    '''data: list of usernames, months, hashtags
        usernames: list of usernames
        Returns: dictioanry with username and count as key value pair'''
    
    histogram = {}
    
    # Creates dictionary with hashtag as key and count as value
    for lists in data:
        username = lists[0]
        hashtags = lists[2]
        if username in usernames:
            for hashtag in hashtags:
                if hashtag not in histogram:
                    histogram[hashtag] = 1
                else:
                    histogram[hashtag] += 1
                       
    return histogram              

def get_tags_by_month_for_users(data, usernames):
    '''data: list of usernames, months, hashtags
        usernames: list of usernames
        Returns: list of tuples with months and hashtags as key value pair'''
    
    # Creates a list of months as integers
    hashtags_by_months = []
    months = 0
    for i in range(0,12):
        months += 1
        hashtags_by_months.append((months, set()))  

    # Creates list of of tuples with months as key and hashtags as values
    for lists in data:
        username = lists[0]
        month = int(lists[1])
        hashtags = lists[2]
        if username in usernames:        
            for hashtag in hashtags:
                month_index = month - 1
                hashtags_by_months[month_index][1].add(hashtag)      
                
    return hashtags_by_months        
        
def get_user_names(data):
    '''data: list of usernames, months, hashtags
        Returns: list of usernames'''
    
    usernames = []
    
    # Creates a list of usernames based off file
    for lists in data:
        usernames.append(lists[0])
        usernames = sorted(set(usernames))
        
    return usernames    

def three_most_common_hashtags_combined(data, usernames):
    '''data: list of usernames, months, hashtags
        usernames: list of usernames
        Returns: list of top three hashtags and their counts overall'''
    
    combined = []
    
    # Calculates the top three most common hashtags of all users
    histogram = get_histogram_tag_count_for_users(data, usernames)
    histogram = sorted([(v, k) for k, v in histogram.items()], reverse=True)
    
    for i in range(0,3):
        combined.append(histogram[i])
    
    return combined        

def three_most_common_hashtags_individuals(data, usernames):
    '''data: list of usernames, months, hashtags
        usernames: list of usernames
        Returns: list of top three hashtags and their counts by users'''
    
    lists = []
    individuals = []

    # Calculates the top three most common hashtags by individuals
    for username in usernames:
        histogram = get_histogram_tag_count_for_users(data, username)
        histogram = [(v, k) for k, v in histogram.items()]
        for tup in histogram:
            final_tup = (tup[0], tup[1], username)
            lists.append(final_tup)
    
    lists.sort(key = itemgetter(0), reverse = True)
    
    for i in range (0,3):
        individuals.append(lists[i])
        
    return individuals
    
def similarity(data, user1, user2):
    '''data: list of usernames, months, hashtags
        user1: first user inputted
        user2: second user inputted
        Returns: list of months and count of shared hashtags'''

    similar = []

    histogram1 = get_tags_by_month_for_users(data, user1)
    histogram2 = get_tags_by_month_for_users(data, user2)
    
    # Calculates which hashtags were used between both users 
    for i in range(0,12):
        intersect = histogram1[i][1].intersection(histogram2[i][1])
        tag_set = (i + 1, intersect)
        similar.append(tag_set)
        
    return similar  
        
def plot_similarity(x_list,y_list,user1,user2):
    '''Plot y vs. x with user1 and user2 in the title.'''
    
    pylab.plot(x_list,y_list)
    pylab.xticks(x_list,MONTH_NAMES,rotation=45,ha='right')
    pylab.ylabel('Hashtag Similarity')
    pylab.title('Twitter Similarity Between '+user1+' and '+user2)
    pylab.tight_layout()
    pylab.show()
    # the next line is simply to illustrate how to save the plot
    # leave it commented out in the version you submit
    #pylab.savefig("plot.png")


def main():
    
    fp = open_file() 
    data = read_data(fp)  
    usernames = get_user_names(data)   
    
    # Calculates the top three hashtags combined for all users
    print()
    print("Top Three Hashtags Combined")
    print("{:>6s} {:<20s}".format("Count","Hashtag")) 
    combined = three_most_common_hashtags_combined(data, usernames) 
    for hashtags in combined:
        print("{:>6d} {:<20s}".format(hashtags[0], hashtags[1]))
    print()
    
    # Calculates the top three hashtags individually for all users
    print("Top Three Hashtags by Individual")
    print("{:>6s} {:<20s} {:<20s}".format("Count","Hashtag","User"))
    individuals = three_most_common_hashtags_individuals(data, usernames)
    for hashtags in individuals:
        print("{:>6d} {:<20s} {:<20s}".format(hashtags[0],hashtags[1],hashtags[2]))
    print()
    
    # Prompts for two user names from username list
    user_str = ", ".join(usernames)
    print("Usernames: ", user_str)
    
    while True:
        two_users = input("Input two user names from the list, comma separated: ")
        
        while True:
            two_user = two_users.strip().split(",")
            
            # If two usernames are not inputted, print error message and reprompt
            if len(two_user) != 2:
                print("Error in user names.  Please try again")
                two_users = input("Input two user names from the list, comma separated: ")
                two_user = two_users.strip().split(",")
            user1 = two_user[0].strip()
            user2 = two_user[1].strip()
            
            # If usernames don't exist, print error message and reprompt
            if user1 not in usernames or user2 not in usernames: 
            
                print("Error in user names.  Please try again")
                two_users = input("Input two user names from the list, comma separated: ")
                two_user = two_users.strip().split(",")
                user1 = two_user[0].strip()
                user2 = two_user[1].strip()
            
            break
            
        # If usernames exist, calculates similar hashtags used by users    
        if user1 and user2 in usernames:       
            print()
            print("Similarities for "+user1+" and "+user2)
            print("{:12s}{:6s}".format("Month","Count"))
            months = ["January", "February", "March", "April", "May", "June", 
                      "July", "August", "September", "October", "November",
                      "December"]
            
            similar = similarity(data, [user1], [user2])
            i = 0
            
            for tup in similar:        
                print("{:12s}{:<6d}".format(months[i],len(tup[1])))
                i += 1
            print() 
            
            # If answer is yes, plots data
            choice = input("Do you want to plot (yes/no)?: ")     
            if choice.lower() == 'yes':
                x_list = []
                y_list = []
                for tup in similar:
                    x_list.append(tup[0])
                    y_list.append(len(tup[1]))
                plot_similarity(x_list,y_list,user1,user2)
            else:
                break
        break
        
if __name__ == '__main__':
    main()