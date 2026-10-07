"""
a function that takes in a file with a string of different lengths and estimates how long it will take the reader to finish
the text to read.
"""
text_to_read = open("reading_text.txt", 'r' )
print(text_to_read.read())

# def time_remaining(text_to_read):
#     wpm = 200
#     length_of_text = len(text_to_read)
#     result = int(length_of_text/wpm)
#     print (result)
#     return f"you have approximatly {result} minutes estimated left"

# time_remaining(text_to_read)
