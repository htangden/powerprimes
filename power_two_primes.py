
def is_prime(i, primes):
    for prime in primes:
        if prime <= i ** 0.5:
            if i % prime == 0:
                return False
    return True

primes = []

with open("data/primes.txt", 'r') as file:
    for line in file:
        primes.append(int(line))


with open("data/power_two_prime.txt", 'w') as file:
    largest_prime = primes[-1]

    for prime in primes:
        m = 2**prime - 1

        if m > largest_prime**2: # can't accurately check if prime
            break 

        if is_prime(m, primes):
            file.write(f"{m} = {2}**{prime} - 1\n")
            file.flush()
