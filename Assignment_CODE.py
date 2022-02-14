# Assignment 1

# Write a Python program to find average of three numbers entered by the user

print("-------1------\n")
print("To find average of three numbers")
First_num = float(input("Enter the first number   :   "))
Second_num = float(input("Enter the second number  :   "))
Third_num = float(input("Enter the third number   :   "))
Average = (First_num+Second_num+Third_num)/3
print(
    "The average of ",First_num,",",Second_num,"and",Third_num,"is  :   ", Average
)

print("\n \n")

# Write a python program to compute a person's income tax

print("-------2------\n")
print("To compute a person's income tax")
Income = int(input("Enter your Gross Income   :   "))
Dependents = int(input("Enter the number of Dependents  :   "))
# Taxable income = Gross Income - Standard deduction - (Dependent deduction * No. of dependents)
Taxable_Income = Income -10000 - 3000*Dependents
# Tax = Taxable Income * Tax Rate
Income_Tax = Taxable_Income*0.2
print("Your income tax is  : ",Income_Tax)

print("\n \n")

#Write a python program to store different data type values into a list

print("-------3------\n")
print("To store different data type values into a list")
Name = str(input("Enter your Name   :   "))
SID = int(input("Enter your SID :   "))
print("If Male,type 'M', if Female, type 'F' and if Others typr, 'U'")
Gender = input("Enter your Gender   :   ")
Cousre = input("Enter the Course you are enrolled   :   ")
CGPA = float(input("Enter your CGPA   :   "))
Student_Info = [SID,Name,Gender,Cousre,CGPA]
print("Student", Student_Info)


print("\n \n")

#Write a python program to enter marks of 5 students into a list and display them in sorted manner

print("-------4------\n")
print(
    "to enter marks of 5 students into a list and display them in sorted manner"
)
First_st = float(input("Enter the marks of First Student   :   "))
Second_st = float(input("Enter the marks of Second Student   :   "))
Third_st  = float(input("Enter the marks of Third Student   :   "))
Fourth_st = float(input("Enter the marks of Fourth Student   :   "))
Fifth_st = float(input("Enter the marks of Fifth Student   :   "))
Marks_list = [ First_st, Second_st , Third_st, Fourth_st, Fifth_st ]
Marks_list.sort()
print(Marks_list)


print("\n \n")

#Write a Python program to print a specified list after removing 4th element

print("-------5 a------ \n")
print("Removing element 4 from List")
Colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(Colors)
del Colors[3]
print("After Deleting, List Is  :   color",Colors)

print("\n \n")

print("-------5 b------ \n")
print("Replacing 'Black' and 'Pink' with 'Purple'")
Colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(Colors)
Colors[3:5] = ['Purple']
print("After Replacing, List is : color",Colors)
