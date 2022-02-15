# ASSIGNMENT 3


print("\n\n" , "-"*70,"\n" , "1".center(70," ") ,"\n" ,"-"*70 ,"\n")
print("COUNTING THE NUMBER OF WORDS OR LETTERS (in case of single word)\n\n")


# QUESTION 1
# To count the number of occurences of each character and words in string enterd by user

Given_string = input("Enter the String to count\t:\t").lower().replace(",", " ").replace(".", " ")

if Given_string.strip() == "":
    print("\nYou Have Entered Nothing")
    exit()

if " " in Given_string:
    Given_string = Given_string.split()


#TO COUNT THE NO. OF OCCURENCES OF EACH CHARACTER or WORD

repeat_cha = []                                     #list of elements that have been counted so no repetition occurs

print("\n\nCHARACTER\t\t :\tNo. Of TIMES OCCURED\n")

for cha_ in Given_string:                           #cha_ is character or word in string
    
    if len(cha_) < 7:                               #for right positioning of tabs
        n = 3
    elif len(cha_)< 16:                            
        n=2
    elif len(cha_)< 24:
        n=1


    if cha_ not in repeat_cha:
        Counting = Given_string.count(cha_)         #this counts the no. of occurences
        repeat_cha.append(cha_)
        print(cha_ , "\t"*n, ":\t" , Counting)




print("\n\n" , "-"*70,"\n" , "2".center(70," ") ,"\n" ,"-"*70 ,"\n")
print("FINDING THE NEXT DATE\n\n")



# QUESTION 2
# TO FIND THE NEXT DATE OF INPUT DATE


def leap_year(Year):                                                        # Function for leap year
    if Year%4 == 0 and Year%400 not in [100,200,300]:
        return True
    else:
        return None


Days_31 = [1, 3, 5, 7, 8, 10, 12]                                           # list of months with 31 days
Days_30 = [4,6,9,11]                                                        # list of months with 30 days

while True:                                                                 # loop for repeatition of input for wrong date

    Date = int(input("Enter The Date\t:\t"))
    Month = int(input("Enter The Month\t:\t"))
    Year = int(input("Enter The Year\t:\t"))

    if 1 <= Month <= 12 and 1800 <= Year <= 2025 and Date > 0:

        if leap_year(Year) and Month == 2 and Date<=29:
            break
        elif Month == 2 and Date <= 28:
            break
        elif Month in Days_30 and Date <= 30:
            break
        elif Month in Days_31 and Date <= 31:
            break
        else:
            print("\nThe Date Entered By you is NOT POSSIBLE\nEnter it again\n")

    else:
        print("\nThe Date Entered by you is out of range\nEnter the date ranging from 1800 to 2025\n")


# For Normal Case  '_N' represents particulars of next day

Year_N = Year
Date_N = Date + 1
Month_N = Month


if Month in Days_31 and Date == 31 or Month in Days_30 and Date == 30:
        Date_N = 1
        
        if Month == 12:                                 # Special case for Year end
            Month_N = 1 
            Year_N = Year + 1
        else:
            Month_N = Month + 1

elif Month == 2:                                        # Special case for FEB month

    if leap_year(Year):

        if Date == 29:
            Month_N = Month + 1
            Date_N = 1

    else:

        if Date == 28:
            Month_N = Month + 1
            Date_N = 1


print(
    "Next date of {}/{}/{} is\t:\t {}/{}/{}".format(Date, Month, Year, Date_N, Month_N, Year_N)
)




print("\n\n" , "-"*70,"\n" , "3".center(70," ") ,"\n" ,"-"*70 ,"\n")
print("SQUARING THE NUMBERS\n\n")



# QUESTION 3
# TO CREATE A LIST OF TUPLES WITH SECOND NUMBER AS A SQUARE OF FIRST NUMBER


print("Write The Numbers sepearted by a space in them ' ' ")
Given_Numbers = input().split()

Final = []

for num in Given_Numbers:
    square = (int(num))**2
    
    t = (int(num), square)
    Final.append(t)

print("\nThe numbers and their Squares are written in form \'(NUMBER, SQUARE)\' \n", Final)




print("\n\n" , "-"*70,"\n" , "4".center(70," ") ,"\n" ,"-"*70 ,"\n")
print("GET GRADE ON BASIS OG GRADE POINTS\n\n")



# QUESTION 4
# TO GIVE THE LETTER GRADE ON BASIS GRADE POINTS


while True:
    
    Grade = int(input("Enter the Grade Points\t:\t"))

    if 4 <= Grade <= 10:
        break
    else:
        print("\nEnter the Grade Point in range 4 to 10\n")


Letter_Gra = {}                                     # Dictionary of Grade point and letter grade
Performance = {}                                    # Dictionary of Grade point and Performace


if Grade == 10:
    Letter_Gra['10'] = "A+"
    Performance['10'] = "Outstanding"

elif Grade == 9:
    Letter_Gra['9'] = "A"
    Performance['9'] = "Excellent"
    
elif Grade == 8:
    Letter_Gra['8'] = "B+"
    Performance['8'] = "Very Good"
    
elif Grade == 7:
    Letter_Gra['7'] = "B"
    Performance['7'] = "Good"
     
elif Grade == 6:
    Letter_Gra['6'] = "C+"
    Performance['6'] = "Average"
    
elif Grade == 5:
    Letter_Gra['5'] = "C"
    Performance['5'] = "Below Average"
    
elif Grade == 4:
    Letter_Gra['4'] = "D"
    Performance['4'] = "Poor"


print("Your Grade is '{}' and {} Performance".format(Letter_Gra[str(Grade)], Performance[str(Grade)]))




print("\n\n" , "-"*70,"\n" , "5".center(70," ") ,"\n" ,"-"*70 ,"\n")
print("REVERSE PYRAMID PATTERN \n\n")



# QUESTION 5
# TO PRINT THE PATTERN OF ALPHABETS


# ASCII for 'A' is 65,
# For 'B' is 66 and so on and
# for 'K' is 75


for i in range(6):
    print(" "*i, end="")                    # Printing spaces before text

    for n in range(65, 76 - 2*(i)):
        print(chr(n), end="")

    print("")




print("\n" , "-"*70,"\n" , "6".center(70," ") ,"\n" ,"-"*70 ," \n")
print("STORING STUDENTs INFO\n\n")


# QUESTION 6
# TO STORE THE INFO OF STUDENTS IN DICTIONARY


# Function that gives the 'key' in dictionary while searching with 'value'
def get_key(val, dicti):
    for key, value in dicti.items():
        if val == value:
            return key


# PART A
Response = "Y"
SID_Info = {}


while Response == "Y":
    Name = input("Enter the Name of the Student\t:\t")
    SID  = int(input("Enter the SID of the Student\t:\t"))
    SID_Info[SID] = Name

    while True:                                         #  loop for asling user to add another details
        Response = input(
            "Type 'Y' if want Add another Student's Details or Type 'N' if doesnot want to Add\t:\t"
        ).upper()

        if Response == "Y" or Response =="N":
            break
        else:
            print("\nEnter The Correct Response\n")
    
    if Response == "N":
        break
    
print("\n\n","PART A".center(20,"-"))
print("\nStudents details are in form (SID: NAME)\n",SID_Info)



# PART B
# TO SORT THE DICTIONARY WITH RESPECT TO SIDs

Sorted_SIDs = sorted(SID_Info.keys())
SID_sort = {}

for sid in Sorted_SIDs:
    SID_sort[sid] = SID_Info[sid]

print("\n\n","PART B".center(20,"-"))
print("\nStudents Details in sorted SIDs form are as Follows:\n",SID_sort)



# PART C
# TO SORT0 THE DICTIONARY WITH RESPECT TO NAMEs

Sorted_Names = sorted(SID_Info.values())
Name_sort = {}

for s_name in Sorted_Names:
    s_sid = get_key(s_name, SID_sort)
    Name_sort[s_sid] = s_name


print("\n\n","PART C".center(20,"-"))
print("\nStudents Details in sorted NAMEs form are as Follows:\n", Name_sort)



# PART D
# TO SEARCH THE STUDENT NAME FROM SID

print("\n\n","PART D".center(20,"-"))

while True:
    SID_search = int(input("\n\nEnter the SID to search the Name\t:\t"))

    if SID_search in SID_Info:
        print(f"\nThe NAME of the STUDENT with SID \'{SID_search}\' is \t:\t", SID_Info[SID_search])
        break
    else:
        print("\nEnter the SID that has been already added by you")




print("\n\n" , "-"*70,"\n" , "7".center(70," ") ,"\n" ,"-"*70 ,"\n")
print("FIBBONACCI SERIES\n\n")


# QUESTION 7
# TO PRINT THE FIBONACCI SERIERS


n = int(input("ENTER THE NO. OF TERMS YOU WANT THE FIBONACCI SERIES \t:\t"))
Sum = 0
Terms_list =[]

for i in range(n):

    if i==0:
        Term = 0
    elif i == 1:
        Term = 1
    else:
        Term = Terms_list[i-1] + Terms_list[i-2]

    Terms_list.append(Term)
    Sum = Sum + Term


for i in range(n):
    
    if (i)%10 == 0:
        print()
    print(Terms_list[i], end="\t")


Average = Sum/n
print("\n\nThe Average of FIRST \'" + str(n) + "\' terms of FIBONACI Series is \t:\t" ,Average)




print("\n\n" , "-"*70,"\n" , "8".center(70," ") ,"\n" ,"-"*70 ,"\n \n")



# QUESTION 8
# GIVEN SETS


Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

# PART A
# Set of Elements that are in Set1 and Set2 but not in both
Set_A = (Set1|Set2) - (Set1&Set2)

# PART B
# Set of Elements that are exactlyin only Set
Set_C = (Set1 & Set2)|(Set2 & Set3)|(Set3 & Set1)

# PART C
# Set of Elements that are exactly in two Sets
Set_B = (Set1|Set2|Set3) - Set_C

# PART D
# Set of integers from 1 to 10 that are not in Set1
Set_D = set(range(1,11)) - Set1


# PART E
# Set of integers from 1 to 10 that are not in all the three Sets
Set_E = set(range(1,11)) - Set1 - Set2 - Set3

print("GIVEN SETS")
print("------------\n")
print("Set1 is \t:\t", Set1)
print("Set2 is \t:\t", Set2)
print("Set3 is \t:\t", Set3)

# PART A
print("\n\n","PART A".center(20,"-"))
print("\nSet of Elements that are in Set1 and Set2 but not in both\t:\t", Set_A)

# PART B
print("\n\n","PART B".center(20,"-"))
print("\nSet of Elements that are exactlyin only Set\t\t\t:\t", Set_B)

# PART C
print("\n\n","PART C".center(20,"-"))
print("\nSet of Elements that are exactly in two Sets\t\t\t:\t", Set_C)

# PART D
print("\n\n","PART D".center(20,"-"))
print("\nSet of integers from 1 to 10 that are not in Set1\t\t:\t", Set_D)

# PART E
print("\n\n","PART E".center(20,"-"))
print("\nSet of integers from 1 to 10 that are not in all the three Sets\t:\t", Set_E)
