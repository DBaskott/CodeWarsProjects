def word_value(x):# defines a subroutine called 'word_value', All code indented is run as part of the subroutine.
    Letter_Score = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,'p': 16,'q': 17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26}# Dictionary called 'Letter_Score' using letters as keys and the values set to match scoring in task. 
    score = 0# Creates a variable called 'score' and sets the value to 0
    for i in x:# For each element in 'x' run the following indented code. 
          score = score + Letter_Score[i]# Create variable score and set it to the current value of score plus the value of the score for the letter in i. 
    return score# Return the value of score

def high(x):# defines a subroutine called 'high', All code indented is run as part of the subroutine.

    Split_words = x.split(" ")#Creates a list called 'Split_words', Each entry in the list is formed by splitting 'x' when a " " is present. 

    word_score = []# Creates a list called 'word_score'
    for i in Split_words:# For each element in 'Split_words' run the following indented code.
        word_score.append(word_value(i))#Append the word_value of i to word_score.

    High_Score = max(word_score)#Creates a variable called 'High_Score' and sets the value to the highest value in 'word_score'
    High_Score_index = word_score.index(High_Score)#Creates a variable called 'High_Score_index' and sets the value to the index of the first instance that matches 'High_Score'

    return Split_words[High_Score_index]#Returns the value from 'Split_words' that matches the value of 'High_Score_index' 
