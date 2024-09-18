prime_file = "data/primes.txt"

primes = []

with open(prime_file, 'r') as file:
    for line in file:
        primes.append(int(line))

def is_prime(i, primes):
    for prime in primes:
        if prime <= i ** 0.5:
            if i % prime == 0:
                return False
    return True

i = primes[-1] +1 
with open(prime_file, 'a') as file:
    while True:
        for j in range(10**3):
            if is_prime(i, primes):
                primes.append(i)
                file.write(f"{i}\n")
            i += 1
        print(i)



