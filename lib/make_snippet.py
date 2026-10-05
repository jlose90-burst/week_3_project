#a function called make_snippet that takes a string as an argument
# and returns the first five words and then a '...' if there are more than 
#that

# def make_snippet(string):
#     split_string = string.split()
#     if len(split_string) <= 5:
#         return string
        
#     else:
#         i = 0
#         new_string = []
#         for i in range(i, 5):
#             new_string.append(split_string[i])
#             i += 1
#         new_string.append("...")
#         result = " ".join(new_string)
#         return result

def make_snippet(string):
    split_string = string.split(" ")
    if len(split_string) > 5:
        first_five = split_string[:5]
        first_five.append("...")
        result = " ".join(first_five)
        return result

    else: return string 
