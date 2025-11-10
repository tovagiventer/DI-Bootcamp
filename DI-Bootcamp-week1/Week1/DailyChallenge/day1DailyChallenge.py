import random

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