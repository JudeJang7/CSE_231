###########################################################
# Programming Project #5
# 
# Define open_file function:
# Tries to read user inputted file
# If FileNotFoundError, prints error message and reprompts user
#
# Define revenue() function
# Calculates revenue
#
# Define cost_of_goods_sold() function
# Calculates advertising total and production total
# Calculates cost of goods sold using advertising total and production total
#
# Define calculate_ROI() function
# Calculates ROI using revenue and cost of goods sold
#
# Define main() function
# Opens user inputted file
# Reads file
# Iterates through file
# Saves product name and best selling ads number and best ROI
# Prints product names with best selling ads number and best ROI
#
# Calls main() function
###########################################################

# Define open_file() function
def open_file():
    '''prompt for file name, open file, return file pointer'''
    
    # Prompt user for file name
    user_input = input("Input a file name: ")
    
    # Try to open user inputted file
    while True:
        try:
            fp = open(user_input)
            return fp
        # If FileNotFoundError, print error message and reprompt user
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
            user_input = input("Input a file name: ")
    
# Define revenue() function    
def revenue(num_sales, sale_price):
    '''revenue = sales * price'''
    
    # Calculate revenue
    r = num_sales * sale_price

    return r

# Define cost_of_goods_sold() function
def cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost):
    '''costs of goods sold = advertising total + production total'''
    
    # Calculate advertising total, production total, cost of goods sold
    advertising_total = num_ads * ad_price
    production_total = num_sales * production_cost
    c_o_g_s = advertising_total + production_total
    
    return c_o_g_s

# Define calculate_ROI() function
def calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost):
    '''ROI = (Revenue - Cost of goods sold)/Cost of goods sold'''
    
    # Calculate revenue, cost of goods sold, return on investment
    r = revenue(num_sales, sale_price)
    c_o_g_s = cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost)
    ROI = (r - c_o_g_s)/c_o_g_s

    return ROI

# Define main() function
def main():

    # Open user inputted file
    fp = open_file()
    
    # Some print lines to match formatting in Mimir tests
    print()
    print("RobCo AdStats M4000")
    print("-------------------")
    print() 
    
    # Initalized variables
    previous_product = ""
    previous_ad_sales = ""
    previous_ad_ROI = ""
    best_sales = 0
    best_ROI = 0
    
    # Read the file
    for line in fp:
        line = line.strip()
        
        # Extract the data 
        product = line[0:27]
        ad = line[27:54]
        num_ads = line[54:62]
        ad_price = line[62:70]
        num_sales = line[70:78]
        sale_price = line[78:86]
        production_cost = line[86:94]
        
        # Convert variables to int and float types
        num_ads = int(num_ads)
        ad_price = float(ad_price)
        num_sales = int(num_sales)
        sale_price = float(sale_price)
        production_cost = float(production_cost)
        
        # Call calculate_ROI() function
        ROI = calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost)
              
        # print each product's best selling ad sales number, and best ROI
        
        # Keep track of previous product
        # Keep track of ad associated with best selling ad sales number
        # Keep track of ad associated with best ROI
        if previous_product == "" :
            previous_product = product
        if previous_ad_sales == "":
            previous_ad_sales = ad
        if previous_ad_ROI == "":
            previous_ad_ROI = ad
          
        # If product name changes:
        # Print previous product
        # Print ad and best selling ad sales number
        # Print ad and best ROI
        if product != previous_product:
            print(previous_product)
            print("  {:27s}{:>11s}".format("Best-Performing Ad", "sales"))
            print("  {:27s}{:>11d}".format(previous_ad_sales, best_sales))
            print() 
            print("  {:27s}{:>11s}".format("Best ROI", "percent"))
            print("  {:27s}{:>11.2%}".format(previous_ad_ROI, best_ROI/100))
            print()
            
            # If product changes:
            # Resets best selling ad sales number and best ROI
            best_sales = 0
            best_ROI = 0
            
        # If current number of sales is bigger:
        # Best selling ad sales number is now equal to current number of sales
        # Previous ad is now current ad
        # Move onto next product
        if num_sales > best_sales:
            best_sales = num_sales 
            previous_ad_sales = ad
        previous_product = product    

        # If current ROI is bigger:
        # Best ROI is now equal to current ROI
        # Previous ad is now current ad
        # Move onto next product
        if ROI > best_ROI:
            best_ROI = ROI
            previous_ad_ROI = ad
        previous_product = product
        
    # Else statement for last product 
    # Print last product
    # Print ad and best selling ad sales number
    # Print ad and best ROI   
    else: 
        print(product)
        print("  {:27s}{:>11s}".format("Best-Performing Ad", "sales"))
        print("  {:27s}{:>11d}".format(previous_ad_sales, best_sales))
        print()
        print("  {:27s}{:>11s}".format("Best ROI", "percent"))
        print("  {:27s}{:>11.2%}".format(previous_ad_ROI, best_ROI/100))
        
# Calls main() function        
if __name__ == "__main__":
    main()