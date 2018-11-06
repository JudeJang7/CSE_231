###########################################################
#  CSE 231 Programming Project 02
#  Change-Making Program
#  
#  Print stock of coins
#  Prompt user for purchase price
#  Prompt user for payment
#  Calculate change
#  Pay user in quarters, dimes, nickels, pennies
#   
###########################################################

# Stock of coins
quarters = 10
dimes = 10
nickels = 10
pennies = 10

# Welcome to Change-Making Program
print("\nWelcome to change-making program.")

# Print Stock of coins
print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

# Prompt user for purchase price
in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
enough_stock = True
stop = False

# Beginning of calculations
while in_str != 'q' and enough_stock == True and not stop:
    
    # Amount of coins used
    quarters_count = 0
    dimes_count = 0
    nickels_count = 0
    pennies_count = 0   
    
    # Value of coins
    QUARTERS_VALUE = 25
    DIMES_VALUE = 10
    NICKELS_VALUE = 5
    PENNIES_VALUE = 1 
    
    # Convert string to float to integer in cents
    price_float = float(in_str) * 100
    price = int(price_float) 
    
    # Error message for negative price
    if price < 0:
        print("Error: purchase price must be non-negative.")  
        
    # Calculate change   
    if price > 0 and quarters + dimes + nickels + pennies != 0:
       paid_str = input("Input dollars paid (int): ")
       paid_float = float(paid_str) * 100
       paid = int(paid_float)     
       change = paid - price      
       
       # Error message for insufficient payment
       while change < 0:
           print("Error: insufficient payment.")  
           paid_str = input("Input dollars paid (int): ")      
           paid_float = float(paid_str) * 100
           paid = int(paid_float)     
           change = paid - price         
           
       # Message for exact payment    
       else:          
           if change == 0:
               print("No change.")             
               
           # Error message for ran out of coins    
           while change > 0 and enough_stock == True:            
               if quarters + dimes + nickels + pennies == 0 and change != 0:
                   enough_stock = False
                   print("Error: ran out of coins.")
                   stop = True
                   break
                
               # Change in quarters 
               elif change >= QUARTERS_VALUE and quarters > 0:
                   change = change - QUARTERS_VALUE
                   quarters = quarters - 1
                   quarters_count += 1   
                   
               # Change in dimes    
               elif change >= DIMES_VALUE and dimes > 0:
                   if change != 0:
                       change = change - DIMES_VALUE
                       dimes = dimes - 1
                       dimes_count += 1  
                       
               # Change in nickels        
               elif change >= NICKELS_VALUE and nickels > 0:
                   if change != 0:
                       change = change - NICKELS_VALUE
                       nickels = nickels - 1
                       nickels_count += 1      
                       
               # Change in pennies        

               elif change >= PENNIES_VALUE and pennies > 0:
                   if change != 0:
                       change = change - PENNIES_VALUE
                       pennies = pennies - 1
                       pennies_count += 1
                       
    # Message for collect change below
    if (quarters_count + dimes_count + nickels_count + pennies_count > 0 
    and not stop):
        print()
        print("Collect change below:")   
        
        # Amount of quarters given
        if quarters_count > 0:    
            print("Quarters:" , quarters_count)       
            
        # Amount of dimes given    
        if dimes_count > 0:      
            print("Dimes:" , dimes_count)
            
        # Amount of nickels given   
        if nickels_count > 0:
            print("Nickels:" , nickels_count)  
            
        # Amount of pennies given   
        if pennies_count > 0:      
            print("Pennies:" , pennies_count)   
            
    # End of loop                    
    if quarters + dimes + nickels + pennies != 0 and not stop:   
        
        # Remaining stock
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies"
              .format(quarters, dimes, nickels, pennies))
        
        # Prompt user for remaining payment
        in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")