# We will practice two recursive function


def factorial(num):

    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)

    return result


def fib(num):

    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)

    return result

numFibValues = int(raw_input('How Many Fibbonacci values should be found : '))

i = 1

while i < numFibValues:

    print(fib(i))

    i += 1

print('All Done  .!!!')

# print ("!4", factorial(4))
#
# print("fib(4)", fib(4))

