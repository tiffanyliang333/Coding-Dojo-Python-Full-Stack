# 1. Basic - Print all integers from 0 to 50.
for i in range(0,51):
    print(i)


# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1000
for x in range(1,1000):
    if x%5 == 0:
        print(x)

# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print 'Coding Dojo'.
for y in range(1,101):
    if y%10 == 0:
        print('Coding Dojo')
    elif y%5 == 0:
        print('Coding')
    else:
        print(y)

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for z in range(1,500000,2):
    sum += z
print(sum)

# 5. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
lowNum = 1
highNum = 20
mult = 3
for p in range(lowNum,highNum):
    if p%mult == 0:
        print(p)
