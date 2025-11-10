# Instructions:
# 1. Ask for User Input:

# The string must be exactly 10 characters long.
# 2. Check the Length of the String:

# If the string is less than 10 characters, print: "String not long enough."
# If the string is more than 10 characters, print: "String too long."
# If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
# 3. Print the First and Last Characters:

# Once the string is validated, print the first and last characters.
# 4. Build the String Character by Character:

# Using a for loop, construct and print the string character by character. Start with the first character, then the first two characters, and so on, until the entire string is printed.
# Hint: You can create a loop that goes through the string, adding one character at a time, and print it progressively.

# Example:

# Alt text

# 5. Bonus: Jumble the String (Optional)

# As a bonus, try shuffling the characters in the string and print the newly jumbled string.
# Hint: You can use the random.shuffle function to shuffle a list of characters.



#import random

rope = input('Write a 10-character string: ')
if len(rope) < 10:
    print ('String not long enough')
if len(rope) > 10:
    print('String too long')
if len(rope) == 10:
    print('Perfect string')
    print(rope[0], rope[-1])

for char in rope:
    print(char)

# for i in range(len(rope)):
#     print(rope[i])



# my_range = range(0,-2,-1)

# for index in my_range:
#     print(rope[index])

# rope_list = list(rope)
# rope_list = []
# for char in rope:
#     rope_list += [char]

# print(rope_list)
# random.shuffle(rope_list)
# print(rope_list)
# restringed_rope = "".join(rope_list)
# print(restringed_rope)


# my_word = "oh"
# my_word_length = len(my_word)
# my_message = "oh my word, my word's length is "+str(my_word_length)
# print(my_message)