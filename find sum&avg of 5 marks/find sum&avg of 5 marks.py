print("please enter your 5 marks below")

# read 5 inputs
mark1 = input("enter mark 1: ")
mark2 = input("enter mark 2: ")
mark3 = input("enter mark 3: ")
mark4 = input("enter mark 4: ")
mark5 = input("enter mark 5: ")

# if value isnt int change to 0
if mark1.isdigit():
    print(mark1, " is digit")
else:
    print(mark1, "is not digit")
# create array/list with five marks
marksList = [int(mark1), int(mark2), int(mark3), int(mark4), int(mark5)]

# print the array/list
print(marksList)

# calculate the sum and average
sumOfMarks = sum(marksList)
averageOfMarks = sum(marksList)/5

# display results
print("The sum of your marks is: "+str(sumOfMarks))
print("The average of your marks is: "+str(averageOfMarks))
