def read_file(file, D):
    header = file.readline()

    
    
    for line in file:
        line = line.strip().split()
        name = line[0]
        value = int(line[1]) 
        if name in D:
            D[name] += value
        else:
            D[name] = value
            
          
def display_data(D):
  
    score_list = list()
    for name, value in D.items():
        score_list.append((name, value))
    score_list.sort()
        
    print("{:10s} {:<10s}".format("Name", "Score"))
    for line in score_list:
        print("{:10s} {:<10d}".format(line[0], line[1]))
    

    
def main():
    D = {}
    
    fp = open("data1.txt", 'r')
    fp2 = open("data2.txt", 'r')
    
    read_file(fp, D)
    read_file(fp2, D)
    display_data(D)
    
    
main()

    