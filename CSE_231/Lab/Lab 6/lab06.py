in_file = open("scores.txt", "r")
big_list = []
exam1s = 0
exam2s = 0
exam3s = 0
exam4s = 0
for line in in_file:
    line1 = line.split()
    last_name = line1[0]
    first_name = line1[1]
    exam_scores = line1[2:6]
    for i, score in enumerate(exam_scores):
        exam_scores[i] = int(score)
    mean = exam_scores[0] + exam_scores[1] + exam_scores[2] + exam_scores[3]
    mean = mean/4
    list1 = [last_name,first_name,exam_scores[0],exam_scores[1],exam_scores[2],exam_scores[3],mean]
    tuple1 = tuple(list1)
    big_list.append(tuple1)

big_list.sort()
print("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format("Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))
for student in big_list:
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(student[0]+student[1], student[2], student[3], student[4], student[5], student[6]))
    exam1s += student[2]
    exam2s += student[3]
    exam3s += student[4]
    exam4s += student[5]

mean1 = exam1s / 5
mean2 = exam2s / 5
mean3 = exam3s / 5
mean4 = exam4s / 5
print("{:20s}{:6.2f}{:6.2f}{:6.2f}{:6.2f}".format("Exam Mean", mean1, mean2, mean3, mean4))