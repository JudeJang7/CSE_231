###########################################################
# Programming Project 08
#  
# Prompt user for file
# Prompt user for year
# Display hurricane data for year
# Ask user to plot 
# Prompt for year
# If answer is yes, plot map and wind chart
###########################################################

import pylab as py

def open_file():
    '''Returns fp'''
    
    # Try to open file,
    # If file does not exist,
    # Prompt for valid file
    file = input("Input a file name: ") 
    while True: 
        try: 
            fp = open(file, "r") 
            return fp
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
            file = input("Input a file name: ")

def update_dictionary(dictionary, year, hurricane_name, data):
    '''dictionary: Dictionary of dictionaries
        year: key of dictionary
        hurricane_name: key of nested dictionary
        data: value of nested dictionary
        Returns: updated dictionary'''
    
    data_list = []
    
    # If year does not exist,
    # Create dictionary for year
    # Assign dictionary with hurricane name: data pair to year
    if year not in dictionary: 
        dictionary[year] = {} 
        data_list.append(data)
        dictionary[year][hurricane_name] = data_list
        
    # If year does exist, but hurricane doesn't exist,
    # Assign dictionary with hurricane name: data pair to year 
    elif year in dictionary and hurricane_name not in dictionary[year]: 
        data_list.append(data) 
        dictionary[year][hurricane_name] = data_list
    
    # If year does exist, and hurricane does exist,
    # Append data tuple to list for year and hurricane
    else:            
        data_list = dictionary[year][hurricane_name]
        data_list.append(data)
        dictionary[year][hurricane_name] = data_list

    return dictionary
    
def create_dictionary(fp):
    '''fp: file
        Returns: data appended to dictionary'''
    
    dictionary = {}

    # Iterate through each line in file,
    # Create list for each line
    for line in fp:
        line = line.strip().split()
        
        # Variables for each line
        year = line[0]
        hurricane_name = line[1]
        lat = float(line[3])
        lon = float(line[4])
        date = line[5]
        if line[6].isdigit():
            wind = float(line[6])
        else:
            wind = 0
        if line[7].isdigit():  
           pressure = float(line[7])
        else:
            pressure = 0    
    
        data = ((lat, lon, date, wind, pressure))  
        update_dictionary(dictionary, year, hurricane_name, data) 

    return dictionary

def display_table(dictionary, year):
    '''dictionary: dictionary of dictionaries
        year: key of dictionary
        Prints formatted table of data'''

    hurricane_names = []
    peak_wind = 0

    # Iterate through each hurricane in year
    # Append hurricane name to list
    for name in dictionary[year]:
        hurricane_names.append(name)
        
    hurricane_names = sorted(hurricane_names)
    
    print("{:^70s}".format("Peak Wind Speed for the Hurricanes in " + year))
    print("{:15s}{:>15s}{:>20s}{:>15s}".format\
          ("Name","Coordinates","Wind Speed (knots)","Date"))
    
    # Find peak wind speed for each hurricane
    # Find coordinate and date corresponding to peak wind speed
    # If multiple peak wind speeds, pick the larger latitude
    # If multiple peak wind speeds and latitudes, pick the larger longitude
    for name in hurricane_names:      
        for l in dictionary[year][name]:
            if l[3] >= peak_wind:
                if l[3] > peak_wind:
                    peak_wind = l[3]
                    lat = l[0]
                    lon = l[1]
                    date = l[2]
                else:
                    if l[0] >= lat:
                        if l[0] > lat:
                            lat = l[0]
                            lon = l[1]
                            date = l[2]
                        else:
                            if l[1] > lon:
                                lat = l[0]
                                lon = l[1]
                                date = l[2]                  
                                    
        print("{:15s}({:>6.2f},{:.2f}){:>20.2f}{:>15s}".format(name, lat, lon, peak_wind, date)) 

        peak_wind = 0
        lat = 0
        lon = 0    
        date = ""
    
def get_years(dictionary):
    '''dictionary: dictionary of dictionaries
        Returns: tuple containing lowest and highest years'''
    
    years = []
    
    # Iterate through each key in dictionary
    # Append keys to list
    for key in dictionary:
        years.append(key)
    
    years.sort()   
    
    min_year = years[0]
    max_year = years[-1]
    
    return (min_year, max_year)

def prepare_plot(dictionary, year):
    '''dictionary: dictionary of dictionaries
        year: key of dictionary
        Returns: tuple containing hurricane_names, coordinates, max_speed'''
    
    hurricane_names = []
    max_speed = []
    coordinates = []
    
    # Iterate through each hurricane in dictionary
    # Append hurricane name to list
    for name in dictionary[year]:
        hurricane_names.append(name)
        
    hurricane_names.sort()    
    
    # Iterate through hurricane names
    for name in hurricane_names:    
        peak_wind = 0
        data_for_hurricane = []
        
        # Iterate through data for each hurricane
        # Append latitude and longitude to list
        # Find peak wind speed for each hurricane
        for l in dictionary[year][name]:
            data_for_hurricane.append((l[0], l[1]))
            if l[3] >= peak_wind:
                if l[3] > peak_wind:
                    peak_wind = l[3]

        max_speed.append(peak_wind)
        coordinates.append(data_for_hurricane)         
                
    return (hurricane_names, coordinates, max_speed)
    
def plot_map(year, size, names, coordinates):
    '''year: Inputted year 
        size: amount of hurricanes
        coordinates: latitude and longitude
        Plots map
        '''
    
    # The the RGB list of the background image
    img = py.imread("world-map.jpg")

    # Set the max values for the latitude and longitude of the map
    max_longitude, max_latitude = 180, 90
    
    # Set the background image on the plot
    py.imshow(img,extent=[-max_longitude,max_longitude,\
                          -max_latitude,max_latitude])
    
    # Set the corners of the map to cover the Atlantic Region
    xshift = (50,190) 
    yshift = (90,30)
    
    # Show the atlantic ocean region
    py.xlim((-max_longitude+xshift[0],max_longitude-xshift[1]))
    py.ylim((-max_latitude+yshift[0],max_latitude-yshift[1]))
	
    # Generate the colormap and select the colors for each hurricane
    cmap = py.get_cmap('gnuplot')
    colors = [cmap(i/size) for i in range(size)]
    
    # plot each hurricane's trajectory
    for i,key in enumerate(names):
        lat = [ lat for lat,lon in coordinates[i] ]
        lon = [ lon for lat,lon in coordinates[i] ]
        py.plot(lon,lat,color=colors[i],label=key)

     # Set the legend at the bottom of the plot
    py.legend(bbox_to_anchor=(0.,-0.5,1.,0.102),loc=0, ncol=3,mode='expand',\
              borderaxespad=0., fontsize=10)
    
    # Set the labels and titles of the plot
    py.xlabel("Longitude (degrees)")
    py.ylabel("Latitude (degrees)")
    py.title("Hurricane Trayectories for {}".format(year))
    py.show() # show the full map

def plot_wind_chart(year,size,names,max_speed):
    '''year: Inputted year
        size: amount of hurricanes
        names: list of hurricane names
        max_speed: peak wind speed for hurricane
        Plots wind chart'''
    
    # Set the value of the category
    cat_limit = [ [v for i in range(size)] for v in [64,83,96,113,137] ]
    
    # Colors for the category plots
    COLORS = ["g","b","y","m","r"]
    
    # Plot the Wind Speed of Hurricane
    for i in range(5):
        py.plot(range(size),cat_limit[i],COLORS[i],label="category-{:d}".format(i+1))
        
    # Set the legend for the categories
    py.legend(bbox_to_anchor=(1.05, 1.),loc=2,\
              borderaxespad=0., fontsize=10)
    
    py.xticks(range(size),names,rotation='vertical') # Set the x-axis to be the names
    py.ylim(0,180) # Set the limit of the wind speed
    
    # Set the axis labels and title
    py.ylabel("Wind Speed (knots)")
    py.xlabel("Hurricane Name")
    py.title("Max Hurricane Wind Speed for {}".format(year))
    py.plot(range(size),max_speed) # plot the wind speed plot
    py.show() # Show the plot
    
def main():
    '''open_file: opens file
        create_dictionary: creates dictionary of dictionaries
        get_years: retrieves min and max years
        display_table: displays formatted table of data
        prepare_plot: retrieves tuple containing data
        plot_map: plots map
        plot_wind_chart: plots wind chart
        '''
    
    # Open file
    # Create dictionary of dictionaries
    fp = open_file()
    dictionary = create_dictionary(fp)
    
    # Call get_years to find min and max years
    min_year = get_years(dictionary)[0]
    max_year = get_years(dictionary)[1]
    years = []

    # Iterate through each year in dictionary
    # Append years to list
    for key in dictionary:
        years.append(key)

    print("Hurricane Record Software")
    print("Records from {:4s} to {:4s}".format(min_year, max_year))
    
    # Prompt for year
    year = input("Enter the year to show hurricane data or 'quit': ")
    
    # While user does not input quit
    # If year exists, display data for year
    # If year does not exist, prompt for valid year
    while year.lower() != "quit":
        if year in years:
            display_table(dictionary, year)
            
            # Prompt user to plot
            # Prompt for year        
            answer = input("\nDo you want to plot? ")   
            
            # If answer is yes
            # Plot map and wind chart
            if answer.lower() == "yes":
                names, coordinates, max_speed = prepare_plot(dictionary, year)
                size = len(names)
                plot_map(year, size, names, coordinates)
                plot_wind_chart(year, size, names, max_speed)
            else:
                pass
            
            year = input("Enter the year to show hurricane data or 'quit': ")
           
        else:   
            print("Error with the year key! Try another year")
            year = input("Enter the year to show hurricane data or 'quit': ")
        
if __name__ == "__main__":
    main()