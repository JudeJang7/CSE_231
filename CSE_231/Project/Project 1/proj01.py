###########################################################
# CSE 231 Programming Project #1
# Unit Conversions of Rods
#
# Program prompts user to input number of rods 
# Converts rods to:
# Meters
# Feet
# Miles
# Furlongs
# Minutes to walk
###########################################################

rods_str = input("Input rods: ") # Prompt user to input number of rods
RODS = float(rods_str) # Convert string to float
print("You input", RODS, "rods.") # State how many rods were inputted
print() # Newline

#         Constants         #
RODS_TO_METERS= 5.0292 # Rods to Meters
RODS_TO_FEET= 5.0292 / .3048 # Rods to Feet
RODS_TO_MILES = 5.0292 / 1609.34 # Rods to Miles
RODS_TO_FURLONGS = 1 / 40 # Rods to Furlongs
RODS_TO_MINUTES_TO_WALK = 5.0292 / 1609.34 / 3.1 * 60 # Rods to Minutes to walk

#         Calculations         #
METERS = (RODS * RODS_TO_METERS)
FEET = (RODS * RODS_TO_FEET)
MILES = (RODS * RODS_TO_MILES)
FURLONGS = (RODS * RODS_TO_FURLONGS)
MINUTES_TO_WALK = (RODS * RODS_TO_MINUTES_TO_WALK)

print("Conversions") # Conversions rounded to three decimal places
print("Meters:", round(METERS, 3))
print("Feet:", round(FEET, 3))
print("Miles:", round(MILES, 3))
print("Furlongs:", round(FURLONGS, 3))
print("Minutes to walk", RODS, "rods:", round(MINUTES_TO_WALK, 3))