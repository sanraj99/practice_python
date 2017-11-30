# A Prime number can only divided by 1 and itself


def is_prime(num):

    for i in range(2, num):

        if (num % i) == 0:
            return False

    return True


def getPrimes(max_number):

    list_of_primes = []

    for num1 in range(2, max_number):
        if is_prime(num1):
            list_of_primes.append(num1)

    return list_of_primes


max_num_to_check = int(input("Search for Primes up to : "))

list_of_prime = getPrimes(max_num_to_check)

for prime in list_of_prime:
    print(prime)