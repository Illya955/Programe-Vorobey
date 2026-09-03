print("Illya Vorobey, IT-31")

d = 5
c = 7

n = d * c

print(f"n = {d} * {c} = {n}")

divisors = []
divisor_sum = 0

for number in range(1, n + 1):
    if n % number == 0:
        divisors.append(number)
        divisor_sum += number

print("Divisors:", *divisors)
print(f"Divisors count: {len(divisors)}, sum: {divisor_sum}")

is_prime = True

if n < 2:
    is_prime = False
else:
    for number in range(2, n):
        if n % number == 0:
            is_prime = False
            break
    else:
        is_prime = True

if is_prime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")

primes = []
prime_count = 0

for number in range(2, n + 1):
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(number)
        prime_count += 1

print("Primes up to 35:", *primes)
print(f"Primes count: {prime_count}")
