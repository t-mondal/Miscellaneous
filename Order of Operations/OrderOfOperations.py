# This program takes inputted numbers and a target number and produces
#  all permutations of the inputted numbers that produces the target number
#  through standard arithmetic operators and order of operations.

# import from itertools, permutations and product are used later
from itertools import permutations, combinations, product

# takes in the number of numbers
howMany = int(raw_input("How many numbers do you have? "))
# an empty list which stores the inputted numbers later
nums = []

# numbers inputted and appended to nums list
for i in range(howMany):
    nums.append(float(raw_input("Number %s: " % str(i+1))))

# target number inputted
target = raw_input("What is your target number? ")

#permutations of numbers
options = list(permutations(nums))

#number of numbers
n = howMany

# all products of operators between numbers
operations = [x for x in product(['+','-','*','/'],repeat = n-1)]

# permutation of numbers, signifying order of operations
orders = list(permutations([x for x in range(n-1)]))

# file to write to
out = open('s1.txt', 'w')

# for each permutation of numbers
for option in options:
    # for each product of n-1 operations
    for operation in operations:
        # for each order of operations
        for order in orders:
            # setting variables in more usable format
            check = list(option)
            ordr = list(order)
            oper = list(operation)
            outstring = map(str, option)

            # calculate the result and make a string of the whole calculation
            for x in range(len(order)):
                okay = True
                place = ordr.index(min(ordr))
                if oper[place] == '+':
                    check[place] = check[place] + check[place+1]
                    outstring[place] = '('+outstring[place]+'+'+outstring[place+1]+')'
                elif oper[place] == '-':
                    check[place] = check[place] - check[place+1]
                    outstring[place] = '('+outstring[place]+'-'+outstring[place+1]+')'
                elif oper[place] == '*':
                    check[place] = check[place] * check[place+1]
                    outstring[place] = '('+outstring[place]+'*'+outstring[place+1]+')'
                elif check[place+1]==0:
                    # avoiding division by 0
                    okay=False
                    break
                elif oper[place] == '/':
                    check[place] = float(check[place]) / float(check[place+1])
                    outstring[place] = '('+outstring[place]+'/'+outstring[place+1]+')'

                # taking out finished operation
                del outstring[place+1]
                del check[place+1]
                del ordr[place]
                del oper[place]

            # check if result equals target and no division by 0
            if float(check[0]) == float(target) and okay:
                out.write(''.join(outstring)[1:-1]+'\n')
                print ''.join(outstring)[1:-1]
            
