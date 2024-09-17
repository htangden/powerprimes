
primes = []

def is_prime(i, primes):
    for prime in primes:
        if prime <= i ** 0.5:
            if i % prime == 0:
                return False
    return True


for i in range(2, 10**6):
    if is_prime(i, primes):
        primes.append(i)

    if i % 1000 == 0:
        print(i)

with open("primes.txt", 'w') as file:
    for prime in primes:
        file.write(f"{prime}\n")

