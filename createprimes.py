
primes = []

def is_prime(i, primes):
    for prime in primes:
        if prime <= i ** 0.5:
            if i % prime == 0:
                return False
    return True

with open("primes.txt", 'w') as file:

    for i in range(2, 10**9):
        if is_prime(i, primes):
            primes.append(i)
            file.write(f"{i}\n")


        if i % 1000 == 0:
            print(i)


