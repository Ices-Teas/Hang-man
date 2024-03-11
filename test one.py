# ask for student id
id = eval(input("please enter your student ID: "))
# to store the grade
grade = []
# to know how many subject
sub = eval(input("how many subject do you have? "))

# checking for correct number of subject which is either 5 or below 5
while not sub < 6:
    print("there is no way you have", sub, "many subject go back and put the correct number")
    sub = eval(input("how many subject do you have? "))


# calculating each mark 
for x in range (1, sub + 1):
    # ask the name of the class
    classes = str(input("please enter the name of class: "))
    # to know which subject is asking for mark
    print("calculation for", classes)
    # ask for tutorial count and tutorial mark
    tutorial = eval(input("please enter the total count of tutorials: "))
    tutorial_mark = eval(input("please enter the total tutorials mark: "))
    # ask for test and test mark
    test = eval(input("please enter your total test count: ")) 
    test_mark = eval(input("please enter your test mark: "))
    # calculating total percentage of test and tutorial
    total_percentage = (tutorial_mark + test_mark) / (tutorial + test) * 0.5 * 100
    # checking if student failed
    if total_percentage < 40:
        print ("you cant do the final examination because you failed the subject, you got F ")
        grade.append(classes)
        grade.append("F")
        continue
    # calculating final exam percentage
    final_mark = eval(input("please enter your final examination mark: "))
    final_exam_percentage = final_mark / 100 * 0.5 * 100
    # getting the final final score
    total_score = final_exam_percentage + total_percentage
    # assigning grade
    if 80<= total_score <= 100:
        print("nicely done you got an A")
        grade.append(classes)
        grade.append("A")
    elif 70 <= total_score < 80:
        print("a B is still good")
        grade.append(classes)
        grade.append("B")
    elif 60 <= total_score < 70:
        print("could have done better, grade  C")
        grade.append(classes)
        grade.append("C")
    elif 50 <= total_score < 60:
        print("come on now, go start studying, grade D")
        grade.append(classes)
        grade.append("D")
    else:
         print("bruh your parent is disappointed, grade E")
         grade.append(classes)
         grade.append("E")
# output the student id
print("grade for: ", id )

# output all grade
for x in grade:
    print(x)

