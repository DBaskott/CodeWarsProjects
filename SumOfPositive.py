def positive_sum(arr):# defines a subroutine called positive_sum with the parameter arr, All code indented inside are run as part of the subroutine. 
    if len(arr) == 0: # If the lenght of the list arr is equal to 0 run the code indented. 
        return 0 # Returns 0 as the lenght of the list is 0 completeing the additional note of the task. 
    else: #if the condition for 'if len(arr) == 0:' is not met then run the following indented code. 
        Positive_List = [i for i in arr if i >= 0]#Create a list called Positive_List, For each element in the list 'arr' check if it is greater than or equal to 0. If the element passes this condition append the element to 'Positive_list' else ignore it and move to the next element.  
        if len(Positive_List) == 0:# IF the length of 'Positive_List' is equal to 0 run the code indented. 
            return 0 # Returns 0 as no positive numbers was found from list 'arr' to add to list 'Positive_List'
        else: # if the condition for 'if len(Positive_List) == 0:' is not met then run the following indented code. 
            return sum(Positive_List)# return the sum of all elements in 'Positive_list' to complete the task. 
        
