description = "strings are..."
print('strings are...'.upper())
print(description. replace('are', 'is'))
print(description[:7])

x = 1
y = 2
temp = y
y = x
x = temp
print(x, y)

#age = int(input('Enter your age:'))
#result = 100 - age
#print(f'You will turn 100 in {result} years.')
#print(f'You will turn 100 in {100 - age} years.')

x = 5
y = 10
z = 0
word1 = "hello"
word2 = "world"
print(x<y>z)
print(word1 != word2)
print(bool(z) and bool(word1))

# name = 'Alice'
# age = 30
# city = 'New York'
# print(f'Hello, {name}, you are {age} years old and live in {city}.')
# print('Hello,{}, you are {} years old and live in {}.'.format(name, age, city))

# name = input('Enter your name.')
# if len(name)<5:
#     print('You have a short name :)')

number = int(input('Enter a number between 1 and 100.'))
if (number) % 5 == 0 and (number) % 3 == 0:
    print('FizzBuzz')
elif (number) % 3 == 0 and (number) % 5 != 0:
    print('Fizz')
elif (number) % 5 == 0 and (number) % 3 != 0:
    print('Buzz')



