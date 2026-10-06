# A function called count_words that takes a string as an argument and returns the number of words in that string.
def count_words(string):



    
    if type(string)==str:
        x = string.replace(','," ")
        
        split_string = x.split()
        return len(split_string)
    else:
        raise TypeError("must put in a string")

count_words("test,with,commas")
