# ASSIGNMENT 4



print("\n\n" , "-"*70,"\n" , "1".center(70," ") ,"\n" ,"-"*70 ,"\n")
print("SOLVING THE PROBLEM OF TOWER OF HANOI USING RECURSION\n\n")


# QUESTION 1
# To solve the problem of TOWER OF HANOI using recursion

def Tower_Of_Hanoi(n , source, destination, auxiliary):
    if n==0:
        return
    
    Tower_Of_Hanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from ",source,"to ",destination)
    Tower_Of_Hanoi(n-1, auxiliary, destination, source)
         

Tower_Of_Hanoi(3,"A","C","B")                                             #  Calling function for 3 disks and A,B,C  are the name of rods




print("\n\n" , "-"*70,"\n" , "2".center(70," ") ,"\n" ,"-"*70 ,"\n\n")
print("PASCAL's TRIANGLE\n")



# QUESTION 2
# TO PRINT PASCAL's TRIANGLE


while True:                                                                                             
    n = int(input("Enter the Number of Rows in Pascal's Triangle\t:\t"))      
                                    
    if n > 0:
        break
    else:
        print("\nThe value of number of rows must be postive integer\n")


# Using RECURSION Method

print("\n\nThe Pascal's Triangle using 'RECURSION' method is\n")
def pascal(n, originaln=n):

    if n == 0:
        return None

    pascal(n-1,originaln)

    print(' '*(originaln-n), end='')                        #printing the spaces

    Term = 1                                                #first number is always start with 1

    for i in range(1, n+1):

        print(Term, end =' ')
        Term = Term * (n - i) // i                          #using Binomial Coefficient

    print()

pascal(n)        


# Using ITERATION Method

from math import comb

print("\n\nThe Pascal's Triangle using 'ITERATION' method is\n")

for i in range(n):                                                                                      
    print((n-i-1)*" ",end="") 

    for j in range(n):        

        if comb(i,j) != 0:                                                                              
            print(comb(i,j),end=" ")   

    print()




print("\n\n" , "-"*70,"\n" , "3".center(70," ") ,"\n" ,"-"*70 ,"\n")
print()



# QUESTION 3
# USING BUILT IN FUNCTONS TO PERFORM SOME FUNCTIONS

int_1, int_2 = map(int,input("Enter 2 numbers\t:\t").split())

Quotient = int_1 // int_2
print("Quotient is\t:\t", Quotient)

Remainder = int_1 % int_2
print("Remainder is\t:\t", Remainder)


# PART A
print("\n\n","PART A".center(20,"-"))

print("\nQuotient is Callable\t:\t", callable(Quotient))
print("Remainder is Callable\t:\t", callable(Remainder))


# PART B
print("\n\n","PART B".center(20,"-"), "\n")

if Quotient == 0:
    print("Quotient is zero.")
elif Remainder == 0:
    print("Remainder is zero.")
else:
    print("All of the values are non-zero.")


# PART C
print("\n\n","PART C".center(20,"-"), "\n")

List = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

great_4 = []

for i in range(len(List)):

    if List[i] > 4:
        great_4.append(List[i])

print(f"The Filtered Numbers that are Greater than 4 are\t:\t\n{great_4}")


# PART D
print("\n\n","PART D".center(20,"-"), "\n")

Set_Result = set(great_4)
print("Set\t:\t",Set_Result)


# PART E
print("\n\n","PART E".center(20,"-"), "\n")

Immutable_Set = frozenset(Set_Result)
print("Immutable set\t:\t",Immutable_Set)                               #Frozen Set makes the set immutable.


# PART F
print("\n\n","PART F".center(20,"-"), "\n")

print("Hash Value of the Max Value from the above set\t:\t", hash(max(Immutable_Set)))




print("\n\n" , "-"*70,"\n" , "4".center(70," ") ,"\n" ,"-"*70 ,"\n")
print("\nCreating the Class and Assigning  values for Name and Roll Numbers\n\n")



class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number

        print("Object created\n")

    def __del__(self):

        print("Object destroyed")


#Creating object

Student_1 = Student("RISHAV JINDAL",21104095)

print("The Name of the Student is '%s' and  Roll Number is %d\n" % (Student_1.name,Student_1.roll_number))

#Deleting object

del Student_1




print("\n\n" , "-"*70,"\n" , "5".center(70," ") ,"\n" ,"-"*70 ,"\n")
print("STORING THE DETAILS OF EMPLOYES\n\n")



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def print_data(self):
        print("%s has a salary of %d rupees" % (self.name,self.salary))

# Creating employee records

Employee_1 = Employee("Mehak", 40000)
Employee_2 = Employee("Ashok", 50000)
Employee_3 = Employee("Viren", 60000)


print("The current database is\n")
for i in [Employee_1,Employee_2,Employee_3]:
    i.print_data()

print("\n\nPART A".center(20,"-"), "\n")

#PART A
# Updating salary

Employee_1.salary = 70000
print("The Record of Employees after updating Salary of {} to {}".format(Employee_1.name, Employee_1.salary))
for i in [Employee_1,Employee_2,Employee_3]:
    i.print_data()

print("\n\n","PART B".center(20,"-"), "\n")

# PART B
# Deleting a Record

del Employee_3
print("The Record of Employees after Deleting Salary of {}".format(Employee_1.name))
for i in [Employee_1,Employee_2]:
    i.print_data()





print("\n\n" , "-"*70,"\n" , "6".center(70," ") ,"\n" ,"-"*70 ,"\n\n")
print("TO TEST THE FRIENDSHIP BETWEEN AND BARBIE\n\n")



def anagram(word):                              # Function to Make all Combinations of Given Word

    if len(word)==1:
        return [word]

    other_words = anagram(word[1:])
    char = word[0]
    List = []
    
    for combination in other_words:

        for i in range(len(combination)+1):
            List.append(combination[:i]+char+combination[i:])

    return List


George_Word = input("George's word\t:\t").lower().replace(" ", "")
Barbie_Word = input("Barbie's word\t:\t").lower().replace(" ", "")
Other_Words = anagram(George_Word)
print("Other possible words are\n",Other_Words)
print("\n\nIf Barbie's word is present in the list , then their friendship is real \n")

if Barbie_Word in Other_Words:
    print("The Friendship is Real.")
else:
    print("The Friendship is Fake.")
