def solution(number):# defines a subroutine called number with the parameter number, All code indented is run as part of the subroutine. 
    Number_List = list(range(0,number))#Creates a list called 'Number_list' using the range from 0 to the value of 'number' to generate the numbers. 
    Multiples_3_5 = [i for i in Number_List if i%3==0 or i%5==0]#Creates a list called 'Multiples_3_5', Then for each element in the list 'Number_List' check if it's divisible by 3 or 5 with no remainers. If the value passes that check add it to the new list, If not move to the next element. 
    No_Duplicates = list( dict.fromkeys(Multiples_3_5) )#Creates a list called 'No_Duplicates', Which is populated by converting the elements of list 'Multiples_3_5' into keys of a dictonary as a dictonary can't contain duplicate values therefore removing any duplicates.
    if len(No_Duplicates) == 0: #If the length of 'No_duplicates' is equal to 0, Then run the indented code. 
        return 0# As the length of 'No_Duplicates' is equal to 0 therefore no positive numbers were found therefore to pass one element of the task, this returns 0
    else:# If the above if condition isn't met run the indented code. 
        return (sum(No_Duplicates))# Return the sum of 'No_Duplicates', This will add all of the multiples of 3/5 found without any duplicate values to complete the task. 
