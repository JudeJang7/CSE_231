n_str = input("Input an integer (0 terminates): ")
my_int = int(n_str)

odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
positive_int_count = 0

while my_int != 0:
    if my_int < 0:
        print("Invalid number entered")
    elif my_int%2 == 0:
        even_count += 1
        even_sum += my_int
    else:
        odd_count += 1
        odd_sum += my_int
    n_str = input("Input an integer (0 terminates): ")
    my_int = int(n_str)    
    
positive_int_count = even_count + odd_count

print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)