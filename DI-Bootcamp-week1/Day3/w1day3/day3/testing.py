# 1

books = [
    {"title": "Wonders of Steve", "author": "Steve", "color": "blue"},
    {"title": "Rock, Rocks, and More Rocks", "author": "Gem", "color": "red"},
    {"title": "Waters Fall in Waterfalls!", "author": "Cptn. Obvious", "color": "blue"},
    {"title": "The World Once Computers Rule", "author": "Not A. Robot", "color": "red"}
]

blue_book_authors = []

for book in books:
    if book["color"] == "blue":
        blue_book_authors.append(book["author"])

print(blue_book_authors)


# the loop can be rewritten like this to be more descriptive:

# target_color = "blue"

# for book in books:
#     book_color = book["color"]
#     if book_color == target_color:
#         book_author = book["author"]
#         blue_book_authors.append(book_author)


# What are the values of book and blue_book_authors for each iteration?
# What will be printed?


# 2

numbers = [0, 1, 2, 3, 4]
sums = [numbers[0]]

for i in range(1, len(numbers)):
    # take the current element from numbers and add it to the previous element of sums.
    # add that to sums.
    current_num = numbers[i]
    previous_sum = sums[i-1]
    new_sum = current_num + previous_sum
    sums.append(new_sum)

print(sums)


# range(start, stop, step)
my_range = range(5) # range(0, 2, 1)
print(list(my_range))