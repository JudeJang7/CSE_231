def open_file():

    user_input = input("Input a file name: ")
    while True:
        try:
            fp = open(user_input)
            return fp
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
            user_input = input("Input a file name: ")
            
count_list =  [0] * 9
first_dig = 0
line_list = ['30.1%','17.6%','12.5%','9.7%','7.9%','6.7%','5.8%','5.1%','4.6%']

fp = open_file()
for line in fp:
    line = line.strip()
    if line[0] != '0':
        first_dig = int(line[0])
        count_list[first_dig -1] += 1
     
total_sum = 0
total_sum = sum(count_list)
place = 0

print("Digit Percent Benford")

for place, elem in enumerate(count_list):
        print("{:>6s}:{:>7.1%} ({:>5s})".format(str(place+1), elem/total_sum , line_list[place])) 