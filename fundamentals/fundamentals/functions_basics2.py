# 1. Countdown
def countDown(num):
    output = []
    for i in range(num, -1, -1):
        output.append(i)
    return output
print(countDown(5))

# 2. Print and Return
def print_and_return(list):
    print(list[0])
    return(list[1])
print(print_and_return([1,2]))

# 3. First Plus Length
def first_plus_length(list):
    sum = list[0] + list[len(list)-1]
    return sum
print(first_plus_length([1,2,3]))

# 4. Values Greater than Second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0, len(list)):
        if list[i] > list[1]:
            output.append(list[i])
        print(len(output))
        return(output)
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# 5. This Length, That Value
def this_length_that_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output
print(this_length_that_value(4,7))
print(this_length_that_value(6,2))