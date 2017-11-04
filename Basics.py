"""Make a list"""
bikes = ['trek', 'redline', 'giant']
print ("first bike is: "+bikes[0])
print ("last bike is: "+bikes[-1])

for bike in bikes:
    print bike

"Adding item to a list"

bik = []
bik.append('trek')
bik.append('redline')
bik.append('giant')

"Making Numerical List"
squares = []
for x in range(1, 11):
    squares.append(x*2)
    print squares


print"One line"
squares = [x * 2 for x in range(1, 11)]
print squares

"Slice a list"
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
print first_two

"copy a list"
copy_a_bikes=bikes[:]
print copy_a_bikes

"Making  a Tupple"
dimensions = (1920, 1080)

"If Statement"
"""
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else:
    ticket_price = 15
"""
print "Looping through all key-value pairs"

fav_numbers = {'eric': 17, 'ever': 4}

for name, number in fav_numbers.items():
    print(name + ' loves ' + str(number))




