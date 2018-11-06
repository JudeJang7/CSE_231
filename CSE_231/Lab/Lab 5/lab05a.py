infile = open("data.txt", "r")

height_total = []
weight_total = []
bmi_total = []
names = []
header = "{:<12s}{:<12s}{:<12s}{:<12s}".format("Name", "Height(m)", "Weight(kg)", " BMI")
for i in infile:
    try:
        height_total.append(float(i[12:24]))
        weight_total.append(float(i[24:36]))
        names.append(i[0:12])
    except ValueError:
        pass

for w, h in zip(weight_total, height_total):
    bmi_total.append(float(w)/(float(h) ** 2))

average3 = (sum(bmi_total)/len(bmi_total))
max3 = max(bmi_total)
min3 = min(bmi_total)
    


average1 = (sum(height_total)/len(height_total))
max1 = (max(height_total))
min1 = (min(height_total))

average2 = (sum(weight_total)/len(weight_total))
max2 = max(weight_total)
min2 = min(weight_total)




outfile = open("data1.txt", "w")
outfile.write((header))
for n,h,w,bmi in zip(names,height_total, weight_total, bmi_total):
    outfile.write("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(n,h,w,bmi))
outfile.write("\n")
outfile.write("\n")
outfile.write("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average",average1, average2, average3))
outfile.write("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max",max1, max2, max3))
outfile.write("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min",min1, min2, min3))
outfile.close()
