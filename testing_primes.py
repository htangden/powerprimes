def is_prime(i, primes):
    for prime in primes:
        if prime <= i ** 0.5:
            if i % prime == 0:
                return False
    return True

primes = set()

with open("data/primes.txt", 'r') as file:
    for line in file:
        primes.add(int(line))

with open("data/prime_solutions.txt", 'w') as file:
    for n in range(2, 50):
        for a in range(10**3):
            m = a**n - 1
            if m in primes:
                print(f"{m} = {a}**{n} - 1")
                file.write(f"{m} = {a}**{n} - 1\n")
