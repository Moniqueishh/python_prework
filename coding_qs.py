#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name): #Defining function 
   print ("hello_" + user_name +"!") #printing name

hello_name("USERNAME") #Calling function 

    
#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing


def first_odds(): #Defining the function
    i = 0 #starting #
    while i <= 99: #explainable
        i += 1 #adding +1 loop
        if i % 2 == 0: #finding even #'s
            continue #skipping even #'s
        print(i) #printing #'s(odds)

print(first_odds()) #Calling function 



#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

nums = [1,30,59,76,98] #create list
def max_num_in_list(a_list): #define the function
    big = max(nums) #max to find the largets #
    print(big) # print max #

max_num_in_list(nums) #calling the function 
    
#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    year = a_year #assigning the year (from the function)
    while True: #Creating a boolean/while loop
        if (year % 4 == 0) and ((year % 100 == 1) and (year % 400 == 0)): #conditions
            print(f"{year} is a leap year!") #Explainable 
            return True 
        else:
            print(f"{year} is not a leap year!") #Explainable 
            return False
        
print(is_leap_year(2000))

    
#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list): #Creating our function 

    return sorted(a_list) == list(range(min(a_list), max(a_list)+1)) #
#When you wrap list() around a call to the range() function, the output will be a list of numbers
#Find the minimum, maximum, and sum of a list of numbers: min(list), max(list), sum(list)
# +1 to go through the list 
numbers = [23, 24, 25, 26, 27,29] #Creating our list 
print(is_consecutive(numbers))
